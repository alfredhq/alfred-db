"""Add user

Revision ID: 42291aba125
Revises: 5a30bfc89b3
Create Date: 2012-08-28 20:42:37.260384
"""

# revision identifiers, used by Alembic.
revision = '42291aba125'
down_revision = '5a30bfc89b3'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('github_id', sa.Integer(), nullable=False),
        sa.Column('github_access_token', sa.String(), nullable=False),
        sa.Column('login', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('github_id'),
        sa.UniqueConstraint('login'),
    )


def downgrade():
    op.drop_table('users')
