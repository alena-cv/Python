#!/usr/bin/python
# -*- coding: utf-8 -*-

import re    
import sys

args = sys.argv[1:] 

def check_ip(ip_addr): 
    if re.match('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', ip_addr): #проверка на ip-адрес
        return True

def check_ip_subnet(ip_subnet):
    if  re.match('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/([0-9]|[1-2][0-9]|3[0-2]))$', ip_subnet):
        return True 

def check_ip_pool(ip_pool):
    if re.match('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])-(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', ip_pool):
        return True

def match(arg):
    min_ip = arg.split('-')[0].split('.')
    max_ip = arg.split('-')[1].split('.') 
    for i in range(4):
        if int(min_ip[i]) > int(max_ip[i]):
            return 'Not valid range'
    return 'Valid range'

for arg in args:
    if check_ip(arg):
        print('{0} is ip address'.format(arg)) 
    elif check_ip_subnet(arg):
        print('{0} is ip subnet'.format(arg))
    elif check_ip_pool(arg):
        print('{0} is ip pool'.format(arg))
        print(match(arg))
    else:
        print('{0} is nothing'.format(arg))
