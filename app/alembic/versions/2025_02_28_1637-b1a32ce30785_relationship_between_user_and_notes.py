"""relationship between user and notes

Revision ID: b1a32ce30785
Revises: 19f71d675e2a
Create Date: 2025-02-28 16:37:52.019543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1a32ce30785'
down_revision: Union[str, None] = '19f71d675e2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('notes', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key("fk_notes_user_id", 'notes', 'user', ['user_id'], ['id'], ondelete='cascade')


def downgrade() -> None:
    op.drop_constraint("fk_notes_user_id", 'notes', type_='foreignkey')
    op.drop_column('notes', 'user_id')
