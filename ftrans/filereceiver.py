#! /usr/bin/env python3
#
#    Copyright 2015 Zumium <martin007323@gmail.com>
#
#    This file is part of ftrans.
#
#    ftrans is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    ftrans is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with ftrans.  If not, see <http:#www.gnu.org/licenses/>.
#

import socket
import os.path

def recv_file(port,block_size,timeout):
	# Set up socket
	so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	so.bind(('0.0.0.0',port))
	so.settimeout(timeout)
	# Listen on socket to be ready to receive file
	so.listen(1)
	conn,addr=so.accept()
	# Receive file name
	try:
		buf=conn.recv(block_size).decode('UTF-8')
	except TimeoutError:
		print('Error: Receive timeout.\n')
		conn.close()
		exit()
	if buf[:5]!='FILE:':
		print('Invalid control message: {0}'.format(buf[:5]))
		conn.close()
		exit()
	filename=buf[5:]
	# Setup target file
	if os.path.exists(filename):
		if input('File already exists. Sure to overwrite it? Y(es) or N(o)\n')=='N':
			conn.sendall('FILE ALREADY EXISTS'.encode('UTF-8'))
			conn.close()
	f=open(filename,'wb')
	# Receive file
	conn.sendall('READY'.encode('UTF-8'))
	buf=b'RANDOM'
	while buf!=b'':
		buf=conn.recv(block_size)
		f.write(buf)
	# Close file and socket
	f.close()
	conn.close()
	so.close()

