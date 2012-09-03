"""Add organizations table

Revision ID: 393a48ab5fc7
Revises: 5245d0b46f8
Create Date: 2012-09-02 12:24:24.633737
"""

# revision identifiers, used by Alembic.
revision = '393a48ab5fc7'
down_revision = '5245d0b46f8'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('organizations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('github_id', sa.Integer(), nullable=False),
        sa.Column('login', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('github_id'),
        sa.UniqueConstraint('login')
    )


def downgrade():
    op.drop_table('organizations')
