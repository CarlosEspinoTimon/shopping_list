"""empty message

Revision ID: 9413c8990be0
Revises: ab68e7ef0a05
Create Date: 2018-07-10 06:37:55.364549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9413c8990be0'
down_revision = 'ab68e7ef0a05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('format', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_article_name'), 'article', ['name'], unique=True)
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_name'), 'category', ['name'], unique=True)
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_name'), 'company', ['name'], unique=True)
    op.create_table('sub_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sub_category_name'), 'sub_category', ['name'], unique=True)
    op.create_table('supermarket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('lat_location', sa.Float(), nullable=True),
    sa.Column('lon_location', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_supermarket_name'), 'supermarket', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_supermarket_name'), table_name='supermarket')
    op.drop_table('supermarket')
    op.drop_index(op.f('ix_sub_category_name'), table_name='sub_category')
    op.drop_table('sub_category')
    op.drop_index(op.f('ix_company_name'), table_name='company')
    op.drop_table('company')
    op.drop_index(op.f('ix_category_name'), table_name='category')
    op.drop_table('category')
    op.drop_index(op.f('ix_article_name'), table_name='article')
    op.drop_table('article')
    # ### end Alembic commands ###