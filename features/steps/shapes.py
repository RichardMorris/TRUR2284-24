from behave import *

@given('the program is running')
def step_impl(context):
    pass

@when('the program starts')
def step_impl(context):
    pass

@then('a bank scene of size {width:d}x{height:d} is created')
def step_impl(context, width, height):
    assert context.scene.width == width
    assert context.scene.height == height   
