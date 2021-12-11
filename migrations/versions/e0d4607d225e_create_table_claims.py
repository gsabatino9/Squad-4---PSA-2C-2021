"""create table claims

Revision ID: e0d4607d225e
Revises: 3875d77f86f8
Create Date: 2021-12-11 13:14:25.518934

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func



# revision identifiers, used by Alembic.
revision = 'e0d4607d225e'
down_revision = '3875d77f86f8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'claims',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('ticket_id', sa.Integer, ForeignKey('tickets.id')),
        sa.Column('client_id', sa.Integer),
        sa.Column('created_at', sa.DateTime, server_default=func.now()),
    )

    op.create_unique_constraint('pk_claims_client_id_ticket_id', 'claims', ['ticket_id', 'client_id'])


def downgrade():
    op.drop_table('claims')
