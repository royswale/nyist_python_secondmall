"""empty message

Revision ID: bf70119cb34d
Revises: efa27198c06c
Create Date: 2018-10-12 16:26:53.534945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf70119cb34d'
down_revision = 'efa27198c06c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('identity', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('scores', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'scores')
    op.drop_column('user', 'identity')
    op.drop_column('user', 'create_time')
    # ### end Alembic commands ###
