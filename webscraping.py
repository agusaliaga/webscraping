from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
u_client = ureq(my_url)
page_html = u_client.read()
u_client.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand,product_name,shipping\n"
f.write(headers)

for container in containers:
	#brand = container.a.div.div.a.img["title"]
	brand_container = container.findAll("a",{"class":"item-brand"})
	brand = brand_container[0].img["title"]
	
	title_container = container.findAll("a",{"class":"item-title"})
	product_name = title_container[0].text
	
	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	f.write(brand.replace(",", "|") + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()