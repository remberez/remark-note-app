"""create note table

Revision ID: 52e451c86343
Revises: 
Create Date: 2025-02-23 19:19:12.053020

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52e451c86343'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('notes',
    sa.Column('title', sa.String(length=25), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('notes')
