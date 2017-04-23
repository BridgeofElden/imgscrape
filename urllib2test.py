#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 19:17:12 2017

@author: larry
"""

import urllib2
page = urllib2.urlopen("https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=samsung+galaxy+s8")
http = page.read()
print(http)
import re
matches = re.match('www.(?=")+', http)
print(matches)