# mailroom
Mail room assignment form codefellows python 401 course.

This program offers charitable and for-profit organizations a simple, easy way to manage their donor rolls. 

In the main menu, users have the option to prepare a thank you note, to see a report of donor contributions, to return to the main menu, or to quit. 

If the choose to prepare a thank you note, they are then given the option to see a list of tracked donors, or to add a new donation by entering a donor name. If they choose to see a list, the terminal displays a user-friendly list of donor names. If the enter a donor name, that name is entered as a new key in the donor dictionary (if it did not previously exist), and then the user has the opportunity to enter the amount donated. An email is then printed out thanking the donor for their generous contribution, and the user is redirected to the menu.

If the user chooses to see a report, a simple report is generated. The report displays the name of all historical donors, the amount of each donor's cumulative donations, the number of their donations, and the average amount donated eah time. This information will invariably be useful in future fundraising endeavors. 

The user can quit or return to the home menu at any time.


```
#Test Results:
py27 installed: coverage==4.2,Faker==0.7.3,ipaddress==1.0.17,mailroom==0.1,py==1.4.31,pytest==3.0.5,pytest-cov==2.4.0,python-dateutil==2.6.0,six==1.10.0
py27 runtests: PYTHONHASHSEED='4160572942'
py27 runtests: commands[0] | py.test src --cov=src --cov-report term-missing
======================================== test session starts ========================================
platform darwin -- Python 2.7.10, pytest-3.0.5, py-1.4.31, pluggy-0.4.0
plugins: cov-2.4.0
collected 5 items 

src/test_mailroom.py .....

---------- coverage: platform darwin, python 2.7.10-final-0 ----------
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
src/mailroom.py           44     29    34%   17-44, 60, 75
src/test_mailroom.py      23      0   100%
----------------------------------------------------
TOTAL                     67     29    57%


===================================== 5 passed in 0.03 seconds ======================================
py35 installed: coverage==4.2,Faker==0.7.3,mailroom==0.1,py==1.4.31,pytest==3.0.5,pytest-cov==2.4.0,python-dateutil==2.6.0,six==1.10.0
py35 runtests: PYTHONHASHSEED='4160572942'
py35 runtests: commands[0] | py.test src --cov=src --cov-report term-missing
======================================== test session starts ========================================
platform darwin -- Python 3.5.2, pytest-3.0.5, py-1.4.31, pluggy-0.4.0
plugins: cov-2.4.0
collected 5 items 

src/test_mailroom.py .....

---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
src/mailroom.py           44     29    34%   17-44, 60, 75
src/test_mailroom.py      23      0   100%
----------------------------------------------------
TOTAL                     67     29    57%


===================================== 5 passed in 0.03 seconds ======================================
```
