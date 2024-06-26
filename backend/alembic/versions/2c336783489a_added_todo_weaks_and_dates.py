"""added todo weaks and dates

Revision ID: 2c336783489a
Revises: df97648f328d
Create Date: 2024-06-07 22:16:14.666310

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c336783489a'
down_revision: Union[str, None] = 'df97648f328d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goals', sa.Column('start_date', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True))
    op.add_column('goals', sa.Column('end_date', sa.DateTime(), server_default=sa.text('NOW()'), nullable=True))
    op.add_column('goals', sa.Column('data_format', sa.String(), server_default='weaks', nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goals', 'data_format')
    op.drop_column('goals', 'end_date')
    op.drop_column('goals', 'start_date')
    # ### end Alembic commands ###
