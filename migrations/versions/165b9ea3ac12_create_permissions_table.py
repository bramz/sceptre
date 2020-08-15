"""create permissions table

Revision ID: 165b9ea3ac12
Revises: 
Create Date: 2020-08-15 10:29:12.355464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '165b9ea3ac12'
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
