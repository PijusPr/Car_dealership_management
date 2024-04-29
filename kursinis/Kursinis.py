class Car:
    def __init__(self,brand='',model='',year=0,color='',mileage=0,price=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.price = price

    def add_vehicle(self):
        try:
            self.brand = input('Enter vehicle brand: ')
            self.model = input('Enter vehicle model: ')
            self.year = int(input('Enter vehicle year: '))
            self.color = input('Enter vehicle color: ')
            self.mileage = int(input('Enter vehicle mileage: '))
            self.price = int(input('Enter vehicle price: '))
            return True
        except ValueError:
            print('Please enter valid numerical values for year, mileage and price.')
            return False

    def __str__(self):
        return '\t'.join(str(x) for x in [self.brand, self.model, self.year, self.color, self.mileage, self.price])

class ElectricCar(Car):
    def __init__(self, range = 0):
        super().__init__()  
        self.range = range

    def add_vehicle(self):
        if super().add_vehicle():  
            try:
                self.range = int(input('Enter range in miles: '))
                return True
            except ValueError:
                print('Please enter valid numerical values for range.')
                return False

    def __str__(self):
        car_details = super().__str__()
        return f"{car_details}\t{self.range}"

class Inventory:
    def __init__(self):
        self.vehicles = []
        self.load_inventory() 

    def load_inventory(self):
        try:
            with open('vehicle_inventory.txt', 'r') as file:
                next(file) 
                for line in file:
                    data = line.strip().split('\t')
                    if len(data) >= 6:
                        if len(data) == 6:
                            brand, model, year, color, mileage, price = data
                            vehicle = Car()
                        else: 
                            brand, model, year, color, mileage, price, range = data
                            vehicle = ElectricCar(int(range))
                        vehicle.brand = brand
                        vehicle.model = model
                        vehicle.year = int(year)
                        vehicle.color = color
                        vehicle.mileage = int(mileage)
                        vehicle.price = int(price)
                        self.vehicles.append(vehicle)
                    else:
                        print(f"Ignoring incomplete data line: {data}")
        except FileNotFoundError:
            print('Inventory file not found. Starting with empty inventory.')

    def save_inventory(self):
        try:
            with open('vehicle_inventory.txt', 'w') as file:
                file.write('\t'.join(['Brand', 'Model', 'Year', 'Color', 'Mileage', 'Price', 'Range']) + '\n')
                for vehicle in self.vehicles:
                    if isinstance(vehicle, ElectricCar):  
                        file.write(f"{vehicle}\n")
                    else:
                        file.write(f"{vehicle}\t\n")
                print('Inventory saved successfully.')
        except IOError:
            print('Error saving inventory.')

    def add_vehicle(self):
        vehicle_type = input('Enter vehicle type (regular/electric): ').lower()
        if vehicle_type == 'electric':
            vehicle = ElectricCar()
        else:
            vehicle = Car()
        if vehicle.add_vehicle():
            self.vehicles.append(vehicle)
            print('Vehicle added successfully.')
            self.save_inventory()  

    def view_inventory(self):
        if not self.vehicles:
            print('Inventory is empty.')
        else:
            print('\t'.join(['', 'Brand', 'Model', 'Year', 'Color', 'Mileage', 'Price', 'Range']))
            for idx, vehicle in enumerate(self.vehicles, start=1):
                print(f"{idx}\t{vehicle}")

    def delete_vehicle(self):
        self.view_inventory()
        if not self.vehicles:
            return
        try:
            item = int(input('Enter vehicle number to be removed: '))
            if 1 <= item <= len(self.vehicles):
                del self.vehicles[item - 1]
                print('Vehicle removed successfully.')
                self.save_inventory() 
            else:
                print('Invalid number.')
        except ValueError:
            print('Please enter a valid number.')
    
    def search_by_brand(self):
        search_term = input('Enter the brand of the vehicle to search: ').lower()
        found_vehicles = [vehicle for vehicle in self.vehicles if vehicle.brand.lower() == search_term]
        if found_vehicles:
            print('\t'.join(['', 'Brand', 'Model', 'Year', 'Color', 'Mileage', 'Price', 'Range']))
            for idx, vehicle in enumerate(found_vehicles, start=1):
                print(f"{idx}\t{vehicle}")
        else:
            print('No vehicles found with the brand:', search_term)
       
    def sell_vehicle(self):
        self.view_inventory()
        if not self.vehicles:
            return
        try:
            item = int(input('Enter vehicle number to be sold: '))
            if 1 <= item <= len(self.vehicles):
                profit = 0.15 * self.vehicles[item - 1].price
                sold_vehicle = self.vehicles.pop(item - 1)
                print(f"Vehicle {sold_vehicle.brand} {sold_vehicle.model} sold successfully.")
                self.save_inventory()
                total_profit = 0.0
                try:
                    with open('profits.txt', 'r') as profit_file:
                        total_profit = float(profit_file.readline().strip().split(': ')[1])
                except (FileNotFoundError, IndexError):
                    total_profit = 0.0
                total_profit += profit
                with open('profits.txt', 'w') as profit_file:
                    profit_file.write(f"Total Profit: {total_profit}\n")
                print(f"Profit of {profit} has been added to the total profit.")
            else:
                print('Invalid number.')
        except ValueError:
            print('Please enter a valid number.')

inventory = Inventory()

while True:
    print('#1 Add Vehicle to Inventory')
    print('#2 Delete Vehicle from Inventory')
    print('#3 View Current Inventory')
    print('#4 Search inventory by car brand')
    print('#5 Sell a Vehicle')
    print('#6 Quit')
    user_input = input('Please choose from one of the above options: ')
    if user_input == "1":
        inventory.add_vehicle()
    elif user_input == '2':
        inventory.delete_vehicle()
    elif user_input == '3':
        inventory.view_inventory()
    elif user_input == '4':
        inventory.search_by_brand()
    elif user_input == '5':
        inventory.sell_vehicle()
    elif user_input == '6':
        print('Program closing')
        break
    else:
        print('Invalid input')