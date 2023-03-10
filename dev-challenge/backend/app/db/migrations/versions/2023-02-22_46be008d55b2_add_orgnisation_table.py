"""Add Orgnisation Table

Revision ID: 46be008d55b2
Revises: 
Create Date: 2023-02-22 00:59:02.844120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46be008d55b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Employee_id'), 'Employee', ['id'], unique=False)
    op.create_table('Organisation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('postcode', sa.String(), nullable=True),
    sa.Column('contact_name', sa.String(), nullable=True),
    sa.Column('contact_phone', sa.String(), nullable=True),
    sa.Column('contact_email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Organisation_id'), 'Organisation', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Organisation_id'), table_name='Organisation')
    op.drop_table('Organisation')
    op.drop_index(op.f('ix_Employee_id'), table_name='Employee')
    op.drop_table('Employee')
    # ### end Alembic commands ###
