"""Added name to List Header

Revision ID: aaeaa3bc13aa
Revises: 9ce89dbbcee7
Create Date: 2018-10-20 11:13:54.508802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aaeaa3bc13aa'
down_revision = '9ce89dbbcee7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shopping_list_header', sa.Column('name', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shopping_list_header', 'name')
    # ### end Alembic commands ###
