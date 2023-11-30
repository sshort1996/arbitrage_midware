from dataclasses import dataclass


# A generic dataclass representing a bet on an event
@dataclass
class Bet:
    event_id: int
    bookmaker_id: int
    bet_type: str
    stake: float
    odds: float
    selection: str
