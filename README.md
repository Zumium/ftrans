# ftrans

ftrans -- A simple file transmitter program

__Introducing__
---
ftrans is designed in order to transmit one single file from a machine
to another.ftrans's design target is a lightweight,quick-to-use and
extremly simple file transmitter so it doesn't consider other things
like safety.

__Dependence__
---

Python 3

__Install__
---
	sudo python3 setup.py install

__Uninstall__
---
	sudo pip3 uninstall ftrans

__Usage__
---
	usage: main.py [-h] [-s SENDTO] [-r] [-f FILE] [-b BLOCK__SIZE] [-t TIMEOUT]
               [-i]

	optional arguments:
	  -h, --help            show this help message and exit
	  -s SENDTO, --sendto SENDTO
                        specify receiver's ip address
	  -r, --receive         receive file
	  -f FILE, --file FILE  the path of to-be-transmitted file
	  -b BLOCK__SIZE, --block-size BLOCK__SIZE
	                        set transmitting block size
	  -t TIMEOUT, --timeout TIMEOUT
	                        set time out value by seconds
	  -i, --info            show license and author information
	  -n RENAME, --rename RENAME
                        rename received file.used with -r option

__License__
---
Copyright 2015-2016 Zumium <martin007323@gmail.com>

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
