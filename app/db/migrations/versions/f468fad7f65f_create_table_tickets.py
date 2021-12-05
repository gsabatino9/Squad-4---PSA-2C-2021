"""Create table tickets

Revision ID: f468fad7f65f
Revises: 
Create Date: 2021-12-05 17:56:38.482964

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = 'f468fad7f65f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tickets',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('tittle', sa.String),
        sa.Column('description', sa.String),
        sa.Column('created_at', sa.DateTime, server_default=func.now()),
        sa.Column('deleted_at', sa.DateTime, nullable=True)
    )


def downgrade():
    op.drop_table('tickets')
