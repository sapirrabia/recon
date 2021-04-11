#!/usr/bin/env python

import requests
from headers_parser import headers_parser
import re
import smtplib
import dns.resolver
import socket


class Linkedin:

	def __init__(self):
		self.run(self.ask_for_company())
	def ask_for_company(self):
		company = input("Enter Company Name: ")
		return company

	def search_company(self, company):
		with open("cookies2.txt", "r") as f:
			self.headers = headers_parser(f.read())

		self.params = {
			'decorationId': 'com.linkedin.voyager.dash.deco.search.typeahead.GlobalTypeaheadCollection-6',
			'q': 'globalTypeahead',
			'query': company
		}

		url = "https://www.linkedin.com/voyager/api/voyagerSearchDashTypeahead"

		self.res = requests.get(url, params=self.params, headers=self.headers)

		with open("linkedin_res", "w") as f:
			f.write(self.res.text)

	def print_company(self):
		self.jres = self.res.json()

		n = 1
		for element in self.jres['data']['elements']:
			print(str(n)+") "+element['entityLockupView']['title']['text'])
			n += 1
		self.code = self.jres['data']['elements'][2]['entityLockupView']['trackingUrn']
		self.code = self.code.split(":")
		self.code = self.code[3]
#		print(self.code)

	def print_employees(self, company):
		print("\n"+company+" employees: ")
		company_link = 'https://www.linkedin.com/voyager/api/search/blended?count=10&filters=List(currentCompany-%3E'+self.code+',resultType-%3EPEOPLE)&origin=COMPANY_PAGE_CANNED_SEARCH&q=all&queryContext=List(spellCorrectionEnabled-%3Etrue,relatedSearchesEnabled-%3Etrue)&start=0'
		with open("employees_cookies.txt", "r") as f:
			self.headers = headers_parser(f.read())
		res = requests.get(company_link, headers=self.headers)
		with open("test1", "w") as f:
			f.write(res.text)
		jres = res.json()
		n=0
		a=1
		self.empd = {}
		self.employees={}
#		self.emp = []
		self.empfull = []
		mail = "@"+company+".com"
		while n <= 9:
			self.name = jres['data']['elements'][1]['elements'][int(n)]['title']['text']
			self.title = jres['data']['elements'][1]['elements'][int(n)]['headline']['text']
			self.email_employee = "sapir@sisense.com"
			nname = self.name.split(" ")
			self.employees.update({str(a):{'first_name': nname[0], 'last_name': nname[1], 'title': self.title}})
			test = self.employees[str(a)]['first_name']+"."+self.employees[str(a)]['last_name']+mail
			self.emp = (self.name, self.title, test)
			self.empfull.append(self.emp)
			n +=1
			a += 1
		i=1
		for element in self.employees:
			print(self.employees[str(i)]['first_name'], self.employees[str(i)]['last_name']+"   --->   ", self.employees[str(i)]['title'])
#			print(self.employees['first_name'], self.employees['last_name']+"   --->   ", self.employees['title'])
			i += 1
		print(self.empfull)
	def create_emails(self, company):
		mail = "@"+company+".com"
		self.employee_emails = []
		self.empfull1 = []
		i=1
		a = []
		n = 0
		b = []
		for element in self.employees:
			test = self.employees[str(i)]['first_name']+"."+self.employees[str(i)]['last_name']+mail
			self.employee_emails.append(test)
			self.employees[str(i)]['email'] = test
			i += 1
			self.empfull1.append(test)
		while n <= 9:
			a = [self.empfull[n], self.empfull1[n]]
			b.append(a)
			n += 1


	def cheack_valide(self):
		fromAddress = 'name@domain.com'

#		Simple Regex for syntax checking
		regex = '^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-z]{2,})$'

#               Email address to verify
		for mail in self.employee_emails:
			addressToVerify = str(mail)
			print("Check for: "+mail)
			addressToVerify = str(mail)

# Syntax check
			match = re.match(regex, addressToVerify)
			if match == None:
				print('Bad Syntax')
				good_syntax = input("Enter Email Address Again In Good Syntax: ")
				addressToVerify = str(good_syntax)
				match = re.match(regex, addressToVerify)
#				raise ValueError('Bad Syntax')

# Get domain for DNS lookup
			splitAddress = addressToVerify.split('@')
			domain = str(splitAddress[1])
			print('Domain:', domain)

# MX record lookup
			records = dns.resolver.query(domain, 'MX')
			mxRecord = records[0].exchange
			mxRecord = str(mxRecord)


# SMTP lib setup (use debug level for full output)
			server = smtplib.SMTP()
			server.set_debuglevel(0)

# SMTP Conversation
			server.connect(mxRecord)
			server.helo(server.local_hostname)
			server.mail(fromAddress)
			code, message = server.rcpt(str(addressToVerify))
			server.quit()

#		print(code)
#		print(message)

# Assume SMTP response 250 is success
			if code == 250:
				print('Success')
			else:
				print('Bad')


	def run(self, company):
		self.search_company(company)
		self.print_company()
		self.print_employees(company)
		self.create_emails(company)
#		self.cheack_valide()




