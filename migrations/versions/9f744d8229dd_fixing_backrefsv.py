"""fixing backrefsv

Revision ID: 9f744d8229dd
Revises: acca8bee74fc
Create Date: 2021-05-02 06:37:43.335357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f744d8229dd'
down_revision = 'acca8bee74fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('writer_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blogs', 'writers', ['writer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'writer_id')
    # ### end Alembic commands ###
