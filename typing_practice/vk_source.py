import datetime

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


def calc_average_age(data):
    items = data["response"]["items"]
    cities = {}
    for item in items:
        try:
            city_id = item["city"]["id"]
        except (KeyError, TypeError):
            continue
        if city_id not in cities:
            cities[city_id] = {
                "title": item["city"]["title"],
                "count": 0,
                "age": 0
            }
        city_info = cities[city_id]
        try:
            d, m, y = item["bdate"].split('.')
        except (ValueError, AttributeError):
            continue

        d, m, y = int(d), int(m), int(y)
        td = datetime.date.today() - datetime.date(y, m, d)
        city_info["count"] += 1
        city_info["age"] += td.days // 365

    for v in cities.values():
        try:
            print(v["title"], v["age"] / v["count"])
        except ZeroDivisionError:
            continue


calc_average_age(vk_resp)
