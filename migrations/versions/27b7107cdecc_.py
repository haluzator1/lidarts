"""empty message

Revision ID: 27b7107cdecc
Revises: 8e99f87830b4
Create Date: 2020-05-15 16:57:52.988359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27b7107cdecc'
down_revision = '8e99f87830b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tournament_stage_rounds', sa.Column('name', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tournament_stage_rounds', 'name')
    # ### end Alembic commands ###