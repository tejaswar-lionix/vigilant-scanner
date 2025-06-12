from dataclasses import dataclass

@dataclass
class Config:
    entropy_threshold: float = 3.5
    fail_on: str = "high"
    include_tests: bool = False

config = Config()
