"""empty message

Revision ID: 3d5f0af5558a
Revises: 982bc33092e4
Create Date: 2024-05-11 16:35:56.373995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d5f0af5558a'
down_revision: Union[str, None] = '982bc33092e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topic', sa.Column('cost', sa.Integer(), server_default=sa.text('5'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('topic', 'cost')
    # ### end Alembic commands ###
