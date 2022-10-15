"""create posts table

Revision ID: 286ea3277d35
Revises: 
Create Date: 2022-10-10 20:53:50.683073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '286ea3277d35'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
