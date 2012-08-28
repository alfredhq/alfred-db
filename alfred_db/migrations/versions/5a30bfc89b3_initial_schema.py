"""Initial schema

Revision ID: 5a30bfc89b3
Revises: None
Create Date: 2012-08-28 17:02:11.124841
"""

# revision identifiers, used by Alembic.
revision = '5a30bfc89b3'
down_revision = None


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('repositories',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('url', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('user', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user','name'),
    )
    op.create_table('commits',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('hash', sa.String(), nullable=False),
        sa.Column('ref', sa.String(), nullable=False),
        sa.Column('compare_url', sa.String(), nullable=False),
        sa.Column('committer_name', sa.String(), nullable=False),
        sa.Column('committer_email', sa.String(), nullable=False),
        sa.Column('message', sa.Text(), nullable=False),
        sa.Column('repository_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['repository_id'], ['repositories.id']),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('commits')
    op.drop_table('repositories')
