"""Add report and fix

Revision ID: 1c2314efe59
Revises: 42291aba125
Create Date: 2012-08-29 19:58:57.516379
"""

# revision identifiers, used by Alembic.
revision = '1c2314efe59'
down_revision = '42291aba125'


from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('reports',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('error', sa.Text(), nullable=False),
        sa.Column('finished_on', sa.DateTime(), nullable=True),
        sa.Column('commit_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['commit_id'], ['commits.id']),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table('fixes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('description_html', sa.Text(), nullable=False),
        sa.Column('path', sa.String(), nullable=False),
        sa.Column('line', sa.Integer(), nullable=False),
        sa.Column('source', sa.Text(), nullable=False),
        sa.Column('solution', sa.Text(), nullable=True),
        sa.Column('report_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['report_id'], ['reports.id']),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('fixes')
    op.drop_table('reports')
