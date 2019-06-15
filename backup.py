import os
import tarfile
from time import sleep

package=input("Enter Package name \n")
os.system('cls')
command="adb backup -noapk "+package

os.system('adb devices')
os.system(command)
os.system('abe.jar unpack backup.ab backup.tar')
os.system('del backup.ab')
if((os.stat('backup.tar').st_size)<1300):
 os.system('del backup.tar')
 print('\033[1;31;40m \nCheck the package is backup allowed\n')
else:
 tarfile.open('backup.tar').extractall()
 os.system('mkdir '+package)
 os.system('move apps '+package)
 os.system('cls')
 os.system('del backup.tar')
 print('\033[1;37;40m \nSuccessfully completed\n\n')
print('\033[1;37;40m Exiting in 3 seconds...')

sleep(3)