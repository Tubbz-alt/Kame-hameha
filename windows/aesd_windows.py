import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os,re
def aes_decrypt(filename):
    a = filename.split('\\')
    file1 = ''
    for i in range(len(a)-1):
        file1 += a[i]+'\\\\'
    name=a[len(a)-1]
    b64 = json.loads(open(filename,'r').read())
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    keys = open('res/key.txt','r').readlines()
    for line in keys:
        x = re.findall("[A-Z]:.*:", line)
        print(file1+name.split('.')[0])
        if(file1+name.split('.')[0] ==x[0][:-1] ):
            key = re.split("[A-Z]:.*:", line)[1]
    key = b64decode(key)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    os.remove(filename)
    open(filename[:-4],'w').write(pt.decode())
