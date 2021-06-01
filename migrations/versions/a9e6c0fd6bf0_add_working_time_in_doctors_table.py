"""Add working_time in Doctors table.

Revision ID: a9e6c0fd6bf0
Revises: 
Create Date: 2021-05-22 22:14:48.423849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9e6c0fd6bf0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctor', sa.Column('working_time', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('doctor', 'working_time')
    # ### end Alembic commands ###