from digin import NestedList

# Hardcoded JSON data
data = [
    {
        "name": "John Smith",
        "age": 30,
        "email": "john.smith@example.com",
        "hobbies": [
            "reading",
            "running",
                {
                "name": "programming",
                "languages": [
                    "Python",
                    "JavaScript",
                    "C++"
                ]
            }
        ]
    },
    {
        "name": "Jane Doe",
        "age": 25,
        "email": "jane.doe@example.com",
        "hobbies": [
            "cooking",
            "traveling",
            [
                "photography",
                "hiking"
            ]
        ]
    }
]


# Convert the JSON data to a NestedDict with a delimiter "."
nd = NestedList(data, ".")

# Use the __getitem__ method to access nested data
print(nd["1.hobbies.2.1"]) # Outputs: "hiking"

# Use the __setitem__ method to modify nested data
nd["0.hobbies.2.languages.1"] = "Java"
print(nd["0.hobbies.2.languages.1"]) # Outputs: "Java"

# print the nested dict
print(nd)
