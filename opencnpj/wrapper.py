# opencnpj/client.py

import requests
import re

# Importe todas as suas novas exceções
from .exceptions import (
    NetworkError,
    RateLimitError,
    RequestError,
    ServerError,
    TimeoutError,
)


class OpenCNPJ:
    def __init__(self) -> None:
        self._BASE_URL = 'https://api.opencnpj.org/'
        self._session = requests.Session()
        self._session.headers.update({'Accept': 'application/json'})

    def _request(self, cnpj):
        url = self._BASE_URL + self.parse_cnpj(cnpj)
        try:
            response = self._session.get(url, timeout=30)

            response.raise_for_status()
            
            return response.json()

        except requests.exceptions.Timeout as err:
            raise TimeoutError(f'Request timed out for {url}') from err
        
        except requests.exceptions.ConnectionError as err:
            raise NetworkError(f'A network error occurred for {url}') from err
            
        except requests.exceptions.HTTPError as err:
            status_code = err.response.status_code

            if status_code == 429:
                raise RateLimitError('API rate limit exceeded. Please wait before trying again.') from err
            elif status_code >= 500:
                raise ServerError(f'API server error (status {status_code}). Please try again later.') from err
            else:
                raise RequestError(
                    f'Unhandled HTTP error (status {status_code}): {err.response.text}'
                ) from err

    def parse_cnpj(self, cnpj: str) -> str:
        if type(cnpj) != str:
            raise "The expected primitive type in cnpj is str"

        cnpj = re.sub(r'\D', '', cnpj)
        
        if len(cnpj) != 14:
            raise "Valid CNPJ numbers have 14 digits"

        return cnpj

    def find_by_cnpj(self, cnpj: str):
        """Recupera os dados de uma empresa a partir do seu CNPJ."""
        return self._request(cnpj)
