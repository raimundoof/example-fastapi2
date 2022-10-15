"""add content column to posts table

Revision ID: 595badf01892
Revises: 286ea3277d35
Create Date: 2022-10-10 21:32:23.762084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '595badf01892'
down_revision = '286ea3277d35'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
