"""add email to user table

Revision ID: f4e7557866d4
Revises: aebd5259866a
Create Date: 2016-09-18 11:40:46.433466

"""

# revision identifiers, used by Alembic.
revision = 'f4e7557866d4'
down_revision = 'aebd5259866a'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('user', sa.Column('email', sa.String(250)))


def downgrade():
    pass
