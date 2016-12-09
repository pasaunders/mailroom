"""Automate thankyou notes and generates donor reports."""

import io
from faker import Faker
# from builtins import input

donors = {}


def get_input():
    """Function gathers all user input and controls program flow."""
    ask_report = input("Thankyou letter (1), report (2) or quit? (q)")
    if ask_report == 1:
        thankyou_input = input("Do you want a list (1) or to enter a donor name (2)")
        while thankyou_input == 1:
            show_list()
            thankyou_input = input("Do you want a list (1) or to enter a donor name (2)")
        if thankyou_input == 2:
            name_added = input("Please enter the donor name:")
            list_check(name_added)
            donor_amount = int(input("How much did they donate?"))
            add_donation(name_added, donor_amount)
            print(print_email(name_added))
            get_input()
    elif ask_report == 2:

    elif ask_report.lower() == 'q':

    else:
        print("Incorrect input, please enter 1, 2 or q")
        get_input()


def show_list():


def list_check(name_added):
    """Check if the provided name is in the donor list, if not, adds it."""
    if name_added not in donors:
        donors[name_added] = []


def add_donation(name_added, donor_amount):
    """Append a dontation amount to a donor's dictionary entry."""
    donors[name_added].append(donor_amount)


def print_email(name_added):
    """Take a donor name and uses it to draft a thank you letter for their most recent donation."""
    return "Dear {}; Thank you for your generous donation of {}. Your continued support allows us to fight on for the unprotected rainforests of the world.".format(name_added, donors[name_added][-1])
