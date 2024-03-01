#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

f1 = open(os.path.join(os.getcwd(), 'VietPhrase.txt'), 'rb').read().splitlines()
f2 = open(os.path.join(os.getcwd(), 'urls.txt'), 'rb').read().splitlines()
domainlist = b'|'.join(f2)
domainlist = br'/^.*?' + domainlist + br'.*?/'

result = br'''[Adblock Plus 2.0]
! Title: uPhrase
! Description: Filters I use myself but may cause unintended effects of other users. Mostly peculiar YouTube filters.
! Homepage: https://github.com/gunir/filterlists
! Expires: 7 days (update frequency)
! Version: 2 November 2023
! Syntax: AdBlock

'''

for item in f1:
	k, v = item.split(b'=')
	rule = domainlist + b'^$doc,replace=/' + k + b'/' + v.replace(br'/', br'\/') + b'/g'
	result += rule + b'\r\n'

f3 = open(os.path.join(os.getcwd(), 'result.txt'), 'wb')
f3.write(result)
f3.close()
