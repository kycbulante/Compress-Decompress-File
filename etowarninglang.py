import sys
import time
import playsound
import colorama
from time import sleep
import os
import zipfile


from colorama import Back, Fore, Style
colorama.init(autoreset=True)

clear = lambda: os.system('cls')
    
print(Fore.MAGENTA + """
\n\t\t\t\t\t   &&&&&&&&&&&&&&&&&&&&&                 
\t\t\t\t\t,@@((((((((((((((((((&@@@@              
\t\t\t\t\t,@@                  (@@  @@.           
\t\t\t\t\t,@@                  (@@    @@@         
\t\t\t\t\t,@@                  (@@       @@       
\t\t\t\t\t,@@                    @@@@@@@@@@@      
\t\t\t\t\t,@@                             @@      
\t\t\t\t\t,@@                             @@      
\t\t\t\t\t,@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
\t\t\t\t\t,@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
\t\t\t\t\t,@@    @@@@@@       @@   @@.  .    @@@@@
\t\t\t\t\t,@@    @@@@@@@@   @@@@   @@.      ,@@@@@
\t\t\t\t\t,@@    @@@@@/    @@@@@   @@.  @@@@@@@@@@
\t\t\t\t\t,@@    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
\t\t\t\t\t,@@    /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/
\t\t\t\t\t,@@                             @@      
\t\t\t\t\t,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
""")
time.sleep(3)


for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("\t[%-10s] %d%%" % ('\u0003'*i, 1*i))
    sys.stdout.flush()
    sleep(0.02)

clear()
time.sleep(2)
print (Fore.BLUE + '\n\n\t\t\t\t\t\t\t Welcome...')
print (Fore.BLUE + '\n\t\t\t\t\t\t What would you like to do?')

 
choice = 1
while choice == 1 or choice == 2:
    choice = int(input ('\n\n\t[1] To compress a file \t\t\t[2] To decompress a file \t\t\t[3] EXIT\n\n\t\t\t\t Choice: '))
    try:
        if choice == 1:
            root = input ('\n\tEnter directory of the file to zip: \t\t\t\tEx. C:/Users/Downloads/New folder\n\t\t')
            root1 = input ('\n\tEnter directory to save the file: \t\t\t\tEx. C:/Users/Downloads/New folder.zip\n\t\t')
            sleep(3)
            my_zip = zipfile.ZipFile(root1,'w')
            my_zip.write(root)
            my_zip.close()
            print('\n\t\tFile compressed successfully!')
            
    except:
        print('\n\t\tFile was not compressed, Please enter a correct file path.')
    try:   
        if choice == 2:
            root = input ('\n\tEnter directory of the file to unzip: \t\t\t\tEx. C:/Users/Downloads/New folder.zip\n\t\t')
            root1 = input ('\n\tEnter directory to save the file:    \t\t\t\tEx. C:/Users/Downloads/New folder\n\t\t ')
        
            my_zip = zipfile.ZipFile(root,'r')
            my_zip.extractall(root1)
            my_zip.close()
            print('\n\t\t\t\tFile decompressed successfully!')
    except:        
        print('\n\t\tFile was not decompressed, Please enter a correct file path.')
    if choice == 3:
        print("\n\t\t\t\t\tThank you")
  
        sys.exit(0)
#C:/Users/Nancy Gaming Laptop/Desktop/SCHOOL FILES/SUMERACRUZ_JAMIEL_PROJ#2.py
##C:/Users/Nancy Gaming Laptop/Desktop/SCHOOL FILES/nazipna9.zip

    

