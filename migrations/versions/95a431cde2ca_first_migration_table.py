"""'first_migration_table'

Revision ID: 95a431cde2ca
Revises: 3812bfc89299
Create Date: 2019-12-16 12:26:31.022854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95a431cde2ca'
down_revision = '3812bfc89299'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('message_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('sent_by', sa.Integer(), nullable=True),
    sa.Column('receive_by', sa.Integer(), nullable=True),
    sa.Column('sender', sa.String(length=255), nullable=True),
    sa.Column('receiver', sa.String(length=255), nullable=True),
    sa.Column('subject', sa.String(length=5000), nullable=True),
    sa.Column('message', sa.String(length=500000), nullable=True),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['receive_by'], ['users.user_id'], ),
    sa.ForeignKeyConstraint(['sent_by'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('message_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
