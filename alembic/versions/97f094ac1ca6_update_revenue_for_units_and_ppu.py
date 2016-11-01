"""update_revenue_for_units_and_ppu

Revision ID: 97f094ac1ca6
Revises: 5175c305b5e4
Create Date: 2016-10-31 14:45:10.749167

"""

# revision identifiers, used by Alembic.
revision = '97f094ac1ca6'
down_revision = '5175c305b5e4'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_column('revenue', 'value')
    op.drop_column('revenue', 'name')
    op.drop_column('revenue', 'description')
    op.add_column('revenue', sa.Column('unit_cost', sa.BigInteger, nullable=False))
    op.add_column('revenue', sa.Column('unit_count', sa.BigInteger, nullable=False))
    op.add_column('revenue', sa.Column('unit_name', sa.String(250), nullable=False))
    op.add_column('revenue', sa.Column('unit_description', sa.Unicode, nullable=True))


def downgrade():
    pass
