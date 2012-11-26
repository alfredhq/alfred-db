"""Email can be null

Revision ID: 1f9dc3c5c274
Revises: 20dbf29885f4
Create Date: 2012-11-26 21:16:38.552067
"""

# revision identifiers, used by Alembic.
revision = '1f9dc3c5c274'
down_revision = '20dbf29885f4'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('pushes', u'committer_email', 
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    op.alter_column('users', u'email', 
                    existing_type=sa.VARCHAR(),
                    nullable=True)


def downgrade():
    op.alter_column('users', u'email',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.alter_column('pushes', u'committer_email',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
