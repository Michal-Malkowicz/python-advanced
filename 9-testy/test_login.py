import pytest
import requests

URL = 'https://reqres.in/api/login'
URL2 = 'https://reqres.in/api/users?page=2'


@pytest.mark.parametrize('login_data, exp_result, exp_key',
                         [({"email": "eve.holt@reqres.in", "password": "cityslicka"}, 200, 'token'),
                          ({'email': 'peter@klaven'}, 400, 'error')])
def test_login(login_data, exp_result, exp_key):
    print(login_data)
    print(requests.post(URL, json=login_data))
    print(requests.post(URL, json=login_data).json())

    assert requests.post(URL, json=login_data).status_code == exp_result
    assert exp_key in requests.post(URL, json=login_data).json()


