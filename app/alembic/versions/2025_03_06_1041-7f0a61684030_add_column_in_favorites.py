"""add column in_favorites

Revision ID: 7f0a61684030
Revises: b1a32ce30785
Create Date: 2025-03-06 10:41:36.747282

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f0a61684030'
down_revision: Union[str, None] = 'b1a32ce30785'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('notes', sa.Column('in_favorites', sa.Boolean(), nullable=False, server_default="false"))


def downgrade() -> None:
    op.drop_column('notes', 'in_favorites')
