#!/usr/bin/python

import os
import random as rand
import zerorpc
import logging

class RPC(object):
	def generate(self,input):
		def get_list():
			w = open('wordlist','r')
			x = w.readlines()
			y = []
			for i in x:
				y.append(i.strip('\n'))
			return y
		
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

s = zerorpc.Server(RPC())
s.bind('tcp://127.0.0.1:8081')
s.run()
