"""add website, seeking_talent and seeking_description to Venue model

Revision ID: 9b825d21d3ee
Revises: 092cf3c88efe
Create Date: 2020-04-24 14:33:37.110936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b825d21d3ee'
down_revision = '092cf3c88efe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('venue', sa.Column('seeking_talent', sa.Boolean(), nullable=False))
    op.add_column('venue', sa.Column('website', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'website')
    op.drop_column('venue', 'seeking_talent')
    op.drop_column('venue', 'seeking_description')
    # ### end Alembic commands ###
