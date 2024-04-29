import unittest
from Kursinis import Inventory, Car, ElectricCar
import os

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import io

class TestInventory(unittest.TestCase):
    def setUp(self):
        
        self.inventory = Inventory()
        
        self.inventory.vehicles = []

    def test_load_inventory_file_not_found(self):
   
        with patch('builtins.open', side_effect=FileNotFoundError):
            self.inventory.load_inventory()
    
        self.assertEqual(len(self.inventory.vehicles), 0)

    def test_save_inventory(self):
        
        car1 = Car()
        car1.brand = 'Toyota'
        car1.model = 'Camry'
        car1.year = 2019
        car1.color = 'Red'
        car1.mileage = 50000
        car1.price = 25000
        self.inventory.vehicles.append(car1)

        electric_car = ElectricCar()
        electric_car.brand = 'Tesla'
        electric_car.model = 'Model 3'
        electric_car.year = 2020
        electric_car.color = 'Blue'
        electric_car.mileage = 20000
        electric_car.price = 45000
        electric_car.range = 300
        self.inventory.vehicles.append(electric_car)

       
        self.inventory.save_inventory()

       
        self.assertTrue(os.path.exists('vehicle_inventory.txt'))
        with open('vehicle_inventory.txt', 'r') as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 3) 
            self.assertIn('Toyota\tCamry\t2019\tRed\t50000\t25000\t\n', lines)
            self.assertIn('Tesla\tModel 3\t2020\tBlue\t20000\t45000\t300\n', lines)

        
        os.remove('vehicle_inventory.txt')

    def test_add_vehicle(self):
        
        with patch('builtins.input', side_effect=['regular', 'Toyota', 'Camry', '2019', 'Red', '50000', '25000']):
            self.inventory.add_vehicle()
        self.assertEqual(len(self.inventory.vehicles), 1)
        self.assertIsInstance(self.inventory.vehicles[0], Car)

        
        with patch('builtins.input', side_effect=['electric', 'Tesla', 'Model 3', '2020', 'Blue', '20000', '45000', '300']):
            self.inventory.add_vehicle()
        self.assertEqual(len(self.inventory.vehicles), 2)
        self.assertIsInstance(self.inventory.vehicles[1], ElectricCar)

    def test_delete_vehicle(self):
       
        car1 = Car()
        car1.brand = 'Toyota'
        car1.model = 'Camry'
        car1.year = 2019
        car1.color = 'Red'
        car1.mileage = 50000
        car1.price = 25000
        self.inventory.vehicles.append(car1)

        electric_car = ElectricCar()
        electric_car.brand = 'Tesla'
        electric_car.model = 'Model 3'
        electric_car.year = 2020
        electric_car.color = 'Blue'
        electric_car.mileage = 20000
        electric_car.price = 45000
        electric_car.range = 300
        self.inventory.vehicles.append(electric_car)

       
        with patch('builtins.input', return_value='1'):  
            self.inventory.delete_vehicle()
        self.assertEqual(len(self.inventory.vehicles), 1)
        self.assertEqual(self.inventory.vehicles[0].brand, 'Tesla')

    def search_by_brand(self):
        search_term = input('Enter the brand of the vehicle to search: ').lower()
        found_vehicles = [vehicle for vehicle in self.vehicles if vehicle.brand.lower() == search_term]
        if found_vehicles:
            print('\t1\tBrand\tModel\tYear\tColor\tMileage\tPrice\tRange')
            for idx, vehicle in enumerate(found_vehicles, start=1):
                print(f"{idx}\t{vehicle}")
        else:
            print('No vehicles found with the brand:', search_term)

    def test_sell_vehicle(self):
        
        car1 = Car()
        car1.brand = 'Toyota'
        car1.model = 'Camry'
        car1.year = 2019
        car1.color = 'Red'
        car1.mileage = 50000
        car1.price = 25000
        self.inventory.vehicles.append(car1)

        
        with patch('builtins.input', return_value='1'):
            with patch('builtins.print') as mock_print:
                self.inventory.sell_vehicle()

      
        self.assertEqual(len(self.inventory.vehicles), 0)

       
        self.assertTrue(os.path.exists('profits.txt'))
        with open('profits.txt', 'r') as profit_file:
            profit_data = profit_file.read()
            self.assertIn('Total Profit:', profit_data)
            
            self.assertIn('3750', profit_data)  

if __name__ == '__main__':
    unittest.main()