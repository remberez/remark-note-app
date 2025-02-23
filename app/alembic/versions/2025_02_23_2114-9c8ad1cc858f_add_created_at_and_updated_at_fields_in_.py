"""add created_at and updated_at fields in note

Revision ID: 9c8ad1cc858f
Revises: 52e451c86343
Create Date: 2025-02-23 21:14:44.790258

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c8ad1cc858f'
down_revision: Union[str, None] = '52e451c86343'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('notes', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('notes', sa.Column('updated_at', sa.DateTime(), nullable=True))


def downgrade() -> None:
    op.drop_column('notes', 'updated_at')
    op.drop_column('notes', 'created_at')
