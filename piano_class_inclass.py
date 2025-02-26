class Piano():
    
    inventory = [] # Stores all instances of the class
    
    def __init__(self, brand, price, keys=88, pedals=3, features=None):
        self.brand = brand
        self.price = price
        self.keys = keys
        self.pedals = pedals
        self.features = features if features is not None else []
        Piano.inventory.append(self) # Append instance to inventory on intialization

    # Class instance methods (methods on class instances)
    # ---------------------------------------------------
    # Print detail of a piano class instance
    

    # Convert the price of a piano to euros 
    
    
    # Add a feature to a piano instance
    

    # Remove a feature of a piano instance
    

    # Update the price of a piano instance
    


    # Class methods, methods for the entire class
    # -------------------------------------------
    # Return a list of all class instances
    
    
    
    # Find the most expensive piano of the class
   
    

    # Remove a piano from the class   
    
    

    # Find a piano by a feature
    
    
       
# Subclasses of the Piano class, inheriting methods and variables
# ---------------------------------------------------------------
class GrandPiano(Piano):
    inventory = [] # Separate inventory for grand piano

    def __init__(self, brand, price, size, keys=88, features=None):
        # Calls the __init__() method of the super class
        super().__init__(brand, price, keys=keys, features=features)
        self.size = size
        GrandPiano.inventory.append(self)


class UprightPiano(Piano):
    inventory = [] # Separate inventory for uprightdpiano

    def __init__(self, brand, price, height, features=None):
        super().__init__(brand, price, features=features)
        self.height = height
        UprightPiano.inventory.append(self)

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





