from behave import *
from app.db.crud import get_ticket

TICKET_TO_CREATE = {
    'title': 'Test Ticket assign emplyee',
    'description': 'Tiket for testing number 1',
    'product_id': 1,
    'ticket_type': 'BUG',
    'severity': 1
}

@given(u'no employee')
def step_impl(context):
    context.employee_id = None

@when(u'call POST /tickets with specific employee')
def step_impl(context):
    context.response = context.client.post('/tickets/', json = {**TICKET_TO_CREATE, 'employee_id': context.employee_id})

@then(u'we will create a ticket with no employee assigned')
def step_impl(context):
    ticket_id = context.response.json()['id']
    ticket = get_ticket(context.db, ticket_id)
    assert ticket.employee_id == None

@given(u'a employee')
def step_impl(context):
    context.employee_id = 2

@then(u'we will create a ticket with employee assigne')
def step_impl(context):
    ticket_id = context.response.json()['id']
    ticket = get_ticket(context.db, ticket_id)
    assert ticket.employee_id == 2