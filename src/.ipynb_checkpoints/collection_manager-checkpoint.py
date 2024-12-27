import json
from src.data_manager import load_data, save_data

class Perfume:
    def __init__(self, name, brand, scent, price):
        self.name = name
        self.brand = brand
        self.scent = scent
        self.price = price

    def __repr__(self):
        return f"Perfume(name={self.name}, brand={self.brand}, scent={self.scent}, price={self.price})"

class CollectionManager:
    def __init__(self):
        self.collection = load_data()  # Load existing collection from the JSON file

    def add_perfume(self, perfume):
        self.collection.append(perfume)
        save_data(self.collection)  # Save updated collection to the JSON file

    def edit_perfume(self, index, name=None, brand=None, scent=None, price=None):
        if name:
            self.collection[index].name = name
        if brand:
            self.collection[index].brand = brand
        if scent:
            self.collection[index].scent = scent
        if price:
            self.collection[index].price = price
        save_data(self.collection)  # Save changes to JSON file

    def delete_perfume(self, index):
        del self.collection[index]
        save_data(self.collection)  # Save updated collection to JSON file

    def view_perfumes(self):
        return self.collection  # Return the full collection list
