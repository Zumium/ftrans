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

def send_file(file_path,remote_ip,port,block_size,timeout):
	#so is the control message and data transfor tunnle
	so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	so.bind(('0.0.0.0',0))
	so.settimeout(timeout)
	#Step 1: Send file name to anounce remote side to be ready to recieve file
	so.connect((remote_ip,port))
	#Expect echo 'READY'
	try:
		so.sendall('FILE:{0}'.format(os.path.basename(file_path)).encode('UTF-8'))
		reply=so.recv(block_size).decode('UTF-8')
	#Timeout when expecting reply from remote side
	except TimeoutError:
		print('Error: Contact remote side time out\n')
		so.close()
		exit()
	#Remote side is not ready for recieving files
	if reply!='READY':
		print('Error: Remote side reply :{0}'.format(reply))
		so.close()
		exit()
	#Remote side is ready, begin to sendall file
	f=open(file_path,'rb')
	buf=b'random content'
	while buf!=b'':
		buf=f.read(block_size)
		so.sendall(buf)
	f.close()
	so.close()

