# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 18:01:13 2016

@author: pwittek
"""


def write_header_gpx(target_file):
    f = open(target_file, 'w')
    f.write('<?xml version=\'1.0\' encoding=\'UTF-8\'?>\n')
    f.write('<gpx version="1.0" creator="HappyCowler" xmlns="http://www.topografix.com/GPX/1/0">\n')
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
        f.write('<wpt lat="' + coordinates[i][0] +
                '" lon="' + coordinates[i][1] + '">\n')
        f.write('    <name>' + names[i].replace('&', 'and') + '</name>\n')
        if "Vegan" in tags[i]:
            f.write('    <extensions><color>#b421880d</color></extensions>\n')
        elif "Vegetarian" in tags[i]:
            f.write('    <extensions><color>#b48a2091</color></extensions>\n')
        elif "Veg-friendly" in tags[i]:
            f.write('    <extensions><color>#b4dc5d5c</color></extensions>\n')
        else:
            f.write('    <extensions><color>#b43775c5</color></extensions>\n')
        f.write('    <desc>\n')
        f.write(addresses[i].replace('&', 'and') + '\n')
        f.write('Phone: ' + phone_numbers[i] + '\n')
        if tags[i] != "":
            f.write('Type: ' + tags[i] + '\n')
        f.write('Rating: ' + ratings[i] + '\n')
        if opening_hours[i] != "" and not "Call for hours" in opening_hours[i]:
            f.write('Hours: ' + opening_hours[i].replace('&', 'and') + '\n')
        else:
            f.write('Hours: unknown\n')
        if cuisines[i] != "":
            f.write(cuisines[i].replace('&', 'and') + '\n')
        f.write('-----\n')
        f.write(descriptions[i].replace('&', 'and') + '\n')
        f.write('    </desc>\n')
        f.write('</wpt>\n')
    f.close()


def write_header_kml(target_file):
    f = open(target_file, 'w')
    f.write('<?xml version=\'1.0\' encoding=\'UTF-8\'?>\n')
    f.write('<kml xmlns="http://earth.google.com/kml/2.1">\n')
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
