#!/usr/bin/python
import cgitb
cgitb.enable()
import os
import logging
import random as rand
import sys
import cgi
from datetime import datetime

def log(message):
	if os.path.exists('/var/log/passgen.log'):
		r = 'a'
	else:
		r = 'w+'
	m = datetime.now().strftime('%Y:%M:%d %h:%m:%s -- ') + str(message) + '\n'
	f = open('/var/log/passgen.log',r)
	f.write(m)
	f.close()

def get_list():
	try:
		w = open('wordlist', 'r')
		x = w.readlines()
		y = []
		for i in x:
			y.append(i.strip('\n'))
		return y
	except:
		log('unable to open or get wordlist [exception in passgen:get_list()]')

def random_word(wordlist):
	try:
		l = len(wordlist) - 1
		i = rand.randint(1,int(l))
		return wordlist[i]
	except:
		log('unable to pick random word from wordlist [exception in passgen:random_word(wordlist)]')

def main():
	try:
		result = []
		wordlist = get_list()
		for x in range(0,4):
			r = random_word(wordlist)
			result.append(r)
		passwords = result[0] + ' ' + result[1] + ' ' + result[2] + ' ' + result[3]
		return passwords
	except:
		log('unable to generate random password list [exception in passgen:main()]')

if __name__ == '__main__':
	try:
		password = main()
		print 'Content-Type: text/html'
		print ''
		print '<style>h2{font-family:Helvetica,Arial,sans-serif;font-size:35px;color:#111;}</style>'
		print '<center><h2>' + str(password) + '</h2></center>'
	except:
		log('exception generated in __main__, unable to complete script [exception in passgen:__main__]')
