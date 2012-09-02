"""Improve repository owner information

Revision ID: 30c0aec2ca06
Revises: 4fdf1059c4ba
Create Date: 2012-09-02 14:45:05.241933
"""

# revision identifiers, used by Alembic.
revision = '30c0aec2ca06'
down_revision = '4fdf1059c4ba'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(
        'repositories',
        sa.Column('owner_type', sa.Enum('organization', 'user', native_enum=False),
                  nullable=False)
    )
    op.add_column(
        'repositories',
        sa.Column('owner_name', sa.String(), nullable=False)
    )
    op.add_column(
        'repositories',
        sa.Column('owner_id', sa.Integer(), nullable=False)
    )
    op.drop_column('repositories', u'user')
    op.create_unique_constraint(
        "uq_owner_type_owner_name",
        "repositories",
        ["owner_type", "owner_name"],
    )


def downgrade():
    op.add_column(
        'repositories',
        sa.Column(u'user', sa.String(), nullable=False)
    )
    op.drop_constraint('uq_owner_type_owner_name', 'repositories', 'unique')
    op.drop_column('repositories', 'owner_id')
    op.drop_column('repositories', 'owner_name')
    op.drop_column('repositories', 'owner_type')
