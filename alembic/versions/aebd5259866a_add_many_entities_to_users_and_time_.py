"""add many entities to users and time stamp columns to tables

Revision ID: aebd5259866a
Revises: 1df0b380fc68
Create Date: 2016-09-12 19:52:56.205701

"""

# revision identifiers, used by Alembic.
from sqlalchemy import TIMESTAMP
from sqlalchemy import func

revision = 'aebd5259866a'
down_revision = '1df0b380fc68'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('user', sa.Column('updated_at', TIMESTAMP, server_default=func.now()))
    op.add_column('user', sa.Column('created_at', TIMESTAMP, server_default=func.now()))

    op.add_column('entity', sa.Column('updated_at', TIMESTAMP, server_default=func.now()))
    op.add_column('entity', sa.Column('created_at', TIMESTAMP, server_default=func.now()))
    op.add_column('entity', sa.Column('user_id', sa.BigInteger))

    op.add_column('revenue', sa.Column('updated_at', TIMESTAMP, server_default=func.now()))
    op.add_column('revenue', sa.Column('created_at', TIMESTAMP, server_default=func.now()))

    op.add_column('operating_expense', sa.Column('updated_at', TIMESTAMP, server_default=func.now()))
    op.add_column('operating_expense', sa.Column('created_at', TIMESTAMP, server_default=func.now()))

def downgrade():
    pass
