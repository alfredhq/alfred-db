"""Add start date to Push

Revision ID: 19489c712d8b
Revises: 40f0d23c8757
Create Date: 2012-11-29 22:05:55.927537
"""

# revision identifiers, used by Alembic.
revision = '19489c712d8b'
down_revision = '40f0d23c8757'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('pushes',
        sa.Column('started_at', sa.DateTime(timezone=True)),
    )


def downgrade():
    op.drop_column('pushes', 'started_at')
