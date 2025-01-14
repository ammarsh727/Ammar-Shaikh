import json
import ipywidgets as widgets
from IPython.display import display
from IPython.display import clear_output
import matplotlib.pyplot as plt
from collections import Counter


# Data management functions
def load_data():
    try:
        with open('perfumes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open('perfumes.json', 'w') as file:
        json.dump(data, file)

SCENT_OPTIONS = [
    'Floral', 'Fruity', 'Citrus', 'Woody', 'Oriental', 'Fresh',
    'Spicy', 'Green', 'Aquatic', 'Gourmand', 'Chypre', 'Leather',
    'Musk', 'Powdery', 'Vanilla', 'Amber', 'Other'
]

# Perfume class
class Perfume:
    def __init__(self, name, brand, scent, price):
        self.name = name
        self.brand = brand
        self.scent = scent
        self.price = price

    def __repr__(self):
        return f"Perfume(name={self.name}, brand={self.brand}, scent={self.scent}, price={self.price})"

# Collection Manager class
class CollectionManager:
    def __init__(self):
        self.collection = load_data()

    def add_perfume(self, perfume):
        self.collection.append(perfume.__dict__)
        save_data(self.collection)

    def edit_perfume(self, index, name=None, brand=None, scent=None, price=None):
        if 0 <= index < len(self.collection):
            if name:
                self.collection[index]['name'] = name
            if brand:
                self.collection[index]['brand'] = brand
            if scent:
                self.collection[index]['scent'] = scent
            if price:
                self.collection[index]['price'] = price
            save_data(self.collection)

    def delete_perfume(self, index):
        if 0 <= index < len(self.collection):
            del self.collection[index]
            save_data(self.collection)

    def view_perfumes(self):
        return self.collection

# Create global CollectionManager instance
manager = CollectionManager()

# Functions to handle actions
def display_perfumes():
    perfumes = manager.view_perfumes()
    if perfumes:
        for idx, perfume in enumerate(perfumes):
            print(f"{idx + 1}. {perfume['name']} - {perfume['brand']}, {perfume['scent']}, £{perfume['price']}")
    else:
        print("No perfumes in collection.")

def get_scent():
    return other_scent_widget.value if scent_widget.value == 'Other' else scent_widget.value

def add_perfume(_):
    name = name_widget.value
    brand = brand_widget.value
    scent = get_scent()
    price = float(price_widget.value)
    perfume = Perfume(name, brand, scent, price)
    manager.add_perfume(perfume)
    print("Perfume added successfully!")
    display_perfumes()

def edit_perfume(_):
    perfumes = manager.view_perfumes()
    if not perfumes:
        print("No perfumes to edit.")
        return

    index = int(edit_index_widget.value) - 1
    name = name_widget.value or None
    brand = brand_widget.value or None
    scent = get_scent() or None
    price = price_widget.value or None
    manager.edit_perfume(index, name, brand, scent, price)
    print("Perfume updated successfully!")
    display_perfumes()

def delete_perfume(_):
    perfumes = manager.view_perfumes()
    if not perfumes:
        print("No perfumes to delete.")
        return

    index = int(delete_index_widget.value) - 1
    manager.delete_perfume(index)
    print("Perfume deleted successfully!")
    display_perfumes()

def view_perfumes(_):
    display_perfumes()

def exit_interface(_):
    clear_output()
    print("Thank you for using the Perfume Collection Manager. The interface has been closed.")
    # This will remove all the widgets from display
    for widget in [name_widget, brand_widget, scent_widget, other_scent_widget, price_widget, 
                   edit_index_widget, delete_index_widget, add_button, 
                   edit_button, delete_button, view_button, exit_button, visualise_brands_button, visualise_scents_button, 
        visualise_prices_button, visualise_price_vs_brand_button,
        generate_summary_button]:
        widget.close()

# Data visualisation functions
def visualise_brands():
    perfumes = manager.view_perfumes()
    brands = [perfume['brand'] for perfume in perfumes]
    brand_counts = Counter(brands)
    
    plt.figure(figsize=(10, 6))
    plt.bar(brand_counts.keys(), brand_counts.values())
    plt.title('Number of Perfumes by Brand')
    plt.xlabel('Brand')
    plt.ylabel('Number of Perfumes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualise_scents():
    perfumes = manager.view_perfumes()
    scents = [perfume['scent'] for perfume in perfumes]
    scent_counts = Counter(scents)
    
    plt.figure(figsize=(8, 8))
    plt.pie(scent_counts.values(), labels=scent_counts.keys(), autopct='%1.1f%%')
    plt.title('Distribution of Perfume Scents')
    plt.axis('equal')
    plt.show()

def visualise_price_range():
    perfumes = manager.view_perfumes()
    prices = [perfume['price'] for perfume in perfumes]
    
    plt.figure(figsize=(10, 6))
    plt.hist(prices, bins=10, edgecolor='black')
    plt.title('Distribution of Perfume Prices')
    plt.xlabel('Price (£)')
    plt.ylabel('Number of Perfumes')
    plt.show()

def visualise_price_vs_brand():
    perfumes = manager.view_perfumes()
    brands = [perfume['brand'] for perfume in perfumes]
    prices = [perfume['price'] for perfume in perfumes]
    
    plt.figure(figsize=(12, 6))
    plt.scatter(brands, prices)
    plt.title('Perfume Prices by Brand')
    plt.xlabel('Brand')
    plt.ylabel('Price (£)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to generate a summary report
def generate_summary():
    perfumes = manager.view_perfumes()
    total_perfumes = len(perfumes)
    total_value = sum(perfume['price'] for perfume in perfumes)
    avg_price = total_value / total_perfumes if total_perfumes > 0 else 0
    most_common_brand = Counter(perfume['brand'] for perfume in perfumes).most_common(1)[0][0] if perfumes else "N/A"
    
    print(f"Collection Summary:")
    print(f"Total number of perfumes: {total_perfumes}")
    print(f"Total value of collection: £{total_value:.2f}")
    print(f"Average price per perfume: £{avg_price:.2f}")
    print(f"Most common brand: {most_common_brand}")


# Widgets for the user interface
name_widget = widgets.Text(description='Name:')
brand_widget = widgets.Text(description='Brand:')
scent_widget = widgets.Dropdown(
    options=SCENT_OPTIONS,
    description='Scent:',
    disabled=False,
)
other_scent_widget = widgets.Text(description='Other Scent:', disabled=True)

def on_scent_change(change):
    if change['new'] == 'Other':
        other_scent_widget.disabled = False
    else:
        other_scent_widget.disabled = True
        other_scent_widget.value = ''

scent_widget.observe(on_scent_change, names='value')
price_widget = widgets.FloatText(description='Price:')
edit_index_widget = widgets.IntText(description='Edit Index:')
delete_index_widget = widgets.IntText(description='Delete Index:')
add_button = widgets.Button(description="Add Perfume")
edit_button = widgets.Button(description="Edit Perfume")
delete_button = widgets.Button(description="Delete Perfume")
view_button = widgets.Button(description="View Perfumes")
exit_button = widgets.Button(description="Exit")


# Attach buttons to functions
add_button.on_click(add_perfume)
edit_button.on_click(edit_perfume)
delete_button.on_click(delete_perfume)
view_button.on_click(view_perfumes)
exit_button.on_click(exit_interface)
# Update the main interface to include visualisation options
visualise_brands_button = widgets.Button(description="Visualise Brands")
visualise_scents_button = widgets.Button(description="Visualise Scents")
visualise_prices_button = widgets.Button(description="Visualise Prices")
visualise_price_vs_brand_button = widgets.Button(description="Price vs Brand")
generate_summary_button = widgets.Button(description="Generate Summary")

visualise_brands_button.on_click(lambda _: visualise_brands())
visualise_scents_button.on_click(lambda _: visualise_scents())
visualise_prices_button.on_click(lambda _: visualise_price_range())
visualise_price_vs_brand_button.on_click(lambda _: visualise_price_vs_brand())
generate_summary_button.on_click(lambda _: generate_summary())

# Display the interface
display(name_widget, brand_widget, scent_widget, other_scent_widget, price_widget, 
        add_button, edit_button, delete_button, view_button, 
        edit_index_widget, delete_index_widget, exit_button, visualise_brands_button, visualise_scents_button, 
        visualise_prices_button, visualise_price_vs_brand_button,
        generate_summary_button)
