"""Remove repository unique constraints

Revision ID: 35952c71f828
Revises: 29a4ddf1d7d
Create Date: 2012-09-04 09:40:54.205227
"""

# revision identifiers, used by Alembic.
revision = '35952c71f828'
down_revision = '29a4ddf1d7d'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_constraint("uq_owner_type_owner_name", "repositories")


def downgrade():
    op.create_unique_constraint(
        "uq_owner_type_owner_name",
        "repositories",
        ["owner_type", "owner_name"],
    )
