"""Add Departments

Revision ID: a83f4b6a3743
Revises: 46be008d55b2
Create Date: 2023-02-22 01:05:51.542881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a83f4b6a3743'
down_revision = '46be008d55b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Organisation', sa.Column('departments', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Organisation', 'departments')
    # ### end Alembic commands ###
