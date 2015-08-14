# ftrans

ftrans -- A simple file transmitter program

Introducing

ftrans is designed in order to transmit one single file from a machine
to another.ftrans's design target is a lightweight,quick-to-use and
extremly simple file transmitter so it doesn't consider other things
like safety.

	usage: main.py [-h] [-s SENDTO] [-r] [-f FILE] [-b BLOCK_SIZE] [-t TIMEOUT]
               [-i]

	optional arguments:
	  -h, --help            show this help message and exit
	  -s SENDTO, --sendto SENDTO
                        specify receiver's ip address
	  -r, --receive         receive file
	  -f FILE, --file FILE  the path of to-be-transmitted file
	  -b BLOCK_SIZE, --block-size BLOCK_SIZE
	                        set transmitting block size
	  -t TIMEOUT, --timeout TIMEOUT
	                        set time out value by seconds
	  -i, --info            show license and author information

License

	Copyright 2015 Zumium <martin007323@gmail.com>
	
	ftrans is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.
	
	ftrans is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.
	
	You should have received a copy of the GNU General Public License
	along with ftrans.  If not, see <http://www.gnu.org/licenses/>.
