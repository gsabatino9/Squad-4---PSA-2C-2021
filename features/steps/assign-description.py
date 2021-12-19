from behave import *
from app.db.crud import get_ticket

TICKET_TO_CREATE = {
    'title': 'Test Ticket assign emplyee',
    'description': 'Tiket for testing number 1',
    'product_id': 1,
    'ticket_type': 'BUG',
    'severity': 1
}

@given(u'no description')
def step_impl(context):
    context.description = None

@when(u'call POST /tickets with specific description')
def step_impl(context):
    context.response = context.client.post('/tickets/', json = {**TICKET_TO_CREATE, 'description': context.description})


@given(u'a description')
def step_impl(context):
    context.description = 'This is a testing ticket'

@then(u'we will create a ticket with description assigne')
def step_impl(context):
    ticket_id = context.response.json()['id']
    ticket = get_ticket(context.db, ticket_id)
    assert ticket.description == context.description