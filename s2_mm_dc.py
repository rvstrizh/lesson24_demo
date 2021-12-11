from typing import List, Optional
from dataclasses import dataclass

import marshmallow
import marshmallow_dataclass
import requests


def fetch_repos(org: str) -> dict:
    resp = requests.get(f"https://api.github.com/orgs/{org}/repos")
    return resp.json()


@dataclass
class License:
    key: str
    name: str

    class Meta:
        unknown = marshmallow.EXCLUDE


@dataclass
class Repo:
    id: int
    name: str
    full_name: str
    license: Optional[License]
    topics: List[str]

    class Meta:
        unknown = marshmallow.EXCLUDE


RepoSchema = marshmallow_dataclass.class_schema(Repo)


def fetch_licenses() -> List[str]:
    repos = fetch_repos("python")
    res = set()
    for item in repos:
        repo = RepoSchema().load(item)
        if repo.license:
            if "python" in repo.topics:
                res.add(repo.license.key)
    return list(res)


print(fetch_licenses())
