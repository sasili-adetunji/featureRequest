"""empty message

Revision ID: a18e0eef9896
Revises: 
Create Date: 2018-11-13 09:45:25.545484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a18e0eef9896'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('features',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('client', sa.Enum('CLIENT_A', 'CLIENT_B', 'CLIENT_C', name='clienttype'), nullable=True),
    sa.Column('client_priority', sa.Integer(), nullable=True),
    sa.Column('target_date', sa.DateTime(), nullable=True),
    sa.Column('product_area', sa.Enum('POLICIES', 'BILLING', 'CLAIMS', 'REPORTS', name='productareatype'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('features')
    # ### end Alembic commands ###
