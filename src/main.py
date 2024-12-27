import ipywidgets as widgets
from IPython.display import display
from src.collection_manager import CollectionManager, Perfume

# Create global CollectionManager instance
manager = CollectionManager()

# Function to display perfumes
def display_perfumes():
    perfumes = manager.view_perfumes()
    if perfumes:
        for idx, perfume in enumerate(perfumes):
            print(f"{idx + 1}. {perfume.name} - {perfume.brand}, {perfume.scent}, £{perfume.price}")
    else:
        print("No perfumes in collection.")

# Functions to handle actions
def add_perfume(_):
    name = name_widget.value
    brand = brand_widget.value
    scent = scent_widget.value
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

    for idx, perfume in enumerate(perfumes):
        print(f"{idx + 1}. {perfume.name} - {perfume.brand}")

    index = int(edit_index_widget.value) - 1
    name = name_widget.value or None
    brand = brand_widget.value or None
    scent = scent_widget.value or None
    price = price_widget.value or None
    manager.edit_perfume(index, name, brand, scent, price)
    print("Perfume updated successfully!")
    display_perfumes()

def delete_perfume(_):
    perfumes = manager.view_perfumes()
    if not perfumes:
        print("No perfumes to delete.")
        return

    for idx, perfume in enumerate(perfumes):
        print(f"{idx + 1}. {perfume.name} - {perfume.brand}")

    index = int(delete_index_widget.value) - 1
    manager.delete_perfume(index)
    print("Perfume deleted successfully!")
    display_perfumes()

def view_perfumes(_):
    display_perfumes()

# Widgets for the user interface
name_widget = widgets.Text(description='Name:')
brand_widget = widgets.Text(description='Brand:')
scent_widget = widgets.Text(description='Scent:')
price_widget = widgets.FloatText(description='Price:')
edit_index_widget = widgets.IntText(description='Edit Index:')
delete_index_widget = widgets.IntText(description='Delete Index:')
add_button = widgets.Button(description="Add Perfume")
edit_button = widgets.Button(description="Edit Perfume")
delete_button = widgets.Button(description="Delete Perfume")
view_button = widgets.Button(description="View Perfumes")

# Attach buttons to functions
add_button.on_click(add_perfume)
edit_button.on_click(edit_perfume)
delete_button.on_click(delete_perfume)
view_button.on_click(view_perfumes)

# Display the interface
display(name_widget, brand_widget, scent_widget, price_widget, add_button, edit_button, delete_button, view_button, edit_index_widget, delete_index_widget)

