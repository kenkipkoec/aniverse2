# tests/test_api_integration.py

import pytest
from unittest.mock import patch
from backend.app.api_integration import fetch_posts, create_post

@patch("backend.app.api_integration.requests.get")
def test_fetch_posts(mock_get):
    # Mock the response from the API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {"id": 1, "title": "Test Post 1", "body": "Body of Test Post 1"},
        {"id": 2, "title": "Test Post 2", "body": "Body of Test Post 2"}
    ]

    # Call the function
    posts = fetch_posts()

    # Assertions
    assert posts is not None
    assert len(posts) == 2
    assert posts[0]["title"] == "Test Post 1"

@patch("backend.app.api_integration.requests.post")
def test_create_post(mock_post):
    # Mock the response from the API
    mock_post.return_value.status_code = 201
    mock_post.return_value.json.return_value = {
        "id": 101,
        "title": "New Test Post",
        "body": "Body of New Test Post",
        "userId": 1
    }

    # Call the function
    new_post = create_post("New Test Post", "Body of New Test Post", 1)

    # Assertions
    assert new_post is not None
    assert new_post["title"] == "New Test Post"
    assert new_post["userId"] == 1
