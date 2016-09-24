HappyCowler
===========
HappyCowler is a crawler and parser for extracting geospatial data from `HappyCow.net <https://happycow.net/>`_ that liberates vegans and vegetarians from having to access the Internet while looking for a restaurant. The script crawls the descriptions and coordinates from the website and generates a GPX or KML file with the extracted information. Currently, the GPX file is tuned for `Osmand <http://osmand.net/>`_.

The primary reason for this crawler is that HappyCow is impossible to use on a mobile browser. While apps are available, they require the presence of proprietary applications such as Google Play. Furthermore, a payment is also required. Thus it is not possible to obtain the app without sacrificing your privacy. By crawling the database, we obtain an offline file that can be used with a GPS app of your choice, without need for Internet access while on the go.

Dependencies
============
The script works with both Python 2 and 3. It relies on `BeautifulSoup4 <http://www.crummy.com/software/BeautifulSoup/>`_ for HTML parsing.

Usage
=====
On the command line, the script takes two parameters. The first is a URL for the results page of a city. The second is the name of the GPX or KML file. For example:

``$ happycowl http://www.happycow.net/asia/japan/tokyo/ Tokyo_Restaurants.gpx``

The type of the file is determined by the extension of the filename. Once the scraping finished, copy the file to your phone where your mapping app can find it. For instance, in Osmand, the contents of the folder ``osmand/tracks`` can easily be put on the map.

You can also use it as a module. In this case, instantiate the  class `HappyCow(city_url, target_file=None, verbose=0)`. Then you can start crawling by calling the `crawl()` method of the class.


Installation
============
The code is available on PyPI, hence it can be installed by

``$ pip install happycowler``

For the development version, clone it from git and follow the standard
procedure for installing Python modules from source:

``$ python setup.py install``

Disclaimer
==========
It is conceivable that crawling HappyCow is illegal.
