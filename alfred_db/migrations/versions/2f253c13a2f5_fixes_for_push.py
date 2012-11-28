"""Fixes for push

Revision ID: 2f253c13a2f5
Revises: 20dbf29885f4
Create Date: 2012-11-23 18:15:59.709799
"""

# revision identifiers, used by Alembic.
revision = '2f253c13a2f5'
down_revision = '1f9dc3c5c274'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('fixes',
        sa.Column('push_id', sa.Integer, nullable=False),
    )
    op.add_column('pushes',
        sa.Column('finished_at', sa.DateTime(timezone=True)),
    )
    op.add_column('pushes',
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    )
    op.add_column('pushes',
        sa.Column('error', sa.Text),
    )

    op.create_foreign_key(
        name='fixes_push_id_fkey',
        source='fixes',
        referent='pushes',
        local_cols=['push_id'],
        remote_cols=['id'],
    )


def downgrade():
    op.drop_constraint('fixes_push_id_fkey', 'fixes')
    op.drop_column('pushes', 'error')
    op.drop_column('pushes', 'created_at')
    op.drop_column('pushes', 'finished_at')
    op.drop_column('fixes', 'push_id')
