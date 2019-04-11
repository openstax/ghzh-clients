import pytest


@pytest.mark.vcr()
def test_get_board(zenhub_client):

    repo_id = "145164796"

    board = zenhub_client.get_board(repo_id)

    assert "pipelines" in board

    pipelines = board["pipelines"]

    assert len(pipelines) == 10


@pytest.mark.vcr()
def test_get_issue(zenhub_client):

    repo_id = "145164796"
    issue_num = "33"

    issue = zenhub_client.get_issue(repo_id, issue_num)

    assert not issue["is_epic"]
    assert not issue["plus_ones"]
    assert issue_num == issue_num
    assert issue["pipeline"]["name"] == "Icebox"


@pytest.mark.vcr()
def test_get_issue_events(zenhub_client):

    repo_id = "145164796"
    issue_num = "33"

    issue_events = zenhub_client.get_issue_events(repo_id, issue_num)

    assert len(issue_events) == 2
