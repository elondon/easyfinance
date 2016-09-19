"""add timestamps to cost

Revision ID: 5175c305b5e4
Revises: f4e7557866d4
Create Date: 2016-09-18 19:56:39.406926

"""

# revision identifiers, used by Alembic.
from sqlalchemy import TIMESTAMP
from sqlalchemy import func

revision = '5175c305b5e4'
down_revision = 'f4e7557866d4'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('cost', sa.Column('updated_at', TIMESTAMP, server_default=func.now()))
    op.add_column('cost', sa.Column('created_at', TIMESTAMP, server_default=func.now()))


def downgrade():
    pass
