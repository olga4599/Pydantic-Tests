from pydantic import BaseModel
import pytest
import requests


class AccessToken(BaseModel):
    token: str

class Booking(BaseModel):
    first_name: str
    last_name: str
    total_price: int


def test_access_token():
    request = {"token": "abc123"}
    AccessToken(**request)

    assert 'token' in request

def test_access_token():
    request = {}
    with pytest.raises(ValueError):
        AccessToken(**request)

def test_access_token_format():
    request = {
        "access_token": "invalid_token_format"
    }
    with pytest.raises(ValueError):
        AccessToken(**request)


def test_get_booking_response():
    response = [
        {"first_name":"Will", "last_name": "Turner", "total_price": 344},
        {"first_name": "Jack", "last_name": "Sparrow", "total_price": 555},
    ]

    client = [Booking(**client) for client in response]

def test_get_booking_successful():
    response = [
        {"first_name":"Will", "last_name": "Turner", "total_price": 344},
        {"first_name": "Jack", "last_name": "Sparrow", "total_price": 555},
        {"first_name": "Elizabeth", "last_name": "Swan", "total_price": 1200},
    ]
    client = [Booking(**client) for client in response]

    assert len(client) == 3
    assert client[1].first_name == "Jack"
    assert client[1].last_name == "Sparrow"
    assert client[1].total_price == 555

def test_empty_booking_list():
    response = []
    client = [Booking(**client) for client in response]
    assert len(client) == 0

def test_booking_format():
    booker = {
                 "first_name": "Will",
                 "last_name": "Turner",
                 "total_price": "invalid_price_format"
             }

    with pytest.raises(ValueError):
        Booking(**booker)

def test_firstname_format():
    booker = {
                 "first_name": 000,
                 "last_name": "Turner",
                 "total_price": 344,
             }
    with pytest.raises(ValueError):
        Booking(**booker)
