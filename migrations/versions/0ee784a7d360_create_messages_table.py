"""create messages table

Revision ID: 0ee784a7d360
Revises: de632fd4ca90
Create Date: 2022-02-09 01:04:02.577942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ee784a7d360'
down_revision = 'de632fd4ca90'
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
        sa.Column('username', sa.Text),
        sa.Column('content', sa.Text),
    )

def downgrade():
    pass
