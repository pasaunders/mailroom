"""This file will test the functions in mailroom.py."""


import pytest


def test_list_check():
    """Tests to see whether names are added to the donor table"""
    from mailroom import list_check
    donors_new = {}
    list_check('Patrick Stewart', donors_new)
    assert donors_new['Patrick Stewart'] == []


def test_add_donation():
    """Test whether we properly add dontaions to existing donors."""
    from mailroom import add_donation
    donors_new = {'Patrick Stewart': [50]}
    assert donors_new['Patrick Stewart'] == [50]

def test_print_email():
    """Test whether we properly add values to the email generator."""
    from mailroom import print_email
    donors_new = {'Patrick Stewart': [50]}
    assert 'Patrick Stewart' and '50' in print_email('Patrick Stewart', donors_new)


def test_print_donor_list():
    from mailroom import print_donor_list, add_donation, donors
    donors_new = {'Patrick Stewart': [50, 200]}
    example = "\nName: {}\n Total Donated: {}\n Number of Donations: {}\n Average Donation: {}\n\n".format('Patrick Stewart', 250, 2, 125)
    assert print_donor_list('Patrick Stewart', donors_new) == example


def test_show_list():
    from mailroom import show_list
    donors_new = {'Matthew Wade': [50.00, 100.00],
                'Betty Stewart': [100.00, 50.00, 150.00],
                'Timothy Berg': [10.00],
                'Paul Benson': [5]}
    assert show_list(donors_new) == " \n".join(sorted(['Matthew Wade', 'Betty Stewart', 'Timothy Berg', 'Paul Benson']))
