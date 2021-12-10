"""create table ticket

Revision ID: 1419d33409e8
Revises: cbb3443cbcf8
Create Date: 2021-12-10 20:20:42.987954

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '1419d33409e8'
down_revision = 'cbb3443cbcf8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tickets',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('product_id', sa.Integer, foreing_key=True),
        sa.Column('product_version', sa.Integer, foreing_key=True),
        sa.Column('employee_id', sa.Integer, foreing_key=True),
        sa.Column('tittle', sa.String),
        sa.Column('description', sa.String),
        sa.Column('created_at', sa.DateTime, server_default=func.now()),
        sa.Column('deleted_at', sa.DateTime, nullable=True),
        sa.Column('ticket_type', sa.String),
        sa.Column('severity', sa.Integer),
        sa.Column('state', sa.String),
        sa.Column('dedicated_hours', sa.Integer, nullable=True)
    )

    op.create_foreign_key('fk_tickets_product_id', 'tickets', 'products', ['product_id', 'product_version'], ['id', 'version'])


def downgrade():
    op.drop_table('tickets')