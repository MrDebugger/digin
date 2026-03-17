from digin import NestedDict

# Hardcoded JSON data
data = {
    "store": {
        "books": [
            {
                "title": "Harry Potter and the Philosopher's Stone",
                "author": "J.K. Rowling",
                "price": 10.99
            },
            {
                "title": "The Lord of the Rings",
                "author": "J.R.R. Tolkien",
                "price": 15.99
            }
        ],
        "location": "New York"
    }
}

# Convert the JSON data to a NestedDict with a delimiter "."
nd = NestedDict(data, ".")

# Use the __call__ method to print the price of items
print(nd("store.books.0.price"))
# Use the __call__ method to update the price of items
nd("store.books.1.price", 16.99)

# Use the __call__ method to find if item is not available
print(nd("store.books.0.price", default="NotFound"))

# print the updated prices
print(nd("store.books.1.price"))
