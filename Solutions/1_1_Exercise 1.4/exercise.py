import urllib.request
u = urllib.request.urlopen('https://ctabustracker.com/bustime/wireless/html/home.jsp?stop=14791&route=22')
from xml.etree.ElementTree import parse
doc = parse(u)
for pt in doc.findall('.//pt'):
    print(pt.text)