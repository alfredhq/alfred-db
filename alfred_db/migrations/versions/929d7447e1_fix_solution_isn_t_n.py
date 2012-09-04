"""Fix solution isn't nullable

Revision ID: 929d7447e1
Revises: 29a4ddf1d7d
Create Date: 2012-09-04 11:21:39.090245
"""

# revision identifiers, used by Alembic.
revision = '929d7447e1'
down_revision = '29a4ddf1d7d'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('fixes', 'solution',
        existing_type=sa.TEXT(),
        nullable=False,
    )


def downgrade():
    op.alter_column('fixes', 'solution',
        existing_type=sa.TEXT(),
        nullable=True,
    )
