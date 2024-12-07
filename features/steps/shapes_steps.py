from behave import *
from shapes import *

@given('the program is loaded')
def step_impl(context):
    pass

@when('the program starts')
def step_impl(context):
    context.shapes = Shapes()

@then('a blank scene of size 40x20 is created')
def step_impl(context):
    assert context.shapes.width == 40
    assert context.shapes.height == 20   
