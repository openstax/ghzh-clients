import os

import pytest

from src import GitHubClient, ZenHubClient

credentials = [
    os.environ.get("GITHUB_USER", "foo"),
    os.environ.get("GITHUB_PASSWORD", "bar"),
    os.environ.get("ZENHUB_TOKEN", "x" * 20)
]


@pytest.fixture
def github_client():
    gh = GitHubClient(user=credentials[0],
                      password=credentials[1])

    yield gh

    gh.session.close()


@pytest.fixture
def zenhub_client():
    zh = ZenHubClient(token=credentials[2])

    yield zh

    zh.session.close()


@pytest.fixture(scope='module')
def vcr_config():
    return {
        # Replace the request headers in cassettes
        "filter_headers": [
            ('Authorization', "beepboopbeep"),
            ("X-Authentication-Token", "x" * 20)
        ],
    }
