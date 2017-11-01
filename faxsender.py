#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# usage ./faxsender.py example.doc 2580 header
import subprocess
import os
import sys
import datetime
import random, string
import time
from pycall import CallFile, Call, Context

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def call(number):
    call = Call('SIP/Avaya/{}'.format(number), callerid="FAX Server <4444>", wait_time=60, retry_time=60, max_retries=1, variables=vars)
    x = Context('fax-tx', 's', '1')
    c = CallFile(call, x, user='asterisk')
    c.spool()

vars = {'FAXFILE': '', 'FAXHEADER': '', 'DESTINATION': '', 'LOCALID': ''}
supportedformat = ['doc', 'docx', 'txt', 'jpg']
cwd = os.getcwd() + '/'
inputfile = str(sys.argv[1])
if inputfile[-4:] == '.pdf':
    vars['FAXFILE'] = inputfile
elif inputfile[-3:] in supportedformat:
    PIPE = subprocess.PIPE
    filename = '{:%d%m%y-%H%M%S}'.format(datetime.datetime.today()) + '_' + randomword(4) + '.pdf'
    abc = subprocess.Popen(['/usr/bin/unoconv -v -f pdf' + ' -o ' + filename + ' ' + str(sys.argv[1])], shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)
    if (abc.stdout.read().decode('utf8').find('Output file') != -1) and (os.path.isfile(filename) and os.path.getsize(filename) > 0):
        filenametif = cwd + filename[:-3] + 'tif'
        zyx = subprocess.Popen(['gs -q -dNOPAUSE -dBATCH -dSAFER -sDEVICE=tiffg3 -sOutputFile=' + filenametif + ' -f ' + filename], shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)
        vars['FAXFILE'] = filenametif
        time.sleep(1)
        subprocess.call(['chown', 'asterisk.asterisk', filenametif])
    else:
        print('Unpredictable error')
else:
    print('File format don\'t supported yet')
dest = str(sys.argv[2])
if dest.isdigit():
    vars['DESTINATION'] = dest
else:
    print('Destination number error')
vars['FAXHEADER'] = str(sys.argv[3])
vars['LOCALID'] = '0322392300'
call(dest)
