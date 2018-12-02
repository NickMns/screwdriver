"""empty message

Revision ID: f4506f36abcc
Revises: 6ced42f5ecf2
Create Date: 2018-12-02 15:52:08.626662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4506f36abcc'
down_revision = '6ced42f5ecf2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Devices', sa.Column('Dev_Created', sa.DateTime(), nullable=True))
    op.drop_column('Devices', 'Dev_Creator')
	op.execute('ALTER TABLE "Devices" ALTER COLUMN "Dev_Model_Year" TYPE character varying COLLATE pg_catalog."default"')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Devices', sa.Column('Dev_Creator', sa.DATE(), autoincrement=False, nullable=True))
    op.drop_column('Devices', 'Dev_Created')
    # ### end Alembic commands ###
