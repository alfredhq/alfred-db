"""Native Enum

Revision ID: bc8b4de7986
Revises: 1db7a220826e
Create Date: 2012-11-23 00:52:25.287729
"""

# revision identifiers, used by Alembic.
revision = 'bc8b4de7986'
down_revision = '53e7eb28395'


from alembic import op
from sqlalchemy.sql import table, column, cast
import sqlalchemy as sa


def upgrade():
    native_enum = sa.Enum('organization', 'user',
        name='repositories_owner_type',
        create_type=False,
    )
    native_enum.create(op.get_bind(), checkfirst=False)

    op.alter_column('repositories', 'owner_type', name='owner_type_old')
    op.add_column('repositories', sa.Column('owner_type', native_enum))

    repositories = table('repositories',
        column('owner_type', native_enum),
        column('owner_type_old', sa.String(12)),
    )
    op.execute(repositories.update().values({
        'owner_type': cast(repositories.c.owner_type_old, native_enum),
    }))

    op.drop_column('repositories', 'owner_type_old')
    op.alter_column('repositories', 'owner_type', nullable=False)


def downgrade():
    op.alter_column('repositories', 'owner_type', name='owner_type_old')
    op.add_column('repositories', sa.Column('owner_type', sa.String(12)))

    native_enum = sa.Enum('organization', 'user',
        name='repositories_owner_type',
        create_type=False,
    )
    repositories = table('repositories',
        column('owner_type', sa.String(12)),
        column('owner_type_old', native_enum),
    )
    op.execute(repositories.update().values({
        'owner_type': cast(repositories.c.owner_type_old, sa.String(12)),
    }))

    op.drop_column('repositories', 'owner_type_old')
    native_enum.drop(op.get_bind(), checkfirst=False)
    op.alter_column('repositories', 'owner_type', nullable=False)
