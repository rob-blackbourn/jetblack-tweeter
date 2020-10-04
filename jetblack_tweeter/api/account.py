"""Account messages"""

from typing import Optional

from ..constants import URL_API_1_1
from ..types import AbstractHttpClient


class Account:

    def __init__(self, client: AbstractHttpClient) -> None:
        self._client = client
        self._url = f'{URL_API_1_1}/account'

    async def settings(self):
        url = f'{self._url}/settings.json'
        return await self._client.get(url)

    async def verify_credentials(
            self,
            include_entities: Optional[bool] = None,
            skip_status: Optional[bool] = None,
            include_email: Optional[bool] = None
    ):
        body = {
            'include_entities': include_entities,
            'skip_status': skip_status,
            'include_email': include_email
        }
        url = f'{self._url}/verify_credentials.json'
        return await self._client.get(url, body)
