from openspending import OpenSpending


def test_entries():

    os = OpenSpending()
    entries = os.entries(params=dict(year=2012), max=23)

    assert len(entries) == 23

    assert "code_sub" in entries[0]
    assert entries[15]["year"] == 2012


def test_entries_by_gov():

    os = OpenSpending()
    entries = os.entries(params=dict(year=2018, gov_code=358), max=1000)

    assert len(entries) > 5


def test_govs():

    os = OpenSpending()
    govs = os.governments(params=dict(), max=1000)

    assert len(govs) == 726
