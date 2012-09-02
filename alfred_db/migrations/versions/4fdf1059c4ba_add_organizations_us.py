"""Add organizations-users association table

Revision ID: 4fdf1059c4ba
Revises: 393a48ab5fc7
Create Date: 2012-09-02 12:37:11.785052
"""

# revision identifiers, used by Alembic.
revision = '4fdf1059c4ba'
down_revision = '393a48ab5fc7'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('memberships',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('organization_id', sa.Integer(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['organization_id'], ['organizations.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('memberships')
