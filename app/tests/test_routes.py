def test_get_all_dogs_with_empty_db_return_empty_list(client):
    # 'client' is the fixture we registered from the conftest.py, 
    # pytest automatically tries to match each test parameter to a 
    # fixture with the same name.

    response = client.get('/dogs')

    response_body = response.get_json()

    assert response_body == []
    assert response.status_code == 200