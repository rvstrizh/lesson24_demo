import datetime
from dataclasses import dataclass
from typing import List, Optional, Dict

import marshmallow_dataclass

vk_resp = {
    "response": {
        "items": [
            {
                "first_name": "Akim",
                "id": 267459072,
                "last_name": "Volkov",
                "city": {
                    "id": 2,
                    "title": "Saint Petersburg"
                },
                "bdate": None
            }, {
                "first_name": "Akshin",
                "id": 2453384,
                "last_name": "Dzhangirov",
                "city": None,
                "bdate": "20.05"
            },
            {
                "first_name": "Aleksandra",
                "id": 1894768,
                "last_name": "Sokolovskaya",
                "city": {
                    "id": 1,
                    "title": "Moscow"
                },
                "bdate": "10.05.1990"
            }]
    }
}


@dataclass
class City:
    id: int
    title: str


@dataclass
class ResponseItem:
    id: int
    first_name: str
    last_name: str
    bdate: Optional[str]
    city: Optional[City]


@dataclass
class Response:
    items: List[ResponseItem]


@dataclass
class VkResponse:
    response: Response


@dataclass
class CityInfo:
    city: City
    count: int = 0
    age: int = 0


def calc_average_age(vk_response: VkResponse) -> Dict[int, CityInfo]:
    cities: Dict[int, CityInfo] = {}
    for item in vk_response.response.items:
        if not item.city:
            continue
        city_id = item.city.id

        if city_id not in cities:
            cities[city_id] = CityInfo(item.city)
        city_info = cities[city_id]

        if not item.bdate:
            continue
        bdate_split: List[str] = item.bdate.split('.')
        if len(bdate_split) != 3:
            continue
        d, m, y = int(bdate_split[0]), int(bdate_split[1]), int(bdate_split[2])

        td = datetime.date.today() - datetime.date(y, m, d)
        city_info.count += 1
        city_info.age += td.days // 365

    return cities


VkResponseSchema = marshmallow_dataclass.class_schema(VkResponse)
data: VkResponse = VkResponseSchema().load(vk_resp)
print(data)

calc_average_age(data)
