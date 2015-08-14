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
import argparse
from ftrans import filesendor,filereceiver

def main():
	block_size=1234
	time_out=None
	port=7441

	parser=argparse.ArgumentParser()
	parser.add_argument('-s','--sendto',help="specify receiver's ip address")
	parser.add_argument('-r','--receive',help='receive file',action='store_true')
	parser.add_argument('-f','--file',help='the path of to-be-transmitted file')
	parser.add_argument('-b','--block-size',help='set transmitting block size')
	parser.add_argument('-t','--timeout',type=int,help='set time out value by seconds')
	parser.add_argument('-i','--info',help='show license and author information',action='store_true')
	args=parser.parse_args()

	if args.info:
		print("""\nCopyright 2015 Zumium <martin007323@gmail.com> 

ftrans is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

ftrans is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ftrans.  If not, see <http://www.gnu.org/licenses/>.\n""")
		exit()

	if not (args.sendto or args.receive):
		print('Error: Must be specific to be sendor or receiver.\n')
		exit()
	elif args.sendto and args.receive:
		print('Error: Cannot be sendor and receiver at the same time.\n')
		exit()
	elif args.sendto and (not args.file):
		print('Error: Must specify the file which is to be sent.\n')
		exit()
	elif args.receive and args.file:
		print('Error: Receiver cannot send file.\n')
		exit()
	

	if args.timeout:
		time_out=args.timeout
	if args.block_size:
		block_size=args.block_size

	if args.sendto:
		filesendor.send_file(args.file,args.sendto,port,block_size,time_out)
	else:
		filereceiver.recv_file(port,block_size,time_out)

if __name__=='__main__':
	main()
