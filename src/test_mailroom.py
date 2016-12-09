"""This file will test the functions in mailroom.py."""


import pytest


def test_list_check():
    """Tests to see whether names are added to the donor table"""
    from mailroom import list_check, donors
    list_check('Patrick Stewart')
    assert donors['Patrick Stewart'] == []


def test_add_donation():
    """Test whether we properly add dontaions to existing donors."""
    from mailroom import add_donation, donors
    add_donation('Patrick Stewart', 50)
    assert donors['Patrick Stewart'] == [50]

def test_print_email():
    """Test whether we properly add values to the email generator."""
    from mailroom import print_email, add_donation, donors
    add_donation('Patrick Stewart', 50)
    assert 'Patrick Stewart' and '50' in print_email('Patrick Stewart')


def test_print_donor_list():
    from mailroom import print_donor_list, add_donation, donors
    add_donation('Patrick Stewart', 50)
    add_donation('Patrick Stewart', 200)
    example = "Name: {}, Total Donated: {}, Number of Donations: {}, Average Donation: {}.".format('Patrick Stewart', 250, 2, 125)
    assert print_donor_list('Patrick Stewart') == example
