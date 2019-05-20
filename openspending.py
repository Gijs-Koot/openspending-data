import requests
from urllib.parse import urljoin
from itertools import islice
import logging
import json


class OpenSpending(object):

    base_url = "https://openspending.nl"

    def entries(self, params: dict, max=100) -> list:

        path = "api/v1/entries"
        return list(islice(self.gen_objects(path, params), max))

    def governments(self, params: dict, max=100) -> list:

        path = "api/v1/governments"
        return list(islice(self.gen_objects(path, params), max))

    def gen_objects(self, path, params):

        nxt = path

        while nxt:

            url = urljoin(self.base_url, nxt)
            raw = requests.get(url, params=params)

            try:
                response = raw.json()
                for obj in response["objects"]:
                    yield obj
                nxt = response["meta"]["next"]
            except json.JSONDecodeError as e:
                logging.warning(f"Got error {e}\n{raw.content}")


if __name__ == "__main__":

    os = OpenSpending()
    print(os.entries(gov_code="GM"))
