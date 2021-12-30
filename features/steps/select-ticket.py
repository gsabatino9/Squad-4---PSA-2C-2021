from behave import *

@given(u'an id')
def step_impl(context):
    context.id = 1

@when(u'call GET /tickets/id')
def step_impl(context):
    context.response = context.client.get('/tickets/{}'.format(context.id))

@then(u'we will get the selected ticket')
def step_impl(context):
    ticket_id = context.response.json()['id']
    assert ticket_id == context.id