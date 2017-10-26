#!/usr/bin/python
# -*- coding: utf-8 -*-

# usage ./converter.py pdf example.doc
import subprocess
import os
import sys
import datetime

filename = '{:%d%m%y-%H%M%S}'.format(datetime.datetime.today()) + '.' + str(sys.argv[1])
PIPE = subprocess.PIPE
abc = subprocess.Popen(['/usr/bin/unoconv -v -f ' + str(sys.argv[1]) + ' -o ' + filename + ' ' + str(sys.argv[2])], shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)
if (abc.stdout.read().decode('utf8').find('Output file') != -1) and (os.path.isfile(filename) and os.path.getsize(filename) > 0):
    print('Success')
else:
    print('Unpredictable error')
