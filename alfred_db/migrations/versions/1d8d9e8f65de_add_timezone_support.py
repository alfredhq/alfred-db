"""Add timezone support

Revision ID: 1d8d9e8f65de
Revises: 498d6689a216
Create Date: 2012-11-18 17:21:02.046260
"""

# revision identifiers, used by Alembic.
revision = '1d8d9e8f65de'
down_revision = '498d6689a216'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('reports', 'finished_on',
        existing_type=sa.DateTime(),
        type_=sa.DateTime(timezone=True),
    )


def downgrade():
    op.alter_column('reports', 'finished_on',
        existing_type=sa.Datetime(timezone=True),
        type_=sa.DateTime(),
    )
