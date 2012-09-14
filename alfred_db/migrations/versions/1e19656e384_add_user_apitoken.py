"""Add User apitoken

Revision ID: 1e19656e384
Revises: 35952c71f828
Create Date: 2012-09-14 23:01:12.126982
"""

# revision identifiers, used by Alembic.
revision = '1e19656e384'
down_revision = '35952c71f828'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('users', sa.Column('apitoken', sa.String(),
                                     unique=True, nullable=False))


def downgrade():
    op.drop_column('users', 'apitoken')
