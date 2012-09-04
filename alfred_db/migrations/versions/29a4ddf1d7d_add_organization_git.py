"""Add Repository.github_id

Revision ID: 29a4ddf1d7d
Revises: 29a56dc34a2b
Create Date: 2012-09-04 00:58:35.728789
"""

# revision identifiers, used by Alembic.
revision = '29a4ddf1d7d'
down_revision = '29a56dc34a2b'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(
        'repositories', 
        sa.Column('github_id', sa.Integer(), nullable=False, unique=True)
    )


def downgrade():
    op.drop_column('repositories', 'github_id')
