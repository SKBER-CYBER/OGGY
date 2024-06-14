import os
import sys
import platform

def main():
    os.system('clear')
    os.system('rm -rf jutt.py')
    os.system('git pull')
    os.system('clear')

    try:
        if sys.argv[1] == 'update':
            os.system('rm -rf jutt.py')
    except IndexError:
        pass

    bit = platform.architecture()[0]

    if bit == '64bit':
        if not os.path.isfile('jutt'):
            os.system('curl -L https://github.com/SKBER-CYBER/cython-file/blob/main/jutt.py?raw=true -o jutt.py')
            os.system('chmod 777 jutt.py;jutt.py')
            return
        else:
            os.system('chmod 777 jutt.py;jutt.py')
            return

if __name__ == "__main__":
    main()



