"""add user table

Revision ID: 86cf093c3a8b
Revises: 595badf01892
Create Date: 2022-10-10 21:41:09.903097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86cf093c3a8b'
down_revision = '595badf01892'
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
