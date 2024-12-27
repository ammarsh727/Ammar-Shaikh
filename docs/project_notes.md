# Collection Manager Project Notes

## Project Overview
The **Collection Manager** is an application designed to help users manage their collection of perfumes. The application allows users to add, remove, edit, and view perfumes in their perfume collection. It offers a user-friendly interface for interacting with the data and organises perfumes based on various attributes such as name, brand, scent, size and price.

**Objective:**  
The goal of this project is to develop a fully functional collection manager that can perform CRUD (Create, Read, Update, Delete) operations on a collection of perfumes. The system will store data in a JSON file format, making it easy for users to manage their collection and retain data between sessions. In addition to this, it is important that the data is able to be visualised for the user.

## Objective and Purpose
The primary purpose of this application is to:
- **Track a collection** of perfumes.
- **Store perfume information** in a simple, structured format.
- **Allow the user** to add new perfumes, edit existing ones, and delete those they no longer wish to keep.
- **Visualise the collection data** to provide insights such as perfume distribution by brand, price range, scent categories, etc.

This application is ideal for people who collect perfumes, such as fragrance enthusiasts, as well as people looking for a system to manage their personal inventory.

**User Needs:**  
- Simple and intuitive interface for managing perfume collection.
- Secure and reliable storage of perfume details.
- Functionality to filter, search, and categorise perfumes.
- Visualisation tools to gain insights from the data (e.g., pie charts, bar graphs, etc.).

## Key Features
The application will provide the following features:

1. **Add Perfumes:**  
   - The user can add new perfumes by entering information such as the name, brand, scent, price, and any other relevant details.
   - Data is validated before being added to the collection.
  
2. **View Perfumes:**  
   - The user can view a list of all perfumes in their collection, with each perfume displayed by its details (e.g., name, brand, scent).
   - The collection can be displayed in sorted or filtered formats (e.g., by name, by brand).

3. **Edit Perfumes:**  
   - The user can edit the details of a perfume in the collection, such as its name, brand, or price.
  
4. **Delete Perfumes:**  
   - The user can remove a perfume from their collection if it is no longer needed or desired.

5.- **Perfume Notes:** In future iterations, the application will display the perfume's notes (e.g., top, middle, and base notes) for each perfume in the collection.
  
6. **Data Persistence:**  
   - Perfume data will be saved in a **JSON file** to ensure the collection is retained between sessions. The JSON file will be loaded when the program starts, and any changes will be saved back to the file.
  
7. **Data Visualisation:**
   - Visualise the collection using **graphs and charts** (e.g., price distribution, brand frequency).
   - Generate **Mermaid diagrams** directly in the Markdown file or use **Matplotlib** for Python-based visualisations within the app.

## User Stories
User stories describe the features and functionalities of the application from the perspective of the users. Each story captures a specific user need and the associated goals.

### User Story 1: Add a Perfume
- **As a** perfume collector,  
- **I want to** add a new perfume to my collection,  
- **So that** I can keep track of it along with my other perfumes.

### User Story 2: Edit a Perfume
- **As a** perfume collector,  
- **I want to** edit the details of a perfume (e.g., change the price or scent),  
- **So that** I can keep my collection up-to-date.

### User Story 3: Delete a Perfume
- **As a** perfume collector,  
- **I want to** remove a perfume from my collection,  
- **So that** I can declutter and remove perfumes I no longer want.

### User Story 4: View Collection
- **As a** perfume collector,  
- **I want to** see all my perfumes in a list,
- **So that** I can view the entire collection and find a perfume easily.

### User Story 5: Save and Load Data
- **As a** user,  
- **I want the data** to be saved in a file,  
- **So that** I can persist my collection even when I close and reopen the application.

### User Story 6: Visualise Collection Data
- **As a** perfume collector,  
- **I want to** visualise my collection's data,  
- **So that** I can see insights like the number of perfumes per brand or the price distribution.

  ## User Personas
### Persona 1: Jane, the Enthusiast
- **Age:** 30  
- **Occupation:** Marketing Manager  
- **Tech-savviness:** Average  
- **Needs:** Jane has a growing perfume collection. She needs a simple application that allows her to add, edit, and remove perfumes easily. She is also interested in visualizing the price distribution and the number of perfumes per brand.

### Persona 2: Mark, the Gift Giver
- **Age:** 40  
- **Occupation:** Business Executive  
- **Tech-savviness:** Low  
- **Needs:** Mark occasionally buys perfumes as gifts and needs a way to keep track of which perfumes he has bought for friends and family. He prefers something very easy to use but also appreciates a simple visualisation of how much his collection is worth.

## Technologies Used
### 1. **Python**
   - Python will be used for the core logic, including the ability to add, edit, delete, and view perfumes. Python will also be used to generate visualisations.

### 2. **JSON**
   - Perfume data will be stored in a JSON file (`perfumes.json`). This allows easy storage and retrieval of data.

### 3. **Git and GitHub**
   - Git will be used for version control, and GitHub will be used for hosting the repository and collaboration.

### 4. **Mermaid (for Markdown Diagrams)**
   - Mermaid will be used for simple flowcharts, Gantt charts, or data flow diagrams directly in Markdown files, providing users with a visual overview of the project.

### 5. **Matplotlib/Seaborn (for Python Visualisations)**
   - These Python libraries will be used to generate advanced visualisations like pie charts, bar graphs, and histograms to represent perfume distribution, price ranges, and brand frequency.

### 6. **Unit Testing (unittest)**
   - The `unittest` framework will be used for testing the core functionalities of the application.

## Data Structure
The perfume data will be stored as a list of dictionaries in JSON format, each dictionary representing a perfume. Each perfume object will contain attributes such as:
- **name**
- **brand**
- **scent**
- **price**

Example:

```json
[
  {
    "name": "Chanel No. 5",
    "brand": "Chanel",
    "scent": "Floral",
    "price": 120.00
  },
  {
    "name": "Dior Sauvage",
    "brand": "Dior",
    "scent": "Woody, Spicy",
    "price": 85.00
  }
]

### Class Diagram Overview

To better understand the structure of the **Collection Manager**, I created a class diagram to visualise the relationships between the classes. This diagram highlights the core components of the application and their interactions. The main classes include `Perfume`, `CollectionManager`, and `Visualiser`, each representing a key aspect of the application's functionality.

The diagram outlines:
- **Attributes** (e.g., name, brand, scent, price) for the `Perfume` class.
- **Methods** (e.g., add_perfume, edit_perfume, delete_perfume) for the `CollectionManager`.
- The relationship between `Perfume` and `Visualiser` to show how data is analysed and presented.

This diagram aids in the development process by ensuring clarity and alignment with the object-oriented design principles of **abstraction**, **encapsulation**, and **inheritance**.

## Class Diagram

Below is the class diagram for the Perfume Collection Manager project:

![Class Diagram](docs/Perfume_Collection_Class_Diagram.png)

