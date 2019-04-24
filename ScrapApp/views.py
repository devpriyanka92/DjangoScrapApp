from django.http import HttpResponse
from django.shortcuts import render, redirect
import bs4 as BeautifulSoup 
from html.parser import HTMLParser
import urllib.request
import requests 
import csv


def index(request):
	URL = "https://www.yelp.com/"
	r = requests.get(URL) 
	r = print(r.content)
	soup = BeautifulSoup.BeautifulSoup('lxml')
	r={'d':soup.prettify()}
	return render(request,'index.html',r)


def webscripimage(request):
	link = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

	ptc = requests.get(link)
	html = ptc.content
	fgn = 1
	sb = BeautifulSoup.BeautifulSoup(html,"html.parser")
	for img in sb.find_all('img'):
		lk = img.get("src")
		if lk[:1] == "/":
			lk="http:%s"%(lk)

		ime = open(r'C:\Users\KARMA\Desktop\work\DjangoScrapingApp\ScrapApp\img\%d.jpg'%(fgn),"wb")
		m = ime.write(urllib.request.urlopen(lk).read())
		p={'d':ptc,'e':html,'f':sb,'g':ime}
		ime.close()
		fgn = fgn + 1
	return render(request,'index.html',p)


def webscrip(request):
	my_url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
	uClient = requests.get(my_url)
	page_html = uClient.content
	uClient.close()
	page_soup = BeautifulSoup.BeautifulSoup(page_html,'html.parser')
	containers = page_soup.findAll("div",{"class":"_3e7xtJ"})
	
	container = containers[0]

	for container in containers:

		name = container.findAll("div",{"class":"_3wU53n"})
		name1 = name[0].text

		discription = container.findAll("div", {"class": "_3ULzGw"})
		disc = discription[0].text

		pricing = container.findAll("div",{"class":"_6BWGkk"})
		price = pricing[0].text

		ratings = container.findAll("div",{"class":"niH0FQ"})
		rat = ratings[0].text

		print(name1,disc,price,rat)

		myFile = open('ScrapApp\products.csv', 'w')  
		with myFile:  
			myFields = ['title', 'disc','ratting','price']
			writer = csv.DictWriter(myFile, fieldnames=myFields)    
			writer.writeheader()
			writer.writerow({'title': name[0].text, 'disc': discription[0].text, 'ratting':ratings[0].text, 'price':pricing[0].text.encode("utf-8") })


		data = {'title': name1, 'disc': disc, 'ratting': rat, 'price': price}
	return render(request, 'about.html', data)


	def index1(request):
	my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=video%20cards'
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	list = []

	page_soup = soup(page_html,"html.parser")
	containers = page_soup.findAll("div",{"class":"item-container"})

	filename = "ScrapApp\products.excel"
	f = open(filename,"w")

	headers = "brand,product_name,shipping"
	f.write(headers)

	for container in containers:
		
		title_container = container.findAll("a",{"class":"item-title"})
		product_name = title_container[0].text

		shipping_container = container.findAll("li",{"class":"price-ship"})
		shipping = shipping_container[0].text.strip()

		print("product_name: " + product_name)
		print("shipping: " + shipping)

		f.write(product_name.replace(",","/") + "," + shipping + "\n")

		data = {'product_name':product_name,'shipping':shipping}


	return render(request,'about.html',data)


def webscrip1(request):
	my_url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
	uClient = requests.get(my_url)
	page_html = uClient.content
	uClient.close()
	page_soup = BeautifulSoup.BeautifulSoup(page_html,'html.parser')
	containers = page_soup.findAll("div",{"class":"_3e7xtJ"})
	
	container = containers[0]

	for container in containers:

		name = container.findAll("div",{"class":"_3wU53n"})
		name1 = name[0].text

		discription = container.findAll("div", {"class": "_3ULzGw"})
		disc = discription[0].text

		pricing = container.findAll("div",{"class":"_6BWGkk"})
		price = pricing[0].text

		ratings = container.findAll("div",{"class":"niH0FQ"})
		rat = ratings[0].text

		print(name1,disc,price,rat)

		myFile = open('ScrapApp\products.csv', 'w')  
		with myFile:  
			myFields = ['title', 'disc','ratting','price']
			writer = csv.DictWriter(myFile, fieldnames=myFields)    
			writer.writeheader()
			writer.writerow({'title': name[0].text, 'disc': discription[0].text, 'ratting':ratings[0].text, 'price':pricing[0].text.encode("utf-8") })


		data = {'title': name1, 'disc': disc, 'ratting': rat, 'price': price}
	return render(request, 'about.html', data)


def yelp(request):
	url = "https://www.yelp.com/"
	name = []

	r = requests.get(url)
	soup = BeautifulSoup.BeautifulSoup(r.content)
	links = soup.find_all("strong")
	for link in links :
		#lt = "<a href='%s'>%s</a>"%(link.get("href"),link.text)
		lt = link.text
		name.append(lt)
		name.append("\\")
	return HttpResponse(name)