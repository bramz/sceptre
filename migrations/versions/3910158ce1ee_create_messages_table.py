"""
create messages table

Revision ID: 3910158ce1ee
Revises: 165b9ea3ac12
Create Date: 2020-08-15 10:29:38.796976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3910158ce1ee'
down_revision = '165b9ea3ac12'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'messages',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('dtime', sa.DateTime),
        sa.Column('guildid', sa.Text),
        sa.Column('guildname', sa.Text),
        sa.Column('userid', sa.Text),
        sa.Column('usernmae', sa.Text),
        sa.Column('content', sa.Text),
    )

def downgrade():
    pass
