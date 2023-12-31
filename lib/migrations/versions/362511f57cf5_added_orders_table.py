"""added orders  table

Revision ID: 362511f57cf5
Revises: 095e9eb2f88d
Create Date: 2023-09-05 10:09:18.891342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '362511f57cf5'
down_revision = '095e9eb2f88d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('consumer_name', sa.String(), nullable=False),
    sa.Column('produce_id', sa.Integer(), nullable=False),
    sa.Column('farmer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['farmer_id'], ['farmers.id'], ),
    sa.ForeignKeyConstraint(['produce_id'], ['produce.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    # ### end Alembic commands ###
