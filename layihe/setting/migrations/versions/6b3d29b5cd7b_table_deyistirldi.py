"""table deyistirldi

Revision ID: 6b3d29b5cd7b
Revises: aae079d0d52a
Create Date: 2021-03-16 11:18:39.573995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b3d29b5cd7b'
down_revision = 'aae079d0d52a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('authors', 'img')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authors', sa.Column('img', sa.VARCHAR(length=50), nullable=True))
    # ### end Alembic commands ###
