from datetime import datetime
from gists_database.search import search_gists

from .fixtures import populated_gists_database as db


def test_search_without_parameters_returns_all_gists(db):
    gists = search_gists(db)
    assert len(gists) == 7


def test_search_with_github_id(db):
    gists = search_gists(db, github_id='4232a4cdad00bd92a7a64cf3e2795820')
    assert len(gists) == 1

    gist = gists[0]
    assert gist.github_id == '4232a4cdad00bd92a7a64cf3e2795820'


def test_search_with_created_date_equals(db):
    # 2014-05-03T20:26:08Z
    d = datetime(2014, 5, 3, 20, 26, 8)

    gists = search_gists(db, created_at=d)
    assert len(gists) == 1

    gist = gists[0]
    assert gist.github_id == '18bdf248a679155f1381'

### Optional functionality
### Uncomment the tests that you want to implement

# """
def test_search_with_created_date_gte(db):
    d = datetime(2017, 5, 10, 16, 2, 54)
    gists = search_gists(db, created_at__gte=d)
    assert len(gists) == 1

    gist = gists[0]
    assert gist.github_id == '4232a4cdad00bd92a7a64cf3e2795820'


def test_search_with_created_date_lt(db):
    d = datetime(2014, 11, 28)
    gists = search_gists(db, created_at__lt=d)
    assert len(gists) == 3

    gist = gists[0]
    assert gist.github_id == '291bfcfe70d2f9582331'

    gist = gists[1]
    assert gist.github_id == '1adb5bee99400ce615a5'

    gist = gists[2]
    assert gist.github_id == '18bdf248a679155f1381'


def test_search_with_created_date_lte(db):
    d = datetime(2014, 5, 3, 20, 26, 8)
    gists = search_gists(db, created_at__lte=d)
    assert len(gists) == 1

    gist = gists[0]
    assert gist.github_id == '18bdf248a679155f1381'


def test_search_with_multiple_and_params(db):
    d = datetime(2014, 5, 3, 20, 26, 8)
    gists = search_gists(db, created_at__lte=d,
                                  github_id='18bdf248a679155f1381')
    assert len(gists) == 1

    gist = gists[0]
    assert gist.github_id == '18bdf248a679155f1381'


def test_search_with_multiple_dates(db):
    d = datetime(2014, 5, 3, 20, 26, 8)
    gists = search_gists(db, created_at__lte=d, updated_at__gte=d)
    assert len(gists) == 1

    gist = gists[0]
    assert gist.github_id == '18bdf248a679155f1381'
# """
