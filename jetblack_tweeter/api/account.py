"""Account messages"""

from typing import Any, Mapping, Optional, cast

from ..constants import URL_API_1_1
from ..types import AbstractHttpClient
from ..utils import optional_bool_to_str


class Account:
    """The api for the account end point"""

    def __init__(self, client: AbstractHttpClient) -> None:
        """Initialise the account endpoint api

        Args:
            client (AbstractHttpClient): The authenticated client.
        """
        self._client = client
        self._url = f'{URL_API_1_1}/account'

    async def settings(
            self,
            timeout: Optional[float] = None
    ) -> Mapping[str, Any]:
        """Returns settings (including current trend, geo and sleep time
        information) for the authenticating user.

        Args:
            timeout (Optional[float], optional): If specified the timeout for
                the request. Defaults to None.

        Returns:
            Mapping[str, Any]: The account settings.
        """
        url = f'{self._url}/settings.json'
        return cast(
            Mapping[str, Any],
            await self._client.get(url, timeout=timeout)
        )

    async def verify_credentials(
            self,
            include_entities: Optional[bool] = None,
            skip_status: Optional[bool] = None,
            include_email: Optional[bool] = None,
            timeout: Optional[float] = None
    ) -> Mapping[str, Any]:
        """Returns an HTTP 200 OK response code and a representation of the
        requesting user if authentication was successful; returns a 401 status
        code and an error message if not. Use this method to test if supplied
        user credentials are valid.

        Args:
            include_entities (Optional[bool], optional): The entities node will
                not be included when set to false. Defaults to None.
            skip_status (Optional[bool], optional): When set to true statuses
                will not be included in the returned user object. Defaults to
                    None.
            include_email (Optional[bool], optional): When set to true email
                will be returned in the user objects as a string. If the user
                does not have an email address on their account, or if the email
                address is not verified, null will be returned. Defaults to
                None.
            timeout (Optional[float], optional): If specified the timeout for
                the request. Defaults to None.

        Returns:
            Mapping[str, Any]: User account details
        """
        body = {
            'include_entities': optional_bool_to_str(include_entities),
            'skip_status': optional_bool_to_str(skip_status),
            'include_email': optional_bool_to_str(include_email)
        }
        url = f'{self._url}/verify_credentials.json'
        return cast(
            Mapping[str, Any],
            await self._client.get(url, body, timeout)
        )
