"""empty message

Revision ID: 8e99f87830b4
Revises: fcb4a534aa37
Create Date: 2020-05-14 14:33:02.333064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e99f87830b4'
down_revision = 'fcb4a534aa37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tournament_invitations_association',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('tournament_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tournament_id'], ['tournaments.id'], name=op.f('fk_tournament_invitations_association_tournament_id_tournaments')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_tournament_invitations_association_user_id_users')),
    sa.PrimaryKeyConstraint('user_id', 'tournament_id', name=op.f('pk_tournament_invitations_association'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tournament_invitations_association')
    # ### end Alembic commands ###
