"""create revenue costs opex tables

Revision ID: 3989420a3fbb
Revises: bbc2377f73af
Create Date: 2016-09-10 12:24:22.267616

"""

# revision identifiers, used by Alembic.
from sqlalchemy import ForeignKey

revision = '3989420a3fbb'
down_revision = 'bbc2377f73af'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'revenue',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('entity_id', sa.BigInteger, ForeignKey('entity.id')),
        sa.Column('name', sa.String(250), nullable=False),
        sa.Column('description', sa.Unicode),
        sa.Column('value', sa.Float, nullable=False)
    )

    op.create_table(
        'cost',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('entity_id', sa.BigInteger, ForeignKey('entity.id')),
        sa.Column('name', sa.String(250), nullable=False),
        sa.Column('description', sa.Unicode),
        sa.Column('value', sa.Float, nullable=False)
    )

    op.create_table(
        'operating_expenses',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('entity_id', sa.BigInteger, ForeignKey('entity.id')),
        sa.Column('name', sa.String(250), nullable=False),
        sa.Column('description', sa.Unicode),
        sa.Column('value', sa.Float, nullable=False)
    )


def downgrade():
    op.drop_table('revenue')
    op.drop_table('cost')
    op.drop_table('operating_expenses')
