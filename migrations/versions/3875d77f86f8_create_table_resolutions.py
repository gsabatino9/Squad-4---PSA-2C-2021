"""create table resolutions

Revision ID: 3875d77f86f8
Revises: 1419d33409e8
Create Date: 2021-12-11 13:14:19.993357

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func



# revision identifiers, used by Alembic.
revision = '3875d77f86f8'
down_revision = '1419d33409e8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'resolutions',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('ticket_id', sa.Integer, ForeignKey('tickets.id')),
        sa.Column('task_id', sa.Integer),
        sa.Column('created_at', sa.DateTime, server_default=func.now()),
    )

    op.create_unique_constraint('pk_resolutions_task_id_ticket_id', 'resolutions', ['ticket_id', 'task_id'])


def downgrade():
    op.drop_table('claims')