from typing import Any, Optional, Union


def get_any(input_dict: dict) -> Any:
    return input_dict.get('key')


res = get_any({})
print(res)


def check_optional(input_dict: dict):
    name: Optional[str] = input_dict.get('name')
    if name:
        print(name.strip())


def greeting(name: Union[str, int]) -> str:
    return 'Hello ' + str(name)


print(greeting(1))
print(greeting(''))
# print(greeting(1.2))
