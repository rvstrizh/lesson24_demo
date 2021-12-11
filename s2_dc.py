# код ниже получает все типы лицензий, которые используются в github репозиториях
# нужно дополнить код так, чтобы в результате оказались только лицензии репозиториев с топиком python
from typing import List, Optional
from dataclasses import dataclass

import requests


def fetch_repos(org: str) -> dict:
    resp = requests.get(f"https://api.github.com/orgs/{org}/repos")
    return resp.json()


@dataclass
class License:
    key: str
    name: str


@dataclass
class Repo:
    id: int
    name: str
    full_name: str
    license: Optional[License]
    topics: List[str]


def fetch_licenses() -> List[str]:
    repos = fetch_repos("python")
    res = set()
    for item in repos:
        if item["license"]:
            license_obj = License(
                key=item["license"]["key"],
                name=item["license"]["name"]
            )
        else:
            license_obj = None

        repo = Repo(
            id=item["id"],
            name=item["name"],
            full_name=item["full_name"],
            license=license_obj,
            topics=item["topics"]
        )
        if repo.license:
            if "python" in repo.topics:
                res.add(repo.license.key)
    return list(res)


print(fetch_licenses())
