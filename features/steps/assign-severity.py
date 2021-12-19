from behave import *
from app.db.crud import get_ticket

TICKET_TO_CREATE = {
    'title': 'Test Ticket assign emplyee',
    'description': 'Tiket for testing number 1',
    'product_id': 1,
    'ticket_type': 'BUG',
    'severity': 1
}

@given(u'no severity')
def step_impl(context):
    context.severity = None

@when(u'call POST /tickets with specific severity')
def step_impl(context):
    context.response = context.client.post('/tickets/', json = {**TICKET_TO_CREATE, 'severity': context.severity})

@then(u'we will not create a ticket')
def step_impl(context):
    assert context.response.status_code == 422
    assert context.response.reason == 'Unprocessable Entity'

@given(u'a severity')
def step_impl(context):
    context.severity = 1

@then(u'we will create a ticket with severity assigne')
def step_impl(context):
    ticket_id = context.response.json()['id']
    ticket = get_ticket(context.db, ticket_id)
    assert ticket.severity == 1