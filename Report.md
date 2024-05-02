# Car_dealership_management
## Introduction

The goal of this coursework is to develop a program that provides easy car dealership management. The application allows to add, delete, view, search and sell vehicles. This program utilizes object-oriented programming principles and design patterns to provide an efficient solution.

## How to Run the Program

To run the program, simply run the Python script (<strong>Kursinis.py</strong>). Ensure that Python is installed on your system.

## How to Use the Program

When program starts running, the users are presented with a menu of options:
- <strong>Add Vehicle to Inventory</strong>: Allows users to add a new vehicle. You need to choose whether the car is regular or electric and enter the brand, model, production year, color, mileage, price and also range if it is an electric vehicle. 
- <strong>Delete Vehicle from Inventory</strong>: Shows a numbered list of vehicles and enables users to remove a vehicle by choosing a corresponding number.
- <strong>View Current Inventory</strong>: Displays the current list of vehicles.
- <strong>Search Inventory by Car Brand</strong>: Allows users to search for vehicles by brand.
- <strong>Sell a Vehicle</strong>: Makes a sale of a selected vehicle and calculates profit.
- <strong>Quit</strong>: Exits the program.

# Body/Analysis

The program is implemented using object-oriented programming (OOP) principles: encapsulation, inheritance, and polymorphism. Design patterns: Factory method and singleton.

## OOP Pillars Used and Implementation

1. **Encapsulation**: Data and methods are encapsulated within classes, ensuring data integrity and preventing direct access to class attributes from outside the class. For example, the <strong>Car</strong> and <strong>ElectricCar</strong> classes encapsulate vehicle attributes such as brand, model, year, etc., and provide methods to interact with them (<strong>add_vehicle</strong>, <strong>__str__</strong> etc.).

2. **Inheritance**: Inheritance is used to create a hierarchy of classes where child classes inherit attributes and methods from parent classes. The <strong>ElectricCar</strong> class inherits from the <strong>Car</strong> class, allowing it to reuse common functionality while extending it with additional attributes and methods specific to electric vehicle (range attribute in specific).

3. **Polymorphism**: Polymorphism allows objects of different classes to be treated as objects of a common superclass. For instance, both <strong>Car</strong> and <strong>ElectricCar</strong> objects can be stored and manipulated within the <strong>Inventory</strong> class, enabling uniform operations on different types of vehicles.

## Design Patterns

1. **Factory Method**: The <strong>add_vehicle</strong> method in the <strong>Inventory</strong> class acts as a factory method that dynamically creates instances of <strong>Car</strong> or <strong>ElectricCar</strong> based on user input. This promotes flexibility and extensibility by allowing the addition of new vehicle types without modifying existing code.

2. **Singleton**: The <strong>Inventory</strong> class utilizes the Singleton pattern to ensure that only one instance of the inventory exists throughout the program's execution. This ensures centralized access to the inventory data and prevents inconsistencies due to multiple instances.

## Results

- Implemented a robust vehicle inventory management system.
- Successfully utilized OOP principles to enhance code readability, maintainability, and scalability.
- Faced challenges in making of the last part of the program where I added user input, it was challenging to implement the OOP pillars.  

# Conclusions

This coursework has achieved a functional and efficient vehicle inventory management system using object-oriented programming principles and design patterns. The program demonstrates the effectiveness of OOP in creating modular, reusable, and maintainable software solutions. Future prospects are that it is always easy to add another function in the inventory class due to the design of the code. The code could benefit from a better user interface.
