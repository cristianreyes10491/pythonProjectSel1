import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class PokeApi():
  # 1. API Get consuption

  def test_api_response(self):
    id: int = 2
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/ditto/info?id={id}')

    assert response.status_code == 200, f"Status code: {response.status_code}"
    print("Status code correct")

    assert 'message' in response, "'message' is not in the response"
    print("'message' is in the response")

    assert response['message'] == "You made a GET request!", f"ID incorrect: {response['message']}"
    print("Correct message")
    response_time = response.elapsed.total_seconds() * 1000

    assert response_time < 500, f"Out of time response: {response_time}ms"
    print(f"Response time: {response_time}ms.")

    assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Response is not JSON"
    print("The content is JSON")

