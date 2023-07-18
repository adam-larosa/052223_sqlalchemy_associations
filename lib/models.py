from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, MetaData

convention = {
    'fk': 'fk_%(table_name)s_%(column_name)s_%(referred_table_name)s'
}
md = MetaData( naming_convention = convention )


Base = declarative_base( metadata = md )