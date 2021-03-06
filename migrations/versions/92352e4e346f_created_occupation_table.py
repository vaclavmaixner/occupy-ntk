"""Created occupation table

Revision ID: 92352e4e346f
Revises: 
Create Date: 2019-12-27 12:54:55.626773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92352e4e346f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('occupation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('floor_6', sa.Integer(), nullable=True),
    sa.Column('floor_5', sa.Integer(), nullable=True),
    sa.Column('floor_4', sa.Integer(), nullable=True),
    sa.Column('floor_3', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_occupation_timestamp'), 'occupation', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_occupation_timestamp'), table_name='occupation')
    op.drop_table('occupation')
    # ### end Alembic commands ###
