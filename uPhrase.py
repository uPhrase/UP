#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
import concurrent.futures
import threading
result = []

class _BoundedPoolExecutor:

	semaphore = None

	def acquire(self):
		self.semaphore.acquire()

	def release(self, fn):
		self.semaphore.release()

	def submit(self, fn, *args, **kwargs):
		self.acquire()
		future = super().submit(fn, *args, **kwargs)
		future.add_done_callback(self.release)

		return future

class BoundedThreadPoolExecutor(_BoundedPoolExecutor, concurrent.futures.ThreadPoolExecutor):

	def __init__(self, max_workers=None):
		super().__init__(max_workers)
		self.semaphore = threading.BoundedSemaphore(self._max_workers)

class BoundedProcessPoolExecutor(_BoundedPoolExecutor, concurrent.futures.ProcessPoolExecutor):

	def __init__(self, max_workers=None):
		super().__init__(max_workers)
		self.semaphore = multiprocessing.BoundedSemaphore(self._max_workers)

def deffunc(item):
	#global result
	try:
		k, v = item.split(b'=')
		rule = domainlist + b'^$doc,replace=/' + k + b'/' + v.replace(br'/', br'\/') + b'/g'
		result.append(rule)
	except:	
		pass

print('uPhrase is running...')
f1 = open(os.path.join(os.getcwd(), 'VietPhrase.txt'), 'rb').read().splitlines()
f2 = open(os.path.join(os.getcwd(), 'urls.txt'), 'rb').read().splitlines()
domainlist = b'|'.join(f2)
domainlist = br'/^.*?' + domainlist + br'.*?/'


with BoundedThreadPoolExecutor(max_workers=64) as executor:
	for item in f1:
		executor.submit(deffunc, item)


f3 = open(os.path.join(os.getcwd(), 'result.txt'), 'wb')
f3.write(b'\r\n'.join(result))
f3.close()
