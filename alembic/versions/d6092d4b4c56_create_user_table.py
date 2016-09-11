"""create user table

Revision ID: d6092d4b4c56
Revises: 
Create Date: 2016-09-10 10:39:07.479291

"""

# revision identifiers, used by Alembic.
revision = 'd6092d4b4c56'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('username', sa.String(250), nullable=False),
        sa.Column('first_name', sa.String(200)),
        sa.Column('last_name', sa.String(200)),
        sa.Column('password', sa.String(250))
    )


def downgrade():
    op.drop_table('user')
