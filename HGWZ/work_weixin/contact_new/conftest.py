import pytest

from HGWZ.work_weixin.contact_new.token import Weixin


@pytest.fixture(scope="session")
def token():
    return Weixin.get_token_new()