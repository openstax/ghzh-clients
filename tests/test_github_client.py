import pytest


@pytest.mark.vcr()
def test_find_pr_commits(github_client):

    repo = "openstax/openstax-cms"
    base = "32cd356522ae5f923a68ad30627e8e462f874303"
    head = "d86fb8ea2fbadd831aba669d67ac2f27e6b58057"

    pr_commits = github_client.find_pr_commits(repo, base, head)

    assert 10 == len(pr_commits)

    for commit in pr_commits:
        assert commit.is_pr_commit
