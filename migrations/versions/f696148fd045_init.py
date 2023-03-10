"""Init

Revision ID: f696148fd045
Revises: 
Create Date: 2022-12-12 20:21:14.299670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f696148fd045'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('number_phone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('number_phone')
    )
    op.create_index(op.f('ix_clients_id'), 'clients', ['id'], unique=False)
    op.create_table('firms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('legal_address', sa.String(), nullable=True),
    sa.Column('number_firm', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('number_firm')
    )
    op.create_index(op.f('ix_firms_id'), 'firms', ['id'], unique=False)
    op.create_table('fuels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kind', sa.String(), nullable=True),
    sa.Column('unit', sa.String(), nullable=True),
    sa.Column('price', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_fuels_id'), 'fuels', ['id'], unique=False)
    op.create_table('refuelings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('address_firms', sa.String(), nullable=True),
    sa.Column('firm_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['firm_id'], ['firms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_refuelings_id'), 'refuelings', ['id'], unique=False)
    op.create_table('daily_sales',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_of_sale', sa.String(), nullable=True),
    sa.Column('amount', sa.String(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('refueling_id', sa.Integer(), nullable=True),
    sa.Column('fuel_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['fuel_id'], ['fuels.id'], ),
    sa.ForeignKeyConstraint(['refueling_id'], ['refuelings.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_daily_sales_id'), 'daily_sales', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_daily_sales_id'), table_name='daily_sales')
    op.drop_table('daily_sales')
    op.drop_index(op.f('ix_refuelings_id'), table_name='refuelings')
    op.drop_table('refuelings')
    op.drop_index(op.f('ix_fuels_id'), table_name='fuels')
    op.drop_table('fuels')
    op.drop_index(op.f('ix_firms_id'), table_name='firms')
    op.drop_table('firms')
    op.drop_index(op.f('ix_clients_id'), table_name='clients')
    op.drop_table('clients')
    # ### end Alembic commands ###
