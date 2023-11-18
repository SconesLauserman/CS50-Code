from lib.JavascriptCall import CheckEmailValid, CheckUsernameValid, SearchUsernames
import os
from random import choice
from pytest import raises

def test_CheckUsernameValid():
    test_username = "SomethingLastname"
    try:
        os.mkdir(f"Users/{test_username}")
        assert CheckUsernameValid(test_username) == "Invalid"
        os.rmdir(f"Users/{test_username}")
    except Exception:
        pass


def test_CheckEmailValid():
    test_mail = "soemthing.lastname@gmail.com"
    try:
        with open("Users/Emails.txt", "a") as Emails:
            Emails.write(test_mail)
        with open("Users/Emails.txt", "r") as Emails:
            assert CheckEmailValid(test_mail) == "Invalid"
    except Exception:
        pass

def test_SearchUsernames():
    test_search_username = choice(os.listdir("Users"))
    try:
        os.mkdir(f"Users/{test_search_username}")
        assert test_search_username in SearchUsernames()
    except Exception:
        pass


