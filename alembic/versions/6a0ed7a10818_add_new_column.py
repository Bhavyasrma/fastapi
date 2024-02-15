"""add new column

Revision ID: 6a0ed7a10818
Revises: 2ab1b2306c1a
Create Date: 2024-02-15 20:25:24.022624

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a0ed7a10818'
down_revision: Union[str, None] = '2ab1b2306c1a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
