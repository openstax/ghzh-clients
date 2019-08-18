import pytest


@pytest.mark.vcr()
def test_get_board(zenhub_client):

    repo_id = "132146582"
    workspace_id = "5af1f4cc12da5e6d74331b60"

    board = zenhub_client.get_board(workspace_id=workspace_id, repo_id=repo_id)

    assert "pipelines" in board

    pipelines = board["pipelines"]

    assert len(pipelines) == 14


@pytest.mark.vcr()
def test_get_issue(zenhub_client):

    repo_id = "145164796"
    issue_num = "33"

    issue = zenhub_client.get_issue(repo_id, issue_num)

    assert not issue["is_epic"]
    assert not issue["plus_ones"]
    assert issue_num == issue_num
    assert issue["pipeline"]["name"] == "New Issues"


@pytest.mark.vcr()
def test_get_issue_events(zenhub_client):

    repo_id = "145164796"
    issue_num = "33"

    issue_events = zenhub_client.get_issue_events(repo_id, issue_num)

    assert len(issue_events) == 2
