# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 12:52:20 2014

@author: wittek
"""
import urllib2
from time import sleep
from bs4 import BeautifulSoup

def process_tags(tag_candidates):
    tag='Other'
    for tag_candidate in tag_candidates:
        if tag_candidate.find('li',class_='vegan') != None:
            tag='Vegan'
            break
        if tag_candidate.find('li',class_='vegetarian') != None:
            tag='Vegetarian'
            break
    return tag
    
def parse_restaurant_page(restaurant_url):
    restaurant_page = urllib2.urlopen(restaurant_url)
    parsed_restaurant_html = BeautifulSoup(restaurant_page)
    gmap_link=parsed_restaurant_html.find('div', class_='map-holder').find('a')
    text_link=gmap_link.find('img').get('src')
    start=text_link.find('center=')+7
    end=text_link.find('&')
    coord2, coord1 = text_link[start:end].split(',')
    return coord1+','+coord2

def write_header(target_file):
    f = open(target_file, 'w')
    f.write('<?xml version=\'1.0\' encoding=\'UTF-8\'?>\n');
    f.write('<kml xmlns="http://earth.google.com/kml/2.1">\n');
    f.write('<Document>\n')
    f.close()

def write_footer(target_file):
    f = open(target_file, 'a')
    f.write('</Document>\n')
    f.write('</kml>\n')
    f.close()

def append_results_to_file(target_file, coordinates, names, tags, ratings, addresses, phone_numbers, opening_hours, cuisines, descriptions):
    f = open(target_file, 'a')
    for i in range(len(names)):
        f.write('  <Placemark>\n')
        f.write('    <name>' + names[i].encode('utf-8') + '</name>\n')
        f.write('    <Point>\n')
        f.write('      <coordinates>' + coordinates[i] + ',0</coordinates>\n')
        f.write('    </Point>\n')
        f.write('   <description>\n')
        f.write('     <![CDATA[ ')
        f.write(addresses[i].encode('utf-8') + '<br>')
        f.write('<b>Phone:</b> ' + phone_numbers[i].encode('utf-8') + '<br>')
        f.write('<b><u>Type</u>:</b> ' + tags[i].encode('utf-8') + ' ')
        f.write('<b><u>Rating</u>:</b> ' + ratings[i].encode('utf-8') + '<br>')
        f.write('<b><u>Cuisine</u>:</b> ' + cuisines[i].encode('utf-8') + '<br>')
        f.write('<b><u>Business hours</u>:</b><br> ' + opening_hours[i].encode('utf-8') + '<br>')
        f.write('<b><u>Description</u>:</b><br> ' + descriptions[i].encode('utf-8') + '<br>')
        f.write(' ]]>\n')
        f.write('   </description>\n')
        f.write('  </Placemark>\n')
    f.close()

def parse_results_page(results_url, page, target_file):
    page = urllib2.urlopen(results_url + page)
    parsed_html = BeautifulSoup(page)
    
    coordinates = []
    names = []
    tags = []
    ratings = []
    addresses = []
    phone_numbers = []
    opening_hours = []
    cuisines = []
    descriptions = []
    for business in parsed_html.body.findAll('article', class_='business-listing'):
        restaurant_url = 'http://www.happycow.net' + business.find('h3').find('a').get('href')
        coordinates.append(parse_restaurant_page(restaurant_url))
        names.append(business.find('h3').text)
        tags.append(process_tags(business.findAll('ul', class_='tags')))
        ratings.append(business.find('span',class_='rating').text[:3])
        addresses.append(business.find('address').text)
        phone_numbers.append(business.find('div', class_='phone').text)
        opening_hours.append(business.find('div', class_='time').text)
        cuisine = business.find('em')
        if cuisine != None:
            cuisines.append(cuisine.text[9:])
        else:
            cuisines.append('')
        descriptions.append(business.find('p').text)
        sleep(1)

    append_results_to_file(target_file, coordinates, names, tags, ratings, addresses, phone_numbers, opening_hours, cuisines, descriptions)
    next_page = parsed_html.find('span',class_='cpaging').find('a',class_='next')
    if next_page != None:
        parse_results_page(results_url, next_page.get('href'), target_file)

target_file='kml/Tokyo_Vegan_and_Vegetarian.kml'
result_page='http://www.happycow.net/asia/japan/tokyo/'
write_header(target_file)
parse_results_page(result_page,'',target_file)
write_footer(target_file)
