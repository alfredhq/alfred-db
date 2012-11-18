"""Add created_on field to the report

Revision ID: 1db7a220826e
Revises: 1d8d9e8f65de
Create Date: 2012-11-18 21:49:53.056495
"""

# revision identifiers, used by Alembic.
revision = '1db7a220826e'
down_revision = '1d8d9e8f65de'


from alembic import op
from alfred_db.helpers import now
from sqlalchemy.sql import table, column
import sqlalchemy as sa


def upgrade():
    op.add_column('reports', sa.Column('created_on',
        sa.DateTime(timezone=True),
        nullable=True,
    ))

    reports = table('reports',
        column('created_on', sa.DateTime(timezone=True)),
    )
    op.execute(reports.update().values({'created_on': now()}))

    op.alter_column('reports', 'created_on',
        existing_type=sa.DateTime(timezone=True),
        nullable=False,
    )


def downgrade():
    op.drop_column('reports', 'created_on')
