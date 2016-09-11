"""rename op expenses to op expense

Revision ID: 1df0b380fc68
Revises: 3989420a3fbb
Create Date: 2016-09-10 13:23:11.509225

"""

# revision identifiers, used by Alembic.
revision = '1df0b380fc68'
down_revision = '3989420a3fbb'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.rename_table('operating_expenses', 'operating_expense')


def downgrade():
    op.rename_table('operating_expense', 'operating_expenses')
