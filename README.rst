HappyCowler
==========
HappyCowler is a crawler and parser for extracting geospatial data from HappyCow.net. The script crawls the descriptions and coordinates from the website, and writes a KML file with the extracted information that can be used with arbitrary GPS application.

The primary reason for this crawler is that HappyCow is difficult to use on a mobile. The apps require the presence of proprietary market applications such as Google Play and payment. Thus it is not possible to obtain the app anonymously. The website itself relies heavily on Javascript, and it is next to useless on a cell phone. By crawling the database, we obtain an offline KML file that can be used with a GPS app of your choice, without Internet access.

Dependencies
============
The script works with Python 2. It relies on `Beautiful Soup<http://www.crummy.com/software/BeautifulSoup/>`_>=4 for HTML parsing.

Usage
=====
The script takes two parameters. The first is a URL for the results page of a city. The second is the name of the KML file. For example:

``$ python2 http://www.happycow.net/asia/japan/tokyo/ Tokyo_Restaurants.kml``

Installation
============
Follow the standard procedure for installing Python modules from source:

``$ sudo python2 setup.py install``

Disclaimer
==============
It is conceivable that crawling HappyCow is not legal.
