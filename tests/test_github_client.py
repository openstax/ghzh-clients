import pytest


@pytest.mark.vcr()
def test_find_pr_commits(github_client):

    repo = "openstax/biglearn-api"
    base = "ce2503b458a36053c5b7cb4fa88706a66e447fc2"
    head = "3c0fdb4ad15127d0d3eac2ff9ba376f94bf4c24f"

    pr_commits = github_client.find_pr_commits(repo, base, head)

    assert len(pr_commits) == 2

    for commit in pr_commits:
        assert commit.is_pr_commit
