"""Add token to repository model

Revision ID: 498d6689a216
Revises: 1e19656e384
Create Date: 2012-10-27 20:16:41.605094
"""

# revision identifiers, used by Alembic.
revision = '498d6689a216'
down_revision = '1e19656e384'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('repositories', sa.Column(
        'token', sa.String(), nullable=False
    ))


def downgrade():
    op.drop_column('repositories', 'token')
