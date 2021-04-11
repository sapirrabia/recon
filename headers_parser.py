#!/usr/bin/env python

from pprint import pprint

def headers_parser(headers):
	parsed_headers = {}
	for header in headers.split("\n"):
		split_header = header.split(": ")
		if not header:
			continue
		parsed_headers[split_header[0]] = split_header[1]
	#pprint(parsed_headers)
	return parsed_headers



headers = '''Host: www.google.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: https://www.google.com/
Connection: keep-alive
Cookie: CGIC=Ij90ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSwqLyo7cT0wLjg; NID=204=iHMKtDwJmqaz_a-F8Y1ekPV3cO9DPP9ERnRMXnDJ__PWJjMHJSFT9GNPwkSk_wxC0JFMWh9_dymge3NHDKfUlCGSM0oyZFUPzL-i7v18bUD_0a7qYoIdnxk5f6dR2F-E8ts3rQOst6HCfthsJqqunGtbonE4NEqdaA6_eUhRHM0hywhky256mlGVEQgbsK8AxtNLmd6uuF6c9H2piPZl74stUOBeNw0KS2pgoUM; 1P_JAR=2020-10-25-09; ANID=AHWqTUm1FNTdwWRgKl76f-o5XgF9q3-EnYfD-4EkQBdBgl-vZHUo2LuBN4e6PtJm; DV=k3gCXO4eelYsYDWOpqAb4t1SG5byVVfvuV7H4kDC4gAAAAA'''




headers_parser(headers)

