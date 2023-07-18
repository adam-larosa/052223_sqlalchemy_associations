from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, MetaData, create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.associationproxy import association_proxy

convention = {
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s'
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

    appointments = relationship( 'Appointment', back_populates = 'doctor' )
    
    patients = association_proxy( 'appointments', 'patient' )

    def __repr__( self ):
        return f'<Doctor id: {self.id} name: {self.name}>'

# a doctor 'has many' apppointments
# an appointment 'belongs to' a doctor
# the 'belongs-to' side ALWAYS gets the foreign key.  ;) 

class Appointment( Base ):
    __tablename__ = 'appointments'
    id = Column( Integer(), primary_key = True )
    notes = Column( String() )
    doctor_id = Column( Integer(), ForeignKey( 'doctors.id' ) )
    patient_id = Column( Integer(), ForeignKey( 'patients.id' ) )
    
    doctor = relationship( 'Doctor', back_populates = 'appointments' )
    patient = relationship( 'Patient', back_populates = 'appointments' )
    
    def __repr__( self ):
        return f'<Appointment id: {self.id} notes: {self.notes}>'


# a patient 'has many' appointments

class Patient( Base ):
    __tablename__ = 'patients'
    id = Column( Integer(), primary_key = True )
    name = Column( String() )

    appointments = relationship( 'Appointment', back_populates = 'patient' )

    doctors = association_proxy( 'appointments', 'doctor' )

    def __repr__( self ):
        return f'<Patient id: {self.id} name: {self.name}>'