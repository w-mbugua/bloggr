"""fixing backrefsvi

Revision ID: 84945a3715af
Revises: 9f744d8229dd
Create Date: 2021-05-02 06:38:32.310300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84945a3715af'
down_revision = '9f744d8229dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('blogs_writer_id_fkey', 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'writer_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('writer_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('blogs_writer_id_fkey', 'blogs', 'writers', ['writer_id'], ['id'])
    # ### end Alembic commands ###