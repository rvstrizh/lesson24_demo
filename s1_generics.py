from typing import List, Dict


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_greeting(self) -> str:
        buf: str = 'Hello ' + self.name
        return buf


def fetch_persons() -> List[Person]:
    return [Person('alex'), Person('ivan')]


def convert_dict_persons_to_list(persons: Dict[str, Person]) -> List[Person]:
    return list(persons.values())
