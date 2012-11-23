"""Initial schema

Revision ID: 20dbf29885f4
Revises: None
Create Date: 2012-11-23 15:47:25.244212
"""

# revision identifiers, used by Alembic.
revision = '20dbf29885f4'
down_revision = None


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('github_id', sa.Integer, nullable=False),
        sa.Column('github_access_token', sa.String, nullable=False),
        sa.Column('login', sa.String, nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('apitoken', sa.String, nullable=False),
        sa.Column('is_syncing', sa.Boolean, nullable=False),
        sa.Column('last_synced_at', sa.DateTime(timezone=True)),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('apitoken'),
        sa.UniqueConstraint('github_id'),
        sa.UniqueConstraint('login'),
    )
    op.create_table('organizations',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('github_id', sa.Integer, nullable=False),
        sa.Column('login', sa.String, nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('github_id'),
        sa.UniqueConstraint('login'),
    )
    op.create_table('repositories',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('github_id', sa.Integer, nullable=False),
        sa.Column('url', sa.String, nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('token', sa.String, nullable=False),
        sa.Column('hook_id', sa.String, nullable=True),
        sa.Column('owner_name', sa.String),
        sa.Column('owner_type',
            sa.Enum('organization', 'user', name='repositories_owner_type'),
            nullable=False,
        ),
        sa.Column('owner_id', sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('github_id'),
    )
    op.create_table('memberships',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('organization_id', sa.Integer),
        sa.Column('user_id', sa.Integer),
        sa.ForeignKeyConstraint(['organization_id'], ['organizations.id']),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table('pushes',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('ref', sa.String, nullable=False),
        sa.Column('compare_url', sa.String, nullable=False),
        sa.Column('commit_hash', sa.String, nullable=False),
        sa.Column('commit_message', sa.Text, nullable=False),
        sa.Column('committer_name', sa.String, nullable=False),
        sa.Column('committer_email', sa.String, nullable=False),
        sa.Column('repository_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['repository_id'], ['repositories.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table('permissions',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('repository_id', sa.Integer, nullable=False),
        sa.Column('admin', sa.Boolean, nullable=False),
        sa.Column('push', sa.Boolean, nullable=False),
        sa.Column('pull', sa.Boolean, nullable=False),
        sa.ForeignKeyConstraint(['repository_id'], ['repositories.id']),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table('reports',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('error', sa.Text),
        sa.Column('created_on', sa.DateTime(timezone=True), nullable=False),
        sa.Column('finished_on', sa.DateTime(timezone=True)),
        sa.Column('push_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['push_id'], ['pushes.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table('fixes',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('description_html', sa.Text, nullable=False),
        sa.Column('path', sa.String, nullable=False),
        sa.Column('line', sa.Integer, nullable=False),
        sa.Column('source', sa.Text, nullable=False),
        sa.Column('solution', sa.Text, nullable=False),
        sa.Column('report_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['report_id'], ['reports.id']),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('fixes')
    op.drop_table('reports')
    op.drop_table('permissions')
    op.drop_table('pushes')
    op.drop_table('memberships')
    op.drop_table('repositories')
    op.drop_table('organizations')
    op.drop_table('users')

    sa.Enum(name='repositories_owner_type').drop(
        bind=op.get_bind(),
        checkfirst=False,
    )
