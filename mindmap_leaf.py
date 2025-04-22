class MindMapLeaf:
    # Step 1: Write the __init__ method
    # - Define an __init__ method that takes two parameters: name and shape.
    # - Assign these parameters to the instance variables self.name and self.shape.
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    def get_shape_representation(self):
        shapes = {
            "circle": "(({}))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{{{}}}}}",
            "bang": ")){}(("
        }
        return shapes.get(self.shape, '{}')

    def display(self, indent=0):
        print(' ' * indent + str(self))

    def __str__(self):
        return self.get_shape_representation().format(self.name)