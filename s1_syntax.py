def hello():
    var1: int = 0
    var2: str = ''
    var3: dict = {}


def greeting(name: str) -> str:
    return 'Hello ' + name


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_greeting(self) -> str:
        buf: str = 'Hello ' + self.name
        return buf


res = greeting('alex')
print(res.upper())

p: Person = Person('alex')
p1 = Person('alex')
print(p.name.upper())

p = Person(1)
print(p.name.upper())
