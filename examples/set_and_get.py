from digin import NestedDict
import json
import os

current_dir = os.path.dirname(__file__)

with open(os.path.join(current_dir,'data.json')) as file:
    data = json.load(file)

nested_data = NestedDict(data)


# Get the firstName of the first employee
print(nested_data.get("employees->0->firstName")) # "John"

# Get the lastName of the second employee
print(nested_data.get("employees->1->lastName")) # "Smith"

# Get the firstName of the first child of the first owner
print(nested_data.get("owners->0->children->0->firstName")) # "Cathy"

# Get the age of the second child of the second owner
print(nested_data.get("owners->1->children->1->age")) # 8

# Set the age of the first owner to 30
nested_data.set("owners->0->age", 30)
print(nested_data.get("owners->0->age")) # 30

# Set the city of the second owner's address to "Los Angeles"
nested_data.set("owners->1->address->city", "Los Angeles")
print(nested_data.get("owners->1->address->city")) # "Los Angeles"