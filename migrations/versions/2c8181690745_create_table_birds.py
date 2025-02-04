"""create table birds

Revision ID: 2c8181690745
Revises: 
Create Date: 2024-07-08 07:55:28.123219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c8181690745'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('birds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('birds')
    # ### end Alembic commands ###
