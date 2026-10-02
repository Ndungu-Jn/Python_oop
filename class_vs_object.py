# Think of class as the architectural blueprint for a house.
# it defines what the house will entail but you cannot live in it.

# Object on the other hand is the actual physical house.
# we can use the same blueprint to build different houses


# 1. This is the CLASS (The Blueprint)
class Dog:
    def __init__(self, name, breed):
        self.name = name    # Attribute template
        self.breed = breed  # Attribute template


# 2. These are the OBJECTS (The Real Instances)
dog1 = Dog("Tommy", "Golden Retriever")  # Allocates memory for Tommy
dog2 = Dog("Bella", "Poodle")
