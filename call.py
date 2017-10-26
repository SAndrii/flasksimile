#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from pycall import CallFile, Call, Context

def call(number):
    call = Call('SIP/Avaya/{}'.format(number), callerid="Asterisk robot <4444>", wait_time=60, retry_time=60, max_retries=1, variables=vars)
    x = Context('fax-tx', 's', '1')
    c = CallFile(call, x, user='asterisk', archive=True)
    c.spool()

vars = {'FAXFILE': '/home/asterisk/261017.tif', 'FAXHEADER': 'loe', 'DESTINATION': '2580'}
call(vars['DESTINATION'])
