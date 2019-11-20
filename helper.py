import gzip
import urllib
import json
from Item import Item


def load_data_csv(filename):
    '''
    This takes the name of the  csv file and parses them into Item class objects and creates a list and a dictionary 
    and returns them.
    :param filename: The name of the csv file we are to parse data out of.
    :return: items_dict, a dictionary of Item objects with their ID as the key.
             items_list, an unsorted list of Item objects.
    '''

    items_dict = {}
    items_list = []

    # Open the file.
    f = gzip.open(filename, 'r')

    # Read the header line so we can skip it during parsing.
    f.readline()

    # Each line is one record so we parse it and create the corresponding Item object.
    for line in f.readlines():
        # Remove any quotation marks, spaces and new line characters from each entry.
        line = line.replace('"', '')
        line = line.replace(' ', '')
        line = line.replace('\n', '')

        # Split on comma to get the individual fields for each object.
        parts = line.split(",")

        item_id = str(parts[0])
        name = str(parts[1])
        brand = str(parts[2])
        retailer = str(parts[3])
        # Try to convert the fourth part of the string into the price. If the price was not specified then
        # we leave it as None.
        try:
            price = float(parts[4])
        except:
            price = None
        in_stock = parts[5] in ['yes', 'y']

        # Create an Item object with the parsed information.
        item = Item(item_id , name, brand, retailer, price, in_stock)

        # Add it to the dictionary and list.
        items_dict[item_id] = item
        items_list.append(item)
    return items_dict, items_list


def load_data_json(url):
    '''
    This takes the URL of the s3 file and parses them into Item class objects and creates a list and a dictionary 
    and returns them.
    :param url: The url of the s3 file.
    :return: items_dict, a dictionary of Item objects with their ID as the key.
             items_list, an unsorted list of Item objects.
    '''

    # Load the JSON data from the url provided.
    json_url = urllib.urlopen(url)
    data = json.loads(json_url.read())

    items_dict = {}
    items_list = []

    # Each line is one record so we parse it and create the corresponding Item object.
    # If any of the fields are empty, we set them as None
    for item in data:
        item_id = str(item['id'])
        try:
            name = str(item['name'])
        except:
            name = None
        try:
            brand = str(item['brand'])
        except:
            brand = None
        try:
            retailer = str(item['retailer'])
        except:
            retailer = None
        try:
            price = float(item['price'])
        except:
            price = None
        try:
            in_stock = str(item['in_stock']) in ['yes', 'y']
        except:
            in_stock = False

        # Create an Item object from the parsed information.
        item = Item(item_id , name, brand, retailer, price, in_stock)

        # Add the Item to the dictionary and list.
        items_dict[item_id] = item
        items_list.append(item)
    return items_dict, items_list
