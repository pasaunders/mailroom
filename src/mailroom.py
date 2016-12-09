"""Automate thankyou notes and generates donor reports."""

import io
import sys

# from builtins import input

donors = {
            'Matthew Wade': [50.00, 100.00],
            'Betty Stewart': [100.00, 50.00, 150.00],
            'Timothy Berg': [10.00],
            'Paul Benson': [5]}


def get_input():
    """Function gathers all user input and controls program flow."""
    ask_report = input("Thank you letter (1), report (2), return to the home menu, (3), or quit? (q) ")
    if ask_report == '1':
        thankyou_input = input("Do you want a list (1) or to enter a donor name (2) ")
        while thankyou_input == '1':
            print("\nDonor List:\n")
            print(show_list(donors))
            thankyou_input = input("Do you want to see a list (1), enter a donor name (2), or return to the main menu? (3) ")
        if thankyou_input == '2':
            name_added = input("Please enter the donor name: ")
            list_check(name_added, donors)
            donor_amount = int(input("How much did they donate? "))
            add_donation(name_added, donor_amount, donors)
            print(print_email(name_added, donors))
            get_input()
        elif thankyou_input == '3':
            get_input()
    elif ask_report == '2':
        print("Below, please find a report of all donor information. ")
        for key in donors:
            print(print_donor_list(key, donors))
        get_input()
    elif ask_report == '3':
        get_input()
    elif ask_report.lower() == 'q':
        sys.exit()
    else:
        print("Incorrect input. Please try again. ")
        get_input()


def show_list(donors_new):
    """Return a donor name."""
    return " \n".join(sorted(donors_new.keys()))


def list_check(name_added, donors_new):
    """Check if the provided name is in the donor list, if not, adds it."""
    if name_added not in donors_new:
        donors_new[name_added] = []


def add_donation(name_added, donor_amount, donors_new):
    """Append a dontation amount to a donor's dictionary entry."""
    donors_new[name_added].append(donor_amount)


def print_email(name_added, donors_new):
    """Take a donor name and uses it to draft a thank you letter for their most recent donation."""
    return "Dear {}; Thank you for your generous donation of ${}. Your continued support allows us to fight on for the unprotected rainforests of the world.".format(name_added, donors_new[name_added][-1])


def print_donor_list(key, donors_new):
    """Return donor name, total donated, number of donations, average donation."""
    return "\nName: {}\n Total Donated: {}\n Number of Donations: {}\n Average Donation: {}\n\n".format(key, sum(donors_new[key]), len(donors_new[key]), int(sum(donors_new[key])/len(donors_new[key])))


if __name__ == "__main__":
    """Run the program in the terminal."""
    get_input()
