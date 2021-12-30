from behave import *
from app.db.crud import get_ticket

TICKET_TO_CREATE = {
    'title': 'Test Ticket assign emplyee',
    'description': 'Tiket for testing number 1',
    'product_id': 1,
    'ticket_type': 'BUG',
    'severity': 1
}


@given(u'no state')
def step_impl(context):
    context.state = None

@given(u'IN_PROGRESS state')
def step_impl(context):
    context.state = 'IN_PROGRESS'

@given(u'WAITING_DEVELOP state')
def step_impl(context):
    context.state = 'WAITING_DEVELOP'


@given(u'WAITING_CLIENT state')
def step_impl(context):
    context.state = 'WAITING_CLIENT'


@given(u'CLOSE state')
def step_impl(context):
    context.state = 'CLOSE'

@when(u'call POST /tickets with specific state')
def step_impl(context):
    context.response = context.client.post('/tickets/', json = {**TICKET_TO_CREATE})

@when(u'call PUT /tickets with specific state')
def step_impl(context):
    context.response = context.client.put('/tickets/1', json = {'state': context.state})

@then(u'ticket created with correct state')
def step_impl(context):
    ticket_id = context.response.json()['id']
    ticket = get_ticket(context.db, ticket_id)
    assert ticket.state == 'OPEN'


@then(u'set correct state')
def step_impl(context):
    ticket_id = context.response.json()['id']
    ticket = get_ticket(context.db, ticket_id)
    assert ticket.state == context.state

