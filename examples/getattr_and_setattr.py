from digin import NestedDict

# Hardcoded JSON data
data = {
    "employees": {
        "john": {
            "age": 30,
            "position": "manager"
        },
        "susan": {
            "age": 25,
            "position": "developer"
        }
    }
}

# Convert the JSON data to a NestedDict
nd = NestedDict(data)

# Use the __getattr__ method to access nested data
print(nd.employees.john.age) # Outputs: 30

# Use the __setattr__ method to modify nested data
nd.employees.john.age = 31
print(nd.employees.john.age) # Outputs: 31

# save the nested dict to json 
print(nd)
