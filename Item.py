import json


class Item:
    def __init__(self, id, name, brand, retailer, price, in_stock):
        '''
        This is an Item object. Which will be used to store the information for the items we are parsing and storing in our
        system. 
        :param id: String, the Item's unique ID
        :param name: String, the Item's name
        :param brand: String, the Item's brand
        :param retailer: String, the retailer that currently sells the item.
        :param price: Float, the price of the item.
        :param in_stock: Boolean, Whether the item is in stock of not. 
        '''
        self.id = id
        self.name = name
        self.brand = brand
        self.retailer = retailer
        self.price = price
        self.in_stock = in_stock

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
