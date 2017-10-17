#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from pycall import CallFile, Call, Application

def call(number):
    call = Call('SIP/{}'.format(number), callerid="Asterisk robot <4444>")
    action = Application('Playback', 'hello-world')
    c = CallFile(call, action, user='asterisk')
    c.spool()

if __name__ == '__main__':
    call(sys.argv[1])
