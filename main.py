from flask import Flask
from helper import load_data_csv, load_data_json
import json

app = Flask(__name__)


@app.route('/search/<item_id>')
def search(item_id):
    '''
        This takes an item's ID and returns a JSON object with the item's details. 
        :param item_id: String, the item's unique ID.
        :return: Item: JSON, a JSON copy of the item's details.
    '''
    return app.config.get('dict_data')[str(item_id)].toJSON()


@app.route('/cheapest/<count>')
def cheapest(count):
    '''
    Returns a list of the N cheapest items available, where N is the count specified by the user in the URL.
    :param count: int, the number of cheap items we want to see.
    :return: a list of the N cheapest objects in JSON format.
    '''
    items = app.config.get('sorted_data')[:int(count)]
    return json.dumps([ob.__dict__ for ob in items])


if __name__ == '__main__':

    # Load the data from the CSV file first.
    csv_filename = 'products.csv.gz'
    dict_data_csv, list_data_csv = load_data_csv(csv_filename)

    # Load the data from the s3 file.
    url = "https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/python-software-developer/products.json"
    dict_data_json, list_data_json = load_data_json(url)

    # Combine the two dictionaries into one so that we only have to perform a lookup once.
    dict_data_csv.update(dict_data_json)

    # Store the dictionary in the app's configuration.
    app.config['dict_data'] = dict_data_csv

    # Combine the two lists of unsorted data into one.
    combined_final_data = list_data_csv + list_data_json

    # Remove any items with None price, as we do not want to see those when searching for cheap items.
    no_null_final_data = [x for x in combined_final_data if x.price is not None]

    # Sort the list by increasing prices to make it easier to find the N cheapest items.
    sorted_final_data = sorted(no_null_final_data, key=lambda y: y.price)

    # Store the sorted list in the app's configuration.
    app.config['sorted_data'] = sorted_final_data

    # Once all the data has been parsed and sorted the way we want it, the server starts.
    app.run(debug=True)
