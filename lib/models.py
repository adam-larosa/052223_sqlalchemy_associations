from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, MetaData, create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
convention = {
    'fk': 'fk_%(table_name)s_%(column_name)s_%(referred_table_name)s'
}
md = MetaData( naming_convention = convention )

Base = declarative_base( metadata = md )

engine = create_engine( 'sqlite:///funstuff.db' )
Session = sessionmaker( bind = engine )

session = Session()


class Doctor( Base ):
    __tablename__ = 'doctors'

    id = Column( Integer(), primary_key = True )
    name = Column( String() )