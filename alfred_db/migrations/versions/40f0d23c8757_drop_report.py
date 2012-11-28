"""Drop reports

Revision ID: 40f0d23c8757
Revises: 2f253c13a2f5
Create Date: 2012-11-28 14:03:53.840575
"""

# revision identifiers, used by Alembic.
revision = '40f0d23c8757'
down_revision = '2f253c13a2f5'


from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    op.drop_column('fixes', 'report_id')
    op.drop_table('reports')


def downgrade():
    op.add_column('fixes', sa.Column(u'report_id', sa.INTEGER, nullable=False))
    op.create_table(u'reports',
        sa.Column('id',
            sa.INTEGER,
            server_default="nextval('reports_id_seq'::regclass)",
            nullable=False,
        ),
        sa.Column('error', sa.TEXT, nullable=True),
        sa.Column('created_on',
            postgresql.TIMESTAMP(timezone=True),
            nullable=False,
        ),
        sa.Column('finished_on',
            postgresql.TIMESTAMP(timezone=True),
        ),
        sa.Column('push_id', sa.INTEGER, nullable=False),
        sa.ForeignKeyConstraint(
            ['push_id'],
            ['pushes.id'],
            name='reports_push_id_fkey',
        ),
        sa.PrimaryKeyConstraint('id', name='reports_pkey')
    )
