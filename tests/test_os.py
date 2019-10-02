from unittest import mock
import json

from openspending import OpenSpending

# load mock value
mock_entries = json.load(open("./resources/entries.json"))
mock_govs = json.load(open("./resources/governments.json"))

def test_entries():
   
    os = OpenSpending()
    
    with mock.patch("openspending.requests") as mr:
        mr.get.return_value.json.return_value = mock_entries
        entries = os.entries(params=dict(year=2012), max=36)

    assert len(entries) == 36

    assert "code_sub" in entries[0]
    assert entries[15]["year"] == 2012


def test_entries_by_gov():

    # mock value
    
    os = OpenSpending()

    with mock.patch("openspending.requests") as mr:

        mr.get.return_value.json.return_value = mock_entries

        params = dict(year=2018, gov_code=358)
        url = os.base_url + "/" + "api/v1/entries"
        entries = os.entries(params, max=6)

        mr.get.called_once_with(url, params)
        
    assert len(entries) > 5


def test_govs():

    os = OpenSpending()

    with mock.patch("openspending.requests") as mr:
        mr.get.return_value.json.return_value = mock_govs
        govs = os.governments(params=dict(), max=726)

    assert len(govs) == 726
