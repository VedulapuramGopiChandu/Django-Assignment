class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Define the iterator method to yield length and width as dictionaries
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
rectangle = Rectangle(length=5, width=10)

# Iterating over the rectangle instance
for dimension in rectangle:
    print(dimension)
