#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from headers_parser import headers_parser
from pprint import pprint
from pyhunter import PyHunter
import re
from time import sleep
from random import randint
import os




class Google:
	def __init__(self):
		self.host = 'https://www.google.com/search'
		self.session = requests.Session()
		self.links = []

		self.search(self.ask_for_keyword())

	def ask_for_keyword(self):
		keyword = input("Enter domain to search: ")
		return keyword

	def search(self, keyword, page=1):
		with open("cookies1.txt", "r") as f:
			self.headers = headers_parser(f.read())
#		self._search(keyword)
#		self._write_results()
#		sleep(randint(3,6))
#		self._parse_result(self._read_results())
#		self._save_admin(self.links)

#		self._search_for_login(keyword)
#		self._write_results()
#		sleep(randint(3,6))
#		self._parse_result(self._read_results())
#		self._save_login(self.links)

		self._search_for_pastebin(keyword)
#		self._write_results()
#		sleep(randint(3,6))
		self._parse_result(self._read_results())
		self._save_pastebin(self.links)

#		self._search_for_emails(keyword)
#		self._write_results()
#		sleep(randint(3,6))
#		self._parse_result_emails(self._read_results())
#		self._save_emails(self.links, self._read_results())

#		self._robots_txt_read(keyword)

#		self._get_emails_hunter(keyword)

#		self._get_hunter_list()

	def _search(self, keyword):
		self.params = {
			'q': 'site:'+keyword+' inurl:admin'
		}

	def _search_for_login(self, keyword):
		self.params = {
			'q': 'site:'+keyword+' inurl:login'
		}

	def _search_for_pastebin(self, keyword):
		self.params = {
			'q': 'site:pastebin.com intext:'+keyword
		}

	def _search_for_emails(self, keyword):
		self.params = {
			'q': 'site:'+keyword+' intext:@'+keyword
		}

	def _parse_result(self, html):
		soup = BeautifulSoup(html, 'html.parser')
		self.links = soup.select('.ZINbbc.xpd.O9g5cc.uUPGi .kCrYT:first-child')

	def _write_results(self):
		res = self.session.get(self.host, params=self.params, headers=self.headers)
		with open("google_class_run.html", "w") as f:
			f.write(res.text)

	def _read_results(self):
		with open("google_class_run.html", "r") as f:
			html = f.read()
		return html


	def _save_admin(self, links):
		for link in self.links:
			try:
				url = link.select_one('a')['href'].split("?q=")[-1]
				title = link.select_one("h3 div").text
				with open("admin_pages", "a") as f:
					admin_pages = f.write(url + r'\r\n\ ')
					if not admin_pages:
						print("Didn't found admin pages in google search !!")
			except:
				pass

	def _save_login(self, links):
		for link in self.links:
			try:
				url = link.select_one('a')['href'].split("?q=")[-1]
				title = link.select_one("h3 div").text
				with open("login_pages", "a") as f:
					login_pages = f.write(url + r'\r\n\ ')
					if not login_pages:
						print("Didn't found login pages in google search !!")
			except:
				pass

	def _save_pastebin(self, links):
		for link in self.links:
			try:
				url = link.select_one('a')['href'].split("?q=")[-1]
				title = link.select_one("h3 div").text
				with open("pastebin_leaks", "a") as f:
					leak = f.write(url + r'\r\n\ ')
					if not leaks:
						print("Didn't found pastebin leaks in google search!!")
			except:
				pass
				print("Didn't found pastebin leaks in google search!!")

	def _parse_result_emails(self, html):
		soup = BeautifulSoup(html, 'html.parser')
		self.links = soup.select('.ZINbbc.xpd.O9g5cc.uUPGi .kCrYT .BNeawe.s3v9rd.AP7Wnd:first-child')

	def _save_emails(self, links, html):
		soup = BeautifulSoup(html, 'html.parser')
		self.links = soup.select('.ZINbbc.xpd.O9g5cc.uUPGi .kCrYT .BNeawe.s3v9rd.AP7Wnd:first-child')
		self.emails = []
		for link in self.links:
			try:
				title = link.select_one("div").text
				lst1 = re.findall(r'[a-zA-Z0-9_.+-]+[@][a-zA-Z0-9-]+\.\w[com]+', title)
				with open("email_address1", "a") as f:
					f.write()
				if lst1:
					self.emails.append(lst1)

			except:
				pass
		if not self.emails:
			print("Didn't found Emails in google search!!")
		else:
			print(f"_save_emails: {self.emails}")

	def _robots_txt_read(self, keyword):
		try:
			res = self.session.get("https://"+keyword+"/robots.txt")
			test = res.text
			with open("robots_txt", "w") as f:
				robots = f.write(test)
				if not robots:
					print("Didn't found robots.txt file in google search !!")
		except:
			pass

	def _get_emails_hunter(self, keyword):
		res = self.session.get("https://api.hunter.io/v2/domain-search?domain="+keyword+"&api_key=f3d69a05a2684d8455a9b64325e0e2ca5219f3c4")
		jres = res.json()
		for element in jres['data']['emails']:
			#print(element['value'])
			with open("emails_hunter1", "a") as f:
				f.write(element['value'] + r'\r\n\ ')


	def _get_hunter_list(self):
		self.hunter_emails = []
		with open("emails_hunter1", "r") as f:
			mail = f.read()
			mail = mail.split("\\r\\n\\ ")
			self.hunter_emails.append(mail)
		print(f"this is hunter nails: {self.hunter_emails}")

#google = Google()
#google.search(google.ask_for_keyword())

