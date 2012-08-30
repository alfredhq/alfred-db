"""Nullable report error

Revision ID: 5245d0b46f8
Revises: 1c2314efe59
Create Date: 2012-08-30 20:31:20.454564
"""

# revision identifiers, used by Alembic.
revision = '5245d0b46f8'
down_revision = '1c2314efe59'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('reports', 'error',
        existing_type=sa.TEXT(),
        nullable=True,
    )


def downgrade():
    op.alter_column('reports', 'error',
        existing_type=sa.TEXT(),
        nullable=False,
    )
