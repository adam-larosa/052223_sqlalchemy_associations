import ipdb
from models import session, Doctor, Appointment, Patient

d1 = session.query( Doctor ).first()
a1 = session.query( Appointment ).first()
p1 = session.query( Patient ).first()

ipdb.set_trace()