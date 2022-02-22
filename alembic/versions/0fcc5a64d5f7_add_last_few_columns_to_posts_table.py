"""add last few columns to posts table

Revision ID: 0fcc5a64d5f7
Revises: bb09f6fc553c
Create Date: 2022-02-21 23:20:30.793318

"""
from re import T
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fcc5a64d5f7'
down_revision = 'bb09f6fc553c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
            'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
            ('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
