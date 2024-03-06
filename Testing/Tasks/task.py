# main.py

import re

def check_email(email):
    # Check if the email is in a valid format
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def check_psw(password):
    # Check if the password meets the criteria
    return bool(re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$£])[A-Za-z\d@$£]{8,}$", password))

def check_psw_equal(password1, password2):
    # Check if two passwords are equal
    return password1 == password2

def check_credentials(email, password1, password2):
    # Check if email is valid and passwords are equal
    return check_email(email) and check_psw_equal(password1, password2)

# Tests to question 1: -------------------------------
# (tests for check_email and check_psw functions)

# TODO write the unit tests for the new functions, remove the comment notation and replace assert False with your code: ---------------------------- 
# 1. Test that two equal passwords return true
def test_psw_equal1():
    psw1 = "password123"
    psw2 = "password123"
    assert check_psw_equal(psw1, psw2) is True

# 2. Test that the function is case sensitive
def test_psw_equal2():
    psw1 = "Password123"
    psw2 = "password123"
    assert check_psw_equal(psw1, psw2) is False

# 3. Test that two inequal passwords return false
def test_psw_equal3():
    psw1 = "password123"
    psw2 = "different456"
    assert check_psw_equal(psw1, psw2) is False

# 4. Test that two equal passwords in the correct format and a correct email return true
def test_check_credentials1():
    email = "myname326@gmail.com"
    psw1 = "Qwerty123"
    psw2 = "Qwerty123"
    assert check_credentials(email, psw1, psw2) is True

# 5. Test that two inequal passwords in the correct format and a correct email return false
def test_check_credentials2():
    email = "myname326@gmail.com"
    psw1 = "Qwerty123"
    psw2 = "Different456"
    assert check_credentials(email, psw1, psw2) is False

# 6. Test that two equal passwords in the correct format and an incorrect email return false
def test_check_credentials3():
    email = "invalid_email"
    psw1 = "Qwerty123"
    psw2 = "Qwerty123"
    assert check_credentials(email, psw1, psw2) is False
