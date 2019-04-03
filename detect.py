#!/usr/bin/env python

import requests,sys,os
from multiprocessing.pool import ThreadPool

print("\t[ Coded By Deray ]\n")
class cracks:
	def __init__(self):
		self.cout=0
		self.sites()
	
	def sites(self):
		self.site=raw_input("[?] site url: ")
		if self.site =="":
			return self.sites()
		self.tridpol()
		
	def tridpol(self):
		try:
			self.p=ThreadPool(input("[?] ThreadPool: "))
		except Exception as __errors__:
			print("[!] %s"%(__errors__))
			return self.tridpol()
		self.cod()
		
	def cod(self):
		try:
			self.status=input("[?] status code: ")
		except Exception as __errors__:
			print("[!] %s"%(__errors__))
		self.lst()
		
	def lst(self):
		try:
			self.k=open(
				raw_input("[?] list: ")).read().splitlines()
			self.g=len(self.k)
		except Exception as __errors__:
			print "[!] %s"%(__errors__)
			return self.lst()
		print 
		self.p.map(self.main,self.k)
	
	def main(self,x):
		r=requests.get(self.site+"/"+x).status_code
		if r ==self.status:
			print("\r[!] %s -> %s                          "%(
				x,self.status))
		else:
			self.cout+=1
			print("\r[+] searching: %s/%s  "%(
				self.cout,self.g)),;sys.stdout.flush()
	
cracks()
