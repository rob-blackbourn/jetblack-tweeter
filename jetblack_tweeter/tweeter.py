"""The twitter client"""

from typing import Optional

from .auth_client import AuthenticatedHttpClient
from .api import Account, Stream, Statuses
from .types import AbstractTweeterSession


class Tweeter:

    def __init__(
            self,
            session: AbstractTweeterSession,
            app_key: str,
            app_key_secret: str,
            *,
            access_token: Optional[str] = None,
            access_token_secret: Optional[str] = None
    ):
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
