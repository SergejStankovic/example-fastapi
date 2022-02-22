"""add user table

Revision ID: 2b7e0969bf11
Revises: 06faa9b6d9dd
Create Date: 2022-02-21 22:25:32.528066

"""
from re import T
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b7e0969bf11'
down_revision = '06faa9b6d9dd'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
