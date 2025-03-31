"""Add User Table

Revision ID: f32f0b0cce54
Revises: 
Create Date: 2025-03-31 16:24:11.343161

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f32f0b0cce54'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
                    sa.Column("username", sa.String(64), nullable=False),
                    sa.Column("email", sa.String(128), nullable=False, unique=True),
                    sa.Column("password", sa.String(128), nullable=False),
                    sa.Column("created_at", sa.DateTime, server_default=sa.func.now(), nullable=False),
                    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
