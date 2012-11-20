"""Add sync fields

Revision ID: 53e7eb28395
Revises: 1db7a220826e
Create Date: 2012-11-20 10:36:45.791392
"""

# revision identifiers, used by Alembic.
revision = '53e7eb28395'
down_revision = '1db7a220826e'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('users',sa.Column('is_syncing', sa.Boolean(),
                                    nullable=False, server_default='0'))
    op.add_column('users', sa.Column('last_synced_at',
                                     sa.DateTime(timezone=True),
                                     nullable=True))


def downgrade():
    op.drop_column('users', 'last_synced_at')
    op.drop_column('users', 'is_syncing')
