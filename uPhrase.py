#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

f1 = open(os.path.join(os.getcwd(), 'VietPhrase.txt'), 'rb').read().splitlines()
f2 = open(os.path.join(os.getcwd(), 'urls.txt'), 'rb').read().splitlines()
domainlist = b'|'.join(f2)
domainlist = br'/^.*?' + domainlist + br'.*?/'

result = br''''''

for item in f1:
	try:
		k, v = item.split(b'=')
		rule = domainlist + b'^$doc,replace=/' + k + b'/' + v.replace(br'/', br'\/') + b'/g'
		result += rule + b'\r\n'
	except:
		pass

f3 = open(os.path.join(os.getcwd(), 'result.txt'), 'wb')
f3.write(result)
f3.close()
