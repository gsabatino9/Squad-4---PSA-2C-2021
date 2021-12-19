from behave import *
from app.db.crud import get_ticket

TICKET_TO_CREATE = {
    'title': 'Test Ticket assign emplyee',
    'description': 'Tiket for testing number 1',
    'product_id': 1,
    'ticket_type': 'BUG',
    'severity': 1
}

@given(u'no title')
def step_impl(context):
    context.title = None

@when(u'call POST /tickets with specific title')
def step_impl(context):
    context.response = context.client.post('/tickets/', json = {**TICKET_TO_CREATE, 'title': context.title})


@given(u'a title')
def step_impl(context):
    context.title = 'Testint ticket title'

@then(u'we will create a ticket with title assigne')
def step_impl(context):
    ticket_id = context.response.json()['id']
    ticket = get_ticket(context.db, ticket_id)
    assert ticket.title == context.title