"""acces token

Revision ID: 19f71d675e2a
Revises: 2f4a6533edc4
Create Date: 2025-02-26 22:08:25.277591

"""
from typing import Sequence, Union

import fastapi_users_db_sqlalchemy
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19f71d675e2a'
down_revision: Union[str, None] = '2f4a6533edc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('accesstoken',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=43), nullable=False),
    sa.Column('created_at', fastapi_users_db_sqlalchemy.generics.TIMESTAMPAware(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('token')
    )
    op.create_index(op.f('ix_accesstoken_created_at'), 'accesstoken', ['created_at'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_accesstoken_created_at'), table_name='accesstoken')
    op.drop_table('accesstoken')
