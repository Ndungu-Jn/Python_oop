# Think of class as the architectural blueprint for a house.
# it defines what the house will entail but you cannot live in it.

# Object on the other hand is the actual physical house.
# we can use the same blueprint to build different houses


# 1. The CLASS (The Blueprint)
# This defines what every house will have, but doesn't create a real house yet.
class House:
    def __init__(self, color, number_of_rooms):
        self.color = color                  # Attribute template
        self.number_of_rooms = number_of_rooms  # Attribute template

    # A behavior/method that all houses can perform
    def display_details(self):
        print(
            f"This house is {self.color} and has {self.number_of_rooms} rooms.")


# 2. The OBJECTS (The Physical Houses)
# We use the same blueprint to build two completely separate houses in memory.
house1 = House(color="Blue", number_of_rooms=4)
house2 = House(color="Yellow", number_of_rooms=6)

# 3. Printing the results to see them in action
print("--- House 1 Details ---")
house1.display_details()

print("\n--- House 2 Details ---")
house2.display_details()
