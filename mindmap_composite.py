import os

class MindMapComposite:
    # Step 1: Write the __init__ method
    # - Define an __init__ method that takes name and shape as parameters.
    # - Initialize self.name, self.shape, and an empty list self.children.

    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

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
        if indent == 0:
            print("mindmap" + os.linesep + "root", end="")
            print(' ' * indent + str(self))
            indent += 2
        else:
            print(' ' * indent + str(self))
        for child in self.children:
            child.display(indent + 2)

    def __str__(self):
        return self.get_shape_representation().format(self.name)