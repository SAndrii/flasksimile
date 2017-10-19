#!/usr/bin/python
# -*- coding: utf-8 -*-

# usage ./converter.py pdf example.doc
import subprocess
import sys

PIPE = subprocess.PIPE
abc = subprocess.Popen(['/usr/bin/unoconv -f ' + str(sys.argv[1]) + ' ' + str(sys.argv[2])], shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT, close_fds=True)
if len(abc.stdout.read()) > 1:
	print('Unpredictable error')