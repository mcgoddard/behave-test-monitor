from random import random
from behave import *

def failer():
    assert False

def errorer():
    10/0

@given('I {chance} {result}')
def step_impl(context, chance, result):
    # Set up what kind of problem we want
    if result == 'fail':
        tester = failer
    else:
        tester = errorer
    # Should we have a problem
    if chance == 'always':
        tester()
    elif chance == 'sometimes' and random() < 0.5:
        tester()
    else:
        pass
