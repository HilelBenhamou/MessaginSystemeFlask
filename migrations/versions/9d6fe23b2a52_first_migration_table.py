"""'first_migration_table'

Revision ID: 9d6fe23b2a52
Revises: b67ca2dbb551
Create Date: 2019-12-15 23:16:02.429130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d6fe23b2a52'
down_revision = 'b67ca2dbb551'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('receive_by', sa.Integer(), nullable=True))
    op.add_column('messages', sa.Column('sent_by', sa.Integer(), nullable=True))
    op.drop_constraint('messages_receiver_fkey', 'messages', type_='foreignkey')
    op.drop_constraint('messages_sender_fkey', 'messages', type_='foreignkey')
    op.create_foreign_key(None, 'messages', 'users', ['receive_by'], ['user_id'])
    op.create_foreign_key(None, 'messages', 'users', ['sent_by'], ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.create_foreign_key('messages_sender_fkey', 'messages', 'users', ['sender'], ['user_id'])
    op.create_foreign_key('messages_receiver_fkey', 'messages', 'users', ['receiver'], ['user_id'])
    op.drop_column('messages', 'sent_by')
    op.drop_column('messages', 'receive_by')
    # ### end Alembic commands ###
