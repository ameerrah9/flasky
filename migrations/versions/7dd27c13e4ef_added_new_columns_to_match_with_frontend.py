"""added new columns to match with frontend

Revision ID: 7dd27c13e4ef
Revises: 
Create Date: 2022-12-19 03:44:06.300575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7dd27c13e4ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caretaker',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dog',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('breed', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('cuteness', sa.Integer(), nullable=True),
    sa.Column('petCount', sa.Integer(), nullable=True),
    sa.Column('caretaker_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['caretaker_id'], ['caretaker.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dog')
    op.drop_table('caretaker')
    # ### end Alembic commands ###
