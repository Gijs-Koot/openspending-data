import requests
from typing import List, Dict
from urllib.parse import urljoin
from itertools import islice
import logging
import json


class OpenSpending(object):

    base_url = "https://openspending.nl"

    def entries(self, params: dict = {}, max=100) -> List[dict]:

        path = "api/v1/entries"
        return list(islice(self._gen_objects(path, params), max))

    def governments(self, params: dict = {}, max=100) -> List[dict]:

        path = "api/v1/governments"
        return list(islice(self._gen_objects(path, params), max))

    def _gen_objects(self, path: str, params: Dict):

        nxt = path

        while nxt:

            url = urljoin(self.base_url, nxt)
            raw = requests.get(url, params=params)

            try:
                response = raw.json()
                for obj in response["objects"]:
                    yield obj
                nxt = response["meta"]["next"]
            except (ValueError, TypeError) as e:
                logging.warning(f"Got error {e}\n{raw.content}")


if __name__ == "__main__":

    os = OpenSpending()
    print(os.entries(dict(gov_code="GM")))
