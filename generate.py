#!/usr/bin/python

import os
import random as rand
import zerorpc
import logging
from datetime import datetime

def log(message):
	if os.path.exists('python.log'):
		r = 'a'
	else:
		r = 'w+'
	m = datetime.now().strftime('%Y:%M:%d %h:%m:%s -- ') + message
	f = open('python.log',r)

class RPC(object):
	def generate(self,input):
		def get_list():
			try:
				w = open('wordlist','r')
				x = w.readlines()
				y = []
				for i in x:
					y.append(i.strip('\n'))
				return y
			except:
				log('unable to get wordlist')
		
		def random_word(list):
			l = len(list)
			r = rand.randint(1,l)
			return list[r]

		def main():
			loop = 0
			result = []
			list = get_list()
			while loop < 4:
				result.append(random_word(list))
				loop = loop + 1
			passwords = result[0] + ' ' + result[1] + ' ' + result[2] + ' ' + result[3]
			return passwords
			print passwords
		return main()

if __name__ == '__main__':

	s = zerorpc.Server(RPC())
	try:
		s.bind('tcp://127.0.0.1:8081')
	except:
		log('unable to bind port to local IP')
		sys.exit(1)
	try:
		s.run()
	except:
		log('app failed to run')
		sys.exit(1)
