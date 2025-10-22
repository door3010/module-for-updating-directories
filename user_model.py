from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    hostname: str
    port: int
    username: str
    password: str
