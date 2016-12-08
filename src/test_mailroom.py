"""This file will test the functions in mailroom.py."""


import pytest
from faker import Faker

    # donors = {
    #                 'Matthew Wade': [50.00, 100.00],
    #                 'Betty Stewart': [100.00, 50.00, 150.00],
    #                 'Timothy Berg': [10.00],
    #                 'Paul Benson': [5]}

def test_list_check():
    """Tests to see whether names are added to the donor table"""
    from mailroom import list_check, donors
    list_check('Patrick Stewart')
    assert donors['Patrick Stewart'] == []


def test_add_donation():
    from mailroom import add_donation, donors
    add_donation('Patrick Stewart', 50.00)
    assert donors['Patrick Stewart'] == [50.00]
