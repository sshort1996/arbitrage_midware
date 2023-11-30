from abc import ABC, abstractmethod


class BookmakerAPI(ABC):
    """
    Abstract base class to represent a bookmaker's API interface.
    """

    is_authenticated = False

    @abstractmethod
    def authenticate(self):
        """
        Authenticate with the bookmaker's API service.

        Implementations should establish a session or retrieve an auth token.
        """
        pass

    @abstractmethod
    def get_available_events(self):
        """
        Retrieve available betting events from the bookmaker.

        Implementations should return data in a consistent format.
        """
        pass

    @abstractmethod
    def place_bet(self, event_id, stake, odds, bet_type="single", **kwargs):
        """
        Place a bet on an event with the bookmaker.

        Args:
            event_id: The identifier for the event to bet on.
            stake: The amount of money to wager.
            odds: The agreed upon odds at the time of placing the bet.
            bet_type: The type of bet (e.g., single, parlay, etc.).
            **kwargs: Additional arguments specific to the bet type or bookmaker.

        Implementations should perform the bet placement and handle errors.
        """
        pass

    @abstractmethod
    def withdraw_funds(self, amount):
        """
        Withdraw funds from the user's account.

        Args:
            amount: The amount of money to withdraw.

        Implementations should carry out the withdrawal process.
        """
        pass
