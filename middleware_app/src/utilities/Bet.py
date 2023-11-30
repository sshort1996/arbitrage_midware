from datetime import datetime
from typing import Set
from pydantic import BaseModel


class NoDirectInstantiationMeta(type(BaseModel)):
    """
    A metaclass for preventing direct instantiation of classes.
    """
    def __call__(cls, *args, **kwargs):
        raise ValueError("This class cannot be instantiated directly. Use the create() method instead.")
    

class CustomBaseModel(BaseModel, metaclass=NoDirectInstantiationMeta):
    pass


class Bet(CustomBaseModel):
    """
    Represents a betting event.

    Attributes:
        event_id (int): The unique identifier of the event.
        bookmaker_id (int): The unique identifier of the bookmaker.
        sport (str): The sport of the betting event.
        event_date (datetime): The date and time of the event.
        event_date (datetime): The timezone in which the event occurs.
        participants (set): The set of participants in the event.
        outcome (str): The selected outcome of the bet for the target participant.
        target (int): The participant to which the chosen outcome refers.
        stake (float): The amount wagered on the bet.
        odds (float): The odds of the bet.
        odds_unit (str): The selected odds standard, i.e., fractional, american, or decimal.
    """

    event_id: int
    bookmaker_id: int
    sport: str
    event_date: datetime
    event_tz: str
    participants: Set[str]
    outcome: str
    target: str
    stake: float
    odds: float
    odds_unit: str

    def __str__(self):
        return (
            f"""
            Bet(
                event_id={self.event_id},
                f"bookmaker_id={self.bookmaker_id},
                f"sport='{self.sport}',
                f"event_date={self.event_date.strftime('%Y-%m-%d %H:%M:%S')},
                f"event_tz='{self.event_tz}',
                f"participants={', '.join(self.participants)},
                f"outcome='{self.outcome}',
                f"target='{self.target}',
                f"stake={self.stake:.2f},
                f"odds={self.odds:.2f},
                f"odds_unit='{self.odds_unit}'
            )"""
        )

    @classmethod
    def create(cls, **data):
        """
        Custom class method to create a Bet object.

        Args:
            **data: Keyword arguments representing the attributes of the Bet object.

        Returns:
            Bet: The created Bet object.

        Raises:
            ValueError: If the target participant is not in the participants set.
            ValueError: If the event_tz string is not a valid timezone.
        """
        instance = super().__new__(cls)
        instance.__init__(**data)

        print(f'post init checks - target: {instance.target}, participants: {instance.participants}')
        if instance.target not in instance.participants:
            raise ValueError("Target participant must be one of the participants")

        # Check if event_tz is a valid timezone
        from pytz import all_timezones
        if instance.event_tz not in all_timezones:
            raise ValueError("Invalid timezone")

        return instance
    
    def place_with_bookmaker(self, bookmaker_api):
        """
        Place this bet using a specific bookmaker's API.

        Args:
            bookmaker_api: An instance of a subclass of BookmakerAPI.
        """
        # Ensure that bookmaker_api is authenticated before placing the bet
        if not bookmaker_api.is_authenticated:
            bookmaker_api.authenticate()

        # Retrieve this instance's attributes as a dictionary
        bet_details = vars(self)

        bookmaker_api.place_bet(**bet_details)
