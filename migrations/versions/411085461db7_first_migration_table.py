"""'first_migration_table'

Revision ID: 411085461db7
Revises: 36a9621f1b96
Create Date: 2019-12-16 15:25:07.524112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '411085461db7'
down_revision = '36a9621f1b96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('is_read', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'is_read')
    # ### end Alembic commands ###
