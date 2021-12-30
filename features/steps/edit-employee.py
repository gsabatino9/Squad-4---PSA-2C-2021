from behave import *
from app.db.crud import get_ticket

@when(u'call PUT /tickets with specific employee')
def step_impl(context):
    context.response = context.client.put('/tickets/1', json = {'employee_id': context.employee_id})


@then(u'we will delete the employee assigned')
def step_impl(context):
    print(context.response.json())
    ticket_id = context.response.json()['id']
    ticket = get_ticket(context.db, ticket_id)
    assert ticket.employee_id == None

@then(u'we update the employee assigned')
def step_impl(context):
    ticket_id = context.response.json()['id']
    ticket = get_ticket(context.db, ticket_id)
    assert ticket.employee_id == 2