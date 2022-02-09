"""create permissions table

Revision ID: de632fd4ca90
Revises: 
Create Date: 2022-02-09 01:03:56.346766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de632fd4ca90'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'permissions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('level', sa.Integer),
    )


def downgrade():
    pass
