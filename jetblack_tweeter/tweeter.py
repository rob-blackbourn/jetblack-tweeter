"""The twitter client"""

from typing import Optional

from .auth_client import AuthenticatedHttpClient
from .api import Account, Stream, Statuses
from .types import AbstractTweeterSession


class Tweeter:
    """The Twitter client.
    """

    def __init__(
            self,
            session: AbstractTweeterSession,
            app_key: str,
            app_key_secret: str,
            *,
            access_token: Optional[str] = None,
            access_token_secret: Optional[str] = None
    ):
        """Initialise the Twitter client.

        Args:
            session (AbstractTweeterSession): The Twitter session implementation.
            app_key (str): The app-key.
            app_key_secret (str): The app-key-secret
            access_token (Optional[str], optional): An optional access
                token. Defaults to None.
            access_token_secret (Optional[str], optional): An optional access
                token secret. Defaults to None.

        Attributes:
            statuses (Statuses): Access to the statuses end point.
            account (Account): Access to the account end point.
            stream (Stream): Access to the stream end point.
        """
        client = AuthenticatedHttpClient(
            session,
            consumer_key=app_key,
            consumer_secret=app_key_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
        self.statuses = Statuses(client)
        self.account = Account(client)
        self.stream = Stream(client)
