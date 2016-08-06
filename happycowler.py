# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 12:52:20 2014

@author: wittek
"""
from __future__ import print_function
try:
    from urllib2 import Request, urlopen
except ImportError:
    from urllib.request import Request, urlopen
import random
import sys
from time import sleep
from bs4 import BeautifulSoup


def write_header_gpx(target_file):
    f = open(target_file, 'w')
    f.write('<?xml version=\'1.0\' encoding=\'UTF-8\'?>\n');
    f.write('<gpx version="1.0" creator="HappyCowler" xmlns="http://www.topografix.com/GPX/1/0">\n');
    f.close()

def write_footer_gpx(target_file):
    f = open(target_file, 'a')
    f.write('</gpx>\n')
    f.close()


def append_results_to_file_gpx(target_file, coordinates, names, tags, ratings,
                               addresses, phone_numbers, opening_hours,
                               cuisines, descriptions):
    f = open(target_file, 'a')
    for i in range(len(names)):
        f.write('  <wpt lat="' + coordinates[i][0] +
                '" lon="' + coordinates[i][1] + '">\n')
        f.write('    <name>' + names[i] + '</name>\n')
        f.write('        <type>Vegetarian Restaurants</type>\n')
        f.write('        <extensions><color>#b400842b</color></extensions>\n')
        f.write('   <desc>\n')
        f.write('<![CDATA[')
        f.write(addresses[i] + '\n')
        f.write('Phone: ' + phone_numbers[i] + '\n')
        f.write('Type: ' + tags[i] + '\n')
        f.write('Rating: ' + ratings[i] + '\n')
        f.write('Cuisine:  ' + cuisines[i] + '\n')
        f.write('Business hours: ' + opening_hours[i] + '\n')
        f.write('   <description>' + descriptions[i] + '\n')
        f.write(']]>\n')
        f.write('   </desc>\n')
        f.write('  </wpt>\n')
    f.close()


def write_header_kml(target_file):
    f = open(target_file, 'w')
    f.write('<?xml version=\'1.0\' encoding=\'UTF-8\'?>\n');
    f.write('<kml xmlns="http://earth.google.com/kml/2.1">\n');
    f.write('<Document>\n')
    f.close()

def write_footer_kml(target_file):
    f = open(target_file, 'a')
    f.write('</Document>\n')
    f.write('</kml>\n')
    f.close()

def append_results_to_file_kml(target_file, coordinates, names, tags, ratings,
                               addresses, phone_numbers, opening_hours,
                               cuisines, descriptions):
    f = open(target_file, 'a')
    for i in range(len(names)):
        f.write('  <Placemark>\n')
        f.write('    <name>' + names[i] + '</name>\n')
        f.write('    <Point>\n')
        f.write('      <coordinates>' + coordinates[i][1] + "," +
                coordinates[i][0] + ',0</coordinates>\n')
        f.write('    </Point>\n')
        f.write('   <description>\n')
        f.write('     <![CDATA[ ')
        f.write(addresses[i] + '<br>')
        f.write('<b>Phone:</b> ' + phone_numbers[i] + '<br>')
        f.write('<b><u>Type</u>:</b> ' + tags[i] + ' ')
        f.write('<b><u>Rating</u>:</b> ' + ratings[i] + '<br>')
        f.write('<b><u>Cuisine</u>:</b> ' + cuisines[i] + '<br>')
        f.write('<b><u>Business hours</u>:</b><br> ' + opening_hours[i] + '<br>')
        f.write('<b><u>Description</u>:</b><br> ' + descriptions[i] + '<br>')
        f.write(' ]]>\n')
        f.write('   </description>\n')
        f.write('  </Placemark>\n')
    f.close()


def write_header(target_file):
    if target_file.endswith(".kml"):
        write_header_kml(target_file)
    elif target_file.endswith(".gpx"):
        write_header_gpx(target_file)
    else:
        raise Exception("Unknown filetype")

def write_footer(target_file):
    if target_file.endswith(".kml"):
        write_footer_kml(target_file)
    elif target_file.endswith(".gpx"):
        write_footer_gpx(target_file)
    else:
        raise Exception("Unknown filetype")


def append_results_to_file(target_file, coordinates, names, tags, ratings,
                           addresses, phone_numbers, opening_hours, cuisines,
                           descriptions):
    if target_file.endswith(".kml"):
        append_results_to_file_kml(target_file, coordinates, names, tags,
                                   ratings, addresses, phone_numbers,
                                   opening_hours, cuisines, descriptions)
    elif target_file.endswith(".gpx"):
        append_results_to_file_gpx(target_file, coordinates, names, tags,
                                   ratings, addresses, phone_numbers,
                                   opening_hours, cuisines, descriptions)
    else:
        raise Exception("Unknown filetype")


def parse_restaurant_page(restaurant_url):
    req = Request(restaurant_url, headers={'User-Agent': 'Mozilla/5.0'})
    restaurant_page = urlopen(req).read()
    parsed_restaurant_html = BeautifulSoup(restaurant_page, "html.parser")
    gmap_link = parsed_restaurant_html.find("div",
                                            class_="box-map-links").find('a')
    text_link = gmap_link.attrs["href"]
    start=text_link.find('q=loc:')+6
    lat, lon = text_link[start:].split('+')
    return (lat, lon)


def parse_results_page(results_url, page_no, target_file):
    req = Request(results_url + page_no, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    parsed_html = BeautifulSoup(page, "html.parser")

    coordinates = []
    names = []
    tags = []
    ratings = []
    addresses = []
    phone_numbers = []
    opening_hours = []
    cuisines = []
    descriptions = []
    for business in parsed_html.body.findAll('div', class_="row venue-list-item fg-form"):
        restaurant_url = 'http://www.happycow.net' + business.find('a').get('href')
        coordinates.append(parse_restaurant_page(restaurant_url))
        names.append(business.find('a').text)
        tags.append(business.find('span').text)
        stars = business.find('ul', class_="venue-ratings list-inline")
        if stars is None:
            rating = "unknown"
        else:
            rating = str(len(stars.findAll("i", class_="fa fa-star")) + 0.5*
                         len(stars.findAll("i", class_="fa fa-star-half-o")))
        ratings.append(rating)
        address = None
        for p in business.findAll('p'):
           if p.find('i', class_="fa fa-map-marker"):
               address = p.text
        if address is not None:
            addresses.append(address)
        else:
            addresses.append('')
        phone_number = None
        for p in business.findAll('p'):
           if p.find('i', class_="fa fa-phone"):
               phone_number = p.text
        if phone_number is not None:
            phone_numbers.append(phone_number)
        else:
            phone_numbers.append('')
        opening_hour = business.find('span', class_='venue-hours-container')
        if opening_hour is not None:
            opening_hours.append(opening_hour.attrs['data-summary'])
        else:
            opening_hours.append('')

        cuisine = None
        for p in business.findAll('p'):
           if "uisine" in p.text:
               cuisine = p.text
        if cuisine is not None:
            cuisines.append(cuisine)
        else:
            cuisines.append('')
        divs = business.findAll("div", class_="col-xs-12")
        description = divs[-1].find('p').text
        if description is not None:
            descriptions.append(description)
        else:
            description.append('')
        sleep(0.5 + random.random())

    append_results_to_file(target_file, coordinates, names, tags, ratings,
                           addresses, phone_numbers, opening_hours, cuisines,
                           descriptions)
    pagination = parsed_html.body.find('ul', class_="pagination").findAll('a')
    for a in pagination:
        if 'aria-label' in a.attrs and a.attrs['aria-label'] == "Next":
            new_url = "http://www.happycow.net" + a.attrs['href']
            if results_url + page_no != new_url:
                parse_results_page("http://www.happycow.net", a.attrs['href'], target_file)


if len(sys.argv) != 3:
    print("Usage: python happycowler.py results_url output_file")
    exit(-1)
result_page = sys.argv[1]
target_file = sys.argv[2]
write_header(target_file)
parse_results_page(result_page,'',target_file)
write_footer(target_file)
