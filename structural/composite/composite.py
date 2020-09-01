from abc import ABC, abstractmethod


class Component(ABC):

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    def is_composite(self):
        return False

    def add(self, component):
        raise NotImplementedError()

    def remove(self, component):
        raise NotImplementedError()

    @abstractmethod
    def operation(self):
        raise NotImplementedError()


class Leaf(Component):
    def operation(self):
        return 'Leaf'


class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def is_composite(self):
        return True

    def operation(self) -> str:
        results = []

        for child in self._children:
            results.append(child.operation())
        return f"Branch({'<*>'.join(results)})"


if __name__ == '__main__':
    leaf = Leaf()
    print(leaf.operation())

    tree = Composite()

    branch = Composite()
    branch.add(Leaf())
    branch.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())
    branch2.add(Leaf())
    branch2.add(Leaf())

    tree.add(branch)
    tree.add(branch2)

    print(tree.operation())
