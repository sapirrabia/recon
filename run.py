#!/usr/bin/env python

from google_class1 import *
from linkedin_class import *
import mysql.connector
import requests
#import dnspython as dns
import dns.resolver

class Run:

	def run_code(self):
		self.google = Google()
		self.linkedin = Linkedin()
		self.search_sub_ip("sisense.com")
		self.search_hackertarget_host("sisense.com")
		self.create_db()
		self.create_Users()
		self.print_Users()
		self.create_Server()
		self.print_Server()


	def search_sub_ip(self,company):
		sub_domains = []
		with open("sub.txt", "r") as f:
			res = f.read()
			res = res.split("\n")
			for i in res:
				if i:
					sub = i+"."+company
					sub_domains.append(sub)
#			print(sub_domains)
			self.list_sub = []
			for sub in sub_domains:
				try:
					result = dns.resolver.query(sub, 'A')
					for ipval in result:
#						print(sub, ipval.to_text())
						subd = (sub, ipval.to_text())
						self.list_sub.append(subd)
				except dns.resolver.NXDOMAIN:
					pass
				except dns.resolver.NoAnswer:
					pass
				except dns.exception.Timeout:
					pass
#			print(self.list_sub)

	def search_hackertarget_host(self, company):
		res = requests.get("https://api.hackertarget.com/hostsearch/?q="+company)
		res = res.text
		res = res.split("\n")
		dnsres = []
		self.dnshacker = []
		for i in res:
			i = i.split(",")
			dnsres.append(i)
		for i in dnsres:
			a = (i[0], i[1])
			self.dnshacker.append(a)
#		print(self.dnshacker)



	def create_db(self):
		self.db = mysql.connector.connect(
			host='localhost',
			user='root',
			password='SapRabia',
			database='testdatabase',
			auth_plugin='mysql_native_password'
			)

		self.mycursur = self.db.cursor()
		self.mycursur.execute("CREATE DATABASE testdatabase")

	def create_Users(self):
		self.db = mysql.connector.connect(
			host='localhost',
			user='root',
			password='SapRabia',
			database='testdatabase',
			auth_plugin='mysql_native_password'
			)
			
		self.mycursur = self.db.cursor()
		
		self.mycursur.execute("CREATE TABLE Users (name VARCHAR(50), title VARCHAR(100), email VARCHAR(100))")
		sql = "INSERT INTO Users (name, title, email ) VALUES ( %s, %s, %s )"
		for val in self.linkedin.empfull:
			self.mycursur.execute(sql, val)
		self.db.commit()
		
		if self.google.emails:
			sql = "INSERT INTO Users ( email ) VALUES ( %s )"
			for val in self.google.emails:
				self.mycursur.execute(sql, val)

#		mycursur.execute("DROP TABLE Users")
#		db.commit()

	def print_Users(self):
		self.db = mysql.connector.connect(
			host='localhost',
			user='root',
			password='SapRabia',
			database='testdatabase',
			auth_plugin='mysql_native_password'
			)
			
		self.mycursur = self.db.cursor()
		self.mycursur.execute("SELECT * FROM Users")
		tables = self.mycursur.fetchall()
		for x in tables:
			print(x)


	def create_Server(self):
#		mycursur.execute("DROP TABLE Server")
#		db.commit()
		self.db = mysql.connector.connect(
			host='localhost',
			user='root',
			password='SapRabia',
			database='testdatabase',
			auth_plugin='mysql_native_password'
			)
			
		self.mycursur = self.db.cursor()


		self.mycursur.execute("CREATE TABLE Server (domain VARCHAR(100), ip VARCHAR(100))")
		sql = "INSERT INTO Server (domain, ip ) VALUES ( %s, %s )"
		for val in self.list_sub:
			self.mycursur.execute(sql, val)
		self.db.commit()

		sql = "INSERT INTO Server (domain, ip ) VALUES ( %s, %s )"
		for val in self.dnshacker:
			self.mycursur.execute(sql, val)
		self.db.commit()


	def print_Server(self):
		self.db = mysql.connector.connect(
			host='localhost',
			user='root',
			password='SapRabia',
			database='testdatabase',
			auth_plugin='mysql_native_password'
			)
			
		self.mycursur = self.db.cursor()
		self.mycursur.execute("SELECT * FROM Server")
		tables = self.mycursur.fetchall()
		for x in tables:
			print(x)

run = Run()
run.run_code()
