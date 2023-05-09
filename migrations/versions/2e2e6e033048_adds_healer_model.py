"""adds Healer model

Revision ID: 2e2e6e033048
Revises: 6c2bb590df8b
Create Date: 2023-05-09 10:00:12.699651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e2e6e033048'
down_revision = '6c2bb590df8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('healer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('healer')
    # ### end Alembic commands ###
