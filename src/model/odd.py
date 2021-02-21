from dataclasses import dataclass
from model.odd_enum import OddEnum


@dataclass
class Odd:
    _match_id: str
    _odd: str
    _home_win_value: float
    _draw_value: float
    _away_win_value: float

    @property
    def match_id(self) -> str:
        return self._match_id

    @property
    def odd(self) -> str:
        return self._odd

    @property
    def home_win_value(self) -> float:
        return self._home_win_value

    @property
    def draw_value(self) -> float:
        return self._draw_value

    @property
    def away_win_value(self) -> float:
        return self._away_win_value

    def __iter__(self):
        return iter(vars(self).values())