"""Add github hook_id field for Repository

Revision ID: 3bfc33bc8291
Revises: bc8b4de7986
Create Date: 2012-11-23 12:11:53.658787
"""

# revision identifiers, used by Alembic.
revision = '3bfc33bc8291'
down_revision = 'bc8b4de7986'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(
        'repositories',
        sa.Column('hook_id', sa.String(), nullable=True)
    )


def downgrade():
    op.drop_column('repositories', 'hook_id')
