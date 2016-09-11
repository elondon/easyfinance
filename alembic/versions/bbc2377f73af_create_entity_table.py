"""create entity table

Revision ID: bbc2377f73af
Revises: d6092d4b4c56
Create Date: 2016-09-10 11:02:46.652715

"""

# revision identifiers, used by Alembic.
from sqlalchemy.orm import relationship

revision = 'bbc2377f73af'
down_revision = 'd6092d4b4c56'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'entity',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.String(250), nullable=False),
        sa.Column('description', sa.Unicode),
    )


def downgrade():
    op.drop_table('entity')
