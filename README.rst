HappyCowler
===========
HappyCowler is a crawler and parser for extracting geospatial data from HappyCow.net. The script crawls the descriptions and coordinates from the website, and writes a GPX or KML file with the extracted information. Currently, the GPX file is targeted at `Osmand <http://osmand.net/>`_.

The primary reason for this crawler is that HappyCow is difficult to use on a mobile. The apps require the presence of proprietary market applications such as Google Play and payment. Thus it is not possible to obtain the app anonymously. The website itself relies heavily on Javascript, and it is next to useless on a cell phone. By crawling the database, we obtain an offline file that can be used with a GPS app of your choice, without need for Internet access while on the go.

Dependencies
============
The script works with both Python 2 and 3. It relies on `BeautifulSoup4 <http://www.crummy.com/software/BeautifulSoup/>`_ for HTML parsing.

Usage
=====
The script takes two parameters. The first is a URL for the results page of a city. The second is the name of the KML or GPX file. For example:

``$ happycowler http://www.happycow.net/asia/japan/tokyo/ Tokyo_Restaurants.gpx``

The type of the file is determined by the extension of the filename.

Installation
============
Follow the standard procedure for installing Python modules from source:

``$ sudo python setup.py install``

Disclaimer
==========
It is conceivable that crawling HappyCow is illegal.
