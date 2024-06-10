"""

Revision ID: cbc51572042b
Revises: 2c336783489a
Create Date: 2024-06-08 18:04:27.759095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cbc51572042b'
down_revision: Union[str, None] = '2c336783489a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('goals', 'todo',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('goals', 'nottodo',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('goals', 'nottodo',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('goals', 'todo',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###