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

    def get_str(self, indent=0):
        result = ''
        if indent == 0:
            result += "mindmap  root"
            result += ' ' * indent + str(self) + os.linesep
            indent += 2
        else:
            result += ' ' * indent + str(self) + os.linesep
        for child in self.children:
            result += str(child.get_str(indent + 2))
        return result

    def __str__(self):
        return self.get_shape_representation().format(self.name)

def main():
    from mindmap_leaf import MindMapLeaf
    root = MindMapComposite("The Battle at Wolf 359", "circle")

    characters = MindMapComposite("Characters", "oval")
    characters.add(MindMapLeaf("Jean-Luc Picard / Locutus", "plain"))
    characters.add(MindMapLeaf("William Riker", "plain"))
    characters.add(MindMapLeaf("Data", "plain"))
    characters.add(MindMapLeaf("Worf", "plain"))
    characters.add(MindMapLeaf("Borg Queen (implied presence)", "plain"))
    root.add(characters)

    root.display()
    print(root.get_str())

if __name__ == '__main__':
    main()