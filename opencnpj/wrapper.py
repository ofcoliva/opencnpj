import requests
import re

URL = "https://api.opencnpj.org/"
MAX_RPS = 50

class OpenCNPJ():
    """
    OpenCNPJ Wrapper
    """
    def __init__(self):
        global URL, MAX_RPS
        self.max_request_per_secount = MAX_RPS
        self.url = URL

    def find_by_cnpj(self, cnpj: str):
        url = self.url + self.parse_cnpj(cnpj)
        response = requests.get(
            url=url,
            verify=True, # Set verify to False to disable SSL certificate checking
            )

        if response.status_code == 404:
            return "CNPJ not found"
        elif response.status_code == 429:
            return "Too many requests"
        
        return response.text

    def parse_cnpj(self, cnpj: str) -> str:
        if type(cnpj) != str:
            raise "The expected primitive type in cnpj is str"

        cnpj = re.sub(r'\D', '', cnpj)
        
        if len(cnpj) != 14:
            raise "Valid CNPJ numbers have 14 digits"

        return cnpj
