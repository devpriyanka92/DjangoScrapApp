from django.http import HttpResponse
from django.shortcuts import render, redirect
import bs4 as BeautifulSoup 
from html.parser import HTMLParser
import urllib.request
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from excel2json import convert_from_file as convert
import requests 
import csv, json
from nltk.tag.stanford import StanfordNERTagger as s

def get_url_content(url):

	headers = {'User-Agent': 'Mozilla/5.0'}
	#r = requests.get(url, headers = headers)
	#return r.text

	# for testing using content from htmnl file

	f = open('dummy-page.html', encoding="utf8")
	return f.read()

def main():

	html_doc = get_url_content("https://www.carid.com/2019-audi-a4-accessories/#spb_interioraccessories")

	soup = BeautifulSoup.BeautifulSoup(html_doc, "html.parser")


	filename = "ScrapApp\products.xls"
	f = open(filename,"w")


	ul_list = soup.findAll("ul")
	#print("ul_list: ", ul_list[0])
	ul = ul_list[0]
	a_list = ul.findAll("a", {"class": "item"}) 

	
	year_name_model_container = soup.findAll("div", {"class": "title-wrap"}) 
	year_name_model = year_name_model_container[0]

	hname = "Name Of Car, Model and year  "
	f.write(hname)
	f.write( year_name_model.text + "\n" )
	print(year_name_model.text)

	headers = "product_name	"
	f.write( headers )

	print("\n" + "   Product Name :: ")

	for a in a_list:
		try:
			print("		",a.text)

			f.write(a.text.replace(",","/") + "  " )

		except:
			print ("   No Name found")


	excel = open("ScrapApp\products.xls","r")
	json = open("ScrapApp\products.json","w")

main()



#https://www.youtube.com/watch?v=7GFXm8HUD7s
#https://docs.quandl.com/docs/in-depth-usage-1#section-filter-rows