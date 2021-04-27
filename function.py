import os
from flask import Flask, session, flash, redirect, url_for
import re

def isValid(email):
    """Checks for valid email addresses
    On the register form needs a genuine emails so isvalid to
    validate emails address.
    Args:
        email: the email address supplied for validation.
    Returns:
        If email is address is valid it will return True if not then it is False.
    """
    if (re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
       is not None):
        return True
    return False