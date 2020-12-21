# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.8.6 (default, Sep 25 2020, 09:36:53) 
# [GCC 10.2.0]
# Embedded file name: LinuxOS.py
# Compiled at: 2019-03-29 00:15:54
import os, sys
from time import sleep as timeout
from core.oscore import *

def main():
    banner()
    print '\x1b[0;31m[01] OS Menu Installation'
    print '\x1b[0;33m[02] Desktop Environment'
    print '\x1b[0;32m[03] Exit the Program\x1b[0m'
    print '\n'
    clo = raw_input('\x1b[0;31mHaN7:~#\x1b[0m ')
    if clo == '1' or clo == '01':
        print '\n    \x1b[0;36m[01] Kali Linux'
        print '    [02] Kali Nethunter'
        print '    [03] Debian 9'
        print '    [04] Ubuntu'
        print '    [05] Fedora'
        print '    [06] CentOs'
        print '    [07] Parrot Sec Os'
        print '    [08] openSUSE_leap'
        print '    [09] Alpine Os'
        print '    [10] Void Os'
        print '    [00] Back to main menu'
        print '\n'
        customosinstall = raw_input('\x1b[0;31mHaN7:~#\x1b[0m ')
        if customosinstall == '01' or customosinstall == '1':
            Kali_Linux()
        elif customosinstall == '02' or customosinstall == '2':
            Kali_Nethunter()
        elif customosinstall == '03' or customosinstall == '3':
            Debian9()
        elif customosinstall == '04' or customosinstall == '4':
            Ubuntu()
        elif customosinstall == '05' or customosinstall == '5':
            Fedora()
        elif customosinstall == '06' or customosinstall == '6':
            CentOs()
        elif customosinstall == '07' or customosinstall == '7':
            ParrotOs()
        elif customosinstall == '08' or customosinstall == '8':
            openSUSE_leap()
        elif customosinstall == '09' or customosinstall == '9':
	    Alpine()
	elif customosinstall == '10' or customosinstall == '10':
	    Void()
        elif customosinstall == '00' or customosinstall == '00':
            restart_program()
        else:
            print '\nERROR: Wrong Input'
            timeout(2)
            restart_program()
    elif clo == '02' or clo == '2':
        banner()
        print '\n     \x1b[0;32m[01] DE Ubuntu'
        print '     [02] DE Debian'
        print '     [03] DE Kali Linux'
        print '     \x1b[0;33m[04] DE Fedora'
        print '     [05] DE Parrot Sec'
        print '     [06] DE Arch Linux'
        print '     \x1b[0;31m[00] EXIT\x1b[0m'
        print '\n'
        chose = raw_input('\x1b[0;31mHaN7:~#\x1b[0m ')
        if chose == '01' or chose == '1':
            DE_Ubuntu()
        elif chose == '02' or chose == '2':
            DE_Debian()
        elif chose == '03' or chose == '3':
            DE_Kali()
        elif chose == '04' or chose == '4':
            DE_Fedora()
        elif chose == '05' or chose == '5':
            DE_Parrot()
        elif chose == '06' or chose == '6':
            DE_ARCH()
        elif chose == '00' or chose == '0':
            restart_program
        else:
            print '\nERROR: Wrong Input'
            timeout(2)
            restart_program()
    elif clo == '03' or clo == '3':
    	timeout(2)
    	print '\nAdios Hijo De Puta'
        timeout(2)
        sys.exit()
    else:
        print '\nERROR: Wrong Input'
        timeout(2)
        restart_program()


if __name__ == '__main__':
    main()
# okay decompiling LinuxOS.pyc

