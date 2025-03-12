"""empty message

Revision ID: 8a33542ec71a
Revises: 7f0a61684030
Create Date: 2025-03-12 17:10:24.630716

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a33542ec71a'
down_revision: Union[str, None] = '7f0a61684030'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('user', sa.Column('premium_end_date', sa.DateTime(), nullable=True))


def downgrade() -> None:
    op.drop_column('user', 'premium_end_date')
