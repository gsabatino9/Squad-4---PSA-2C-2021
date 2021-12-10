"""create table product

Revision ID: cbb3443cbcf8
Revises: 
Create Date: 2021-12-10 20:20:03.675318

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = 'cbb3443cbcf8'
down_revision = None
branch_labels = None
depends_on = None

PRODUCTS_NAMES = ['PSA_ORM', 'PSA_BI', 'PSA_CRM']


def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('version', sa.Integer),
        sa.Column('name', sa.String),
        sa.Column('created_at', sa.DateTime, server_default=func.now()),
    )

    for i in range(5):
        for name in PRODUCTS_NAMES:
            op.execute("INSERT INTO products(name, version) VALUES ('{}', {})".format(name, i))

def downgrade():
    op.drop_table('products')