import bs4 as BeautifulSoup 
from html.parser import HTMLParser
import urllib.request
from urllib.request import urlopen as uReq
import urllib.parse
from bs4 import BeautifulSoup as soup
import xml.etree.cElementTree as ET
import requests 
import csv, json ,codecs,xmltodict


def get_url_content(url):

	headers = {'User-Agent': 'Mozilla/5.0'}

	f = open('dummy-page.html', encoding="utf8")
	return f.read()

def main():

	year = input("enter year ")
	name = input("enter car name which you want ! ")
	model = input("enter model ")

	url = get_url_content("https://www.carid.com/year-name-model-accessories")
	my_url = "https://www.carid.com/"+year+"-"+name+"-"+model+"-"+"accessories/"

	requests = BeautifulSoup.BeautifulSoup(url, "html.parser")
	r = requests.prettify()


	root = ET.Element("year")

	ET.SubElement(root, "year", year=year).text = year
	ET.SubElement(root, "make", name=name).text = name
	ET.SubElement(root, "model", models=model).text = model

	tree = ET.ElementTree(root)
	tree.write("products.xml")

	year  = {
	'year' : year,
	'name' : name,
	'model' : model
	}

	s = json.dumps(year)
	with open("products.json", "w")  as f :
		f.write(s)

	try:
		print(my_url)

	except:
		print (" Not found ")


def scrap(ul):
	get_url = get_url_content(ul)
	soup = BeautifulSoup.BeautifulSoup(get_url, "html.parser")

	filename = "ScrapApp\products.xls"
	f = open(filename,"w")

	ul_list = soup.findAll("ul")
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

main()
scrap("https://www.carid.com/2019-audi-a4-accessories/")