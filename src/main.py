from src.collection_manager import CollectionManager, Perfume

def display_menu():
    print("\nCollection Manager")
    print("1. Add Perfume")
    print("2. Edit Perfume")
    print("3. Delete Perfume")
    print("4. View Perfumes")
    print("5. Exit")

def main():
    manager = CollectionManager()

    while True:
        display_menu()

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter perfume name: ")
            brand = input("Enter perfume brand: ")
            scent = input("Enter perfume scent: ")
            price = float(input("Enter perfume price: "))
            perfume = Perfume(name, brand, scent, price)
            manager.add_perfume(perfume)
            print("Perfume added successfully!")

        elif choice == '2':
            perfumes = manager.view_perfumes()
            for idx, perfume in enumerate(perfumes):
                print(f"{idx + 1}. {perfume.name} - {perfume.brand}")
            index = int(input("Choose a perfume to edit: ")) - 1
            name = input("Enter new name (or leave blank to keep current): ")
            brand = input("Enter new brand (or leave blank to keep current): ")
            scent = input("Enter new scent (or leave blank to keep current): ")
            price = input("Enter new price (or leave blank to keep current): ")
            price = float(price) if price else None
            manager.edit_perfume(index, name, brand, scent, price)
            print("Perfume updated successfully!")

        elif choice == '3':
            perfumes = manager.view_perfumes()
            for idx, perfume in enumerate(perfumes):
                print(f"{idx + 1}. {perfume.name} - {perfume.brand}")
            index = int(input("Choose a perfume to delete: ")) - 1
            manager.delete_perfume(index)
            print("Perfume deleted successfully!")

        elif choice == '4':
            perfumes = manager.view_perfumes()
            if perfumes:
                for perfume in perfumes:
                    print(f"{perfume.name} - {perfume.brand}, {perfume.scent}, ${perfume.price}")
            else:
                print("No perfumes in collection.")

        elif choice == '5':
            print("Exiting the application...")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    main()
