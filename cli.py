#!/usr/bin/env python3

import argparse
import json
from color import white, red, green, yellow, end
from proxy_extractor.extractor import extract_proxy

print('''
%s\tProxy Extractor v0.1.0
%s''' % (white, end))

parser = argparse.ArgumentParser()
parser.add_argument("--count", "-c", dest="count", type=int, help="number of proxies you want to extract (max. 300)")
parser.add_argument("--timeout", "-t", dest="timeout", type=int, help="seconds till the script will check if the proxy is working (default: 50)")
parser.add_argument('--json', help='to display proxies in json format', dest='json', action='store_true')
parser.add_argument('--https', help='to display only https supportable proxies', dest='https', action='store_true')
args = parser.parse_args()

proxy_count = args.count
proxy_json = args.json
proxy_https = args.https
proxy_timeout = args.timeout

if proxy_json:
    proxy_list = extract_proxy(proxy_https, proxy_count, proxy_timeout)
    print(proxy_list)

else:
    proxy_list = extract_proxy(proxy_https, proxy_count, proxy_timeout)
    print('''\t%-15s%s\t\t%-20s\t\t%-10s%s\n''' % (yellow, "IP:Port", "Country", "HTTPS Support", end))
    for each_proxy in proxy_list:
        print('''%-15s%s:%s%s%s\t\t%-20s%s\t\t%s%-10s%s''' % (red, each_proxy["ip"], each_proxy["port"], end, green, each_proxy["country"], end, white, each_proxy["https"].upper(), end))
