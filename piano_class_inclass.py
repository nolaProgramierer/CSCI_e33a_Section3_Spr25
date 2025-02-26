

class Piano():
    
    inventory = [] # Stores all instances of the class
    
    def __init__(self, brand, price, keys=88, pedals=3, features=None):
        self.brand = brand
        self.price = price
        self.keys = keys
        self.pedals = pedals

        if features is None:
            self.features = []
        elif isinstance(features, list):
            self.features = features
        else: raise TypeError('features must be a list')

        Piano.inventory.append(self) # Append instance to inventory on intialization

    # Class instance methods (methods on class instances)
    # ---------------------------------------------------
    # Print detail of a piano class instance
    def print_piano_details(self):
        print(f"{self.brand} - ${self.price:,.0f}")
        print(f"Features: {' ,'.join(self.features)}")

    # Convert the price of a piano to euros 
    def convert_price_to_euros(self, rate):
        return (self.price * rate)
    
    # Add a feature to a piano instance
    def add_feature(self, feature):
        if feature in self.features:
            print(f"This {feature} already exists for this {self.brand}")
        else:
            self.features.append(feature)
            print(f"{feature} added to this piano's features")

    # Remove a feature of a piano instance
    def remove_features(self, feature):
        if feature in self.features:
            self.features.remove(feature)
            print(f"{feature} has been removed from {self.brand}")
        else:
            print(f"This {self.brand} does not have this feature to remove.")

    # Update the price of a piano instance
    def update_price(self, new_price):
        self.price = new_price
        print(f"The price of {self.brand} has been updated to ${self.price:,.0f}")


    # Class methods, methods for the entire class
    # -------------------------------------------
    # Return a list of all class instances
    @classmethod
    def get_inventory(cls):
        return cls.inventory
    
    # Find the most expensive piano of the class
    @classmethod
    def get_most_expensive_piano(cls):
        if not cls.inventory:
            print("No pianos in inventory.")
            return None
        return max(cls.inventory, key=lambda piano: piano.price, default=None)

    # Remove a piano from the class   
    @classmethod
    def remove_piano(cls, piano):
        if piano in cls.inventory:
            cls.inventory.remove(piano)
            print(f"{piano.brand} piano removed from inventory.")
        else:
            print(f"Piano not found in inventory.")

    # Find a piano by a feature
    @classmethod
    def find_piano_by_feature(cls, feature):
        return [piano for piano in cls.inventory if feature in piano.features]

    
# Subclasses of the Piano class, inheriting methods and variables
# ---------------------------------------------------------------
class GrandPiano(Piano):
    inventory = [] # Separate inventory for grand piano

    def __init__(self, brand, price, size, keys=88, features=None):
        # Calls the __init__() method of the super class
        super().__init__(brand, price, keys=keys, features=features)
        self.size = size
        GrandPiano.inventory.append(self)

    #Overriding a method of the super class (Polymorphism)
    def print_piano_details(self):
        super().print_piano_details()
        print(f"Price: {self.price} - Size: {self.size}")

    def play_sound(self):
        print("Playing a beautiful, rich, singing grand piano sound")


class UprightPiano(Piano):
    inventory = [] # Separate inventory for uprightdpiano

    def __init__(self, brand, price, height, features=None):
        super().__init__(brand, price, features=features)
        self.height = height
        UprightPiano.inventory.append(self)

    def play_sound(self):
        print("Playing a bright, somewhat thin, but pleasing upright sound!")


# --------------------------------------------------------
# Instances of the Piano class and its subclasses
# Regular Pianos
p1 = Piano("Yamaha", 5000, features=["Silent Mode"])
p2 = Piano("Steinway", 12000, features=["Concert Grade"])
p3 = Piano("Kawai", 7000, features=["Hybrid Action"])

# Grand Pianos
g1 = GrandPiano("Bösendorfer", 150000, "9ft", keys=97, features=["Handcrafted", "Limited Edition", "Concert Grade"])
g2 = GrandPiano("Steinway", 90000, "7ft", features=["Concert Hall Quality"])
g3 = GrandPiano("Yamaha", 45000, "6ft", features=["Player System"])

# Upright Pianos
u1 = UprightPiano("Baldwin", 3500, "48 inches", features=["Silent Mode"])
u2 = UprightPiano("Kawai", 4000, "50 inches", features=["Practice Pedal"])
u3 = UprightPiano("Steinway", 8500, "52 inches", features=["Handcrafted Wood"])


# (The extra 'print()' statements are only for more readable terminal output)
print()
print("1)")
# Show the details of the Steinway grand piano


print("2)")
# Show the details of the Steinway grand piano


print("3)")
# Play the Yamaha grand piano


print("4)")
# Play the Badlwin upright


print("5)")
# Convert Steinway grand price to euros
# (notice that the method was defined in the super class)


print("6)")
# Add a feature to the Kawai upright


print("7)")
# Update price for Baldwin upright


print("8)")
# Return all pianos in inventory


print("9)")
# Return the most expensive piano


print("10)")
# Return all grand pianos
# (notice that a method defined in the superclass is available in the subclass)


print("11)")
# Find pianos that are Concert Grade












