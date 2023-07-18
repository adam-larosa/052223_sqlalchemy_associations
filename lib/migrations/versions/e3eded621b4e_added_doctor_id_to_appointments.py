"""added doctor_id to appointments

Revision ID: e3eded621b4e
Revises: 6758026cc7ca
Create Date: 2023-07-18 11:50:53.564797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3eded621b4e'
down_revision = '6758026cc7ca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('doctor_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_appointments_doctor_id_doctors'), 'doctors', ['doctor_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_appointments_doctor_id_doctors'), type_='foreignkey')
        batch_op.drop_column('doctor_id')

    # ### end Alembic commands ###