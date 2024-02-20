import os, sys, platform
 
os.system('rm -rf JAKA.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf JAKA.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('aws1.so'):
        os.system('curl -L https://github.com/SKBER-CYBER/JAKA/blob/main/JAKA.cpython-311.so?raw=true -o aws1.so') 
        import JAKA
    else:
        import JAKA
 

 
