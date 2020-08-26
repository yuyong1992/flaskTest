"""empty message

Revision ID: 871ff3027b9d
Revises: 
Create Date: 2020-08-26 17:49:40.886836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '871ff3027b9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nick_name', sa.String(length=20), nullable=True),
    sa.Column('mobile', sa.String(length=11), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('real_name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('mobile'),
    sa.UniqueConstraint('nick_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
