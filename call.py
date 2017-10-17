#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from pycall import CallFile, Call, Application

def call(number):
    call = Call('SIP/{}'.format(number), callerid="Asterisk robot <4444>", wait_time=60, retry_time=60, max_retries=2, variables=vars)
    action = Application('Playback', 'hello-world')
    c = CallFile(call, action, user='asterisk', archive=True)
    c.spool()

vars = {'FAXFILE': 'some.pdf', 'FAXHEADER': '', 'DESTINATION': '', 'EMAIL': 'andriyshvorak@gmail.com'}

if __name__ == '__main__':
    call(sys.argv[1])
