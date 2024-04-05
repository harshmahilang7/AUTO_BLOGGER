# -*- coding: utf-8 -*-
# @Author: Dastan_Alam
# @Date:   10-03-2024 10:45:27 PM       22:45:27
# @Last Modified by:   Dastan_Alam
# @Last Modified time: 11-03-2024 01:49:37 AM       01:49:37

import requests
from requests.exceptions import ConnectionError 
from bs4 import BeautifulSoup
# import time
# import extract_data

# def nice_print(coupon_list, title_list):
# 	for (title, coupon) in zip(title_list, coupon_list):
# 		# file.write(title + '\n' + coupon + '\n\n')
# 		# print(coupon)


import extract_data
def send_to_ext(coupon_list, title_list):
    for (title, coupon) in zip(title_list, coupon_list):
        return extract_data.url(coupon_list)

def get_coupons(go_links):
	coupons = []
	titles = []
	for coupon_link in go_links:
		res = requests.get(coupon_link)
		soup = BeautifulSoup(res.text, 'html.parser')
		coupon = soup.find('div', attrs={'class': 'ui segment'}).a['href']
		title = soup.find('h1', attrs={'class': 'ui grey header'}).getText()
		coupons.append(coupon)
		titles.append(title)
	return send_to_ext(coupons, titles)


def get_go_links(list_url):
	go_link = []
	for link in list_url:
		res = requests.get(link)
		soup = BeautifulSoup(res.text, 'html.parser')
		link_class = soup.find('div', attrs={'class': 'ui center aligned basic segment'}).a['href']
		go_link.append(link_class)
	return get_coupons(go_link)


def get_links(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text, 'html.parser')
	link_class = soup.select('.card-header')
	hn = []
	for idx, item in enumerate(link_class):
		href = link_class[idx].get('href')
		hn.append(href)
	return get_go_links(hn)


# def process():
# 	try:
# 		print('>> Enter 1 for 15 coupons or 2 for 30 coupons: ')
# 		try:
# 			num = int(input('>> Please enter a number: '))
# 			if num == 1:
# 				try:
# 					get_links('https://www.discudemy.com/all')
# 				except ConnectionError:
# 					print('[!] Please check your network connection!')
# 			elif num == 2:
# 				try:
# 					get_links('https://www.discudemy.com/all')
# 					get_links('https://www.discudemy.com/all/2')
# 				except ConnectionError:
# 					print('[!] Please check your network connection!')
# 			else:
# 				print('[!] please enter a valid number')
# 		except ValueError:
# 			print('[!] Please enter a valid number!')
# 	except KeyboardInterrupt:
# 		print('[!] CTRL + C detected\n[!] Quitting...')


# def main():
    
	# t1 = time.time()
	# process()
	# t2 = time.time()
	# print(f'Took {round(t2 - t1)} secs')


# file = open('coupons.txt', '+w', encoding='utf-8')

# main()
get_links('https://www.discudemy.com/all')
# file.close()