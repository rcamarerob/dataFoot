from dataclasses import dataclass
from model import match

@dataclass
class MatchStats:
    _match: match
    _home_shots: int
    _away_shots: int
    _home_shots_target: int
    _away_shots_target: int
    _home_hit_woodwork: int
    _away_hit_woodwork: int
    _home_corners: int
    _away_corners: int
    _home_fouls: int
    _away_fouls: int
    _home_offsides: int
    _away_offsides: int
    _home_red_cards: int
    _away_red_cards: int
    _home_yellow_cards: int
    _away_yellow_cards: int