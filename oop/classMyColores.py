class MyColors:
    def __init__(self):
        self.red: 1
        self.green: 1
        self.blue: 1

    # It is called independent if the attribute exists or not.
    def __getattribute__(self, item):
        if item == 'rgb':
            return self.red, self.green, self.blue

    # It's calling if the attribute not found
    def __getattr__(self, item):
        if item == 'rgb':
            return self.red, self.green, self.blue
        pass

    # Assign a value to the attribute
    def __setattr__(self, key, value):
        pass

    # Delete a attribute
    def __delattr__(self, item):
        pass

    # Check class attributes
    def __dir__(self):
        pass


color = MyColors()
print(color.rgb)
