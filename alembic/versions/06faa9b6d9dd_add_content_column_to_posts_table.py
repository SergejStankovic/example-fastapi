"""add content column to posts table

Revision ID: 06faa9b6d9dd
Revises: 3d7aa363dfeb
Create Date: 2022-02-21 22:13:36.496922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06faa9b6d9dd'
down_revision = '3d7aa363dfeb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
