"""Add permissions

Revision ID: 29a56dc34a2b
Revises: 4fdf1059c4ba
Create Date: 2012-09-02 14:06:24.088307
"""

# revision identifiers, used by Alembic.
revision = '29a56dc34a2b'
down_revision = '5245d0b46f8'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('permissions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('repository_id', sa.Integer(), nullable=False),
        sa.Column('admin', sa.Boolean(), nullable=False),
        sa.Column('push', sa.Boolean(), nullable=False),
        sa.Column('pull', sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ['repository_id'], ['repositories.id'], ondelete='CASCADE',
        ),
        sa.ForeignKeyConstraint(
            ['user_id'], ['users.id'], ondelete='CASCADE',
        ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('permissions')
