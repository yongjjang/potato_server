from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy import func
from app.database import base


class BranchOffice(base):
    __tablename__ = 'branch_office'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    telno = Column(String(11))
    address = Column(String(60))
    latitude = Column(Float(20))
    longitude = Column(Float(20))


    def __init__(self, id, name, telno, address, latitude, longitude):
        self.id = id
        self.name = name
        self.telno = telno
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "<BranchOffice : ('%d', '%s', '%s', '%s', '%f', '%f'>" % \
               (self.id, self.name, self.telno, self.address, self.latitude, self.longitude)

class Employee(base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    telno = Column(String(11))
    address = Column(String(60))
    walking_point = Column(Integer(11))


    def __init__(self, id, name, telno, address, walking_point):
        self.id = id
        self.name = name
        self.telno = telno
        self.address = address
        self.walking_point = walking_point

    def __repr__(self):
        return "<BranchOffice : ('%d', '%s', '%s', '%s', '%d'>" % \
               (self.id, self.name, self.telno, self.address, self.walking_point)


class CommuteLog(base):
    __tablename__ = 'commute_log'
    today = Column(DateTime, default=func.date())
    office_id = Column(String(40))
    emp_id = Column(String(11))
    work_in_time = Column(String(60))
    work_out_time =  Column(Integer(11))


    def __init__(self, today, emp_id, work_in_time, work_out_time):
        self.today = today
        self.emp_id = emp_id
        self.address = address
        self.work_in_time = work_in_time
        self.work_out_time = work_out_time

    def __repr__(self):
        return "<BranchOffice : ('%s', '%d', '%d', '%s', '%d'>" % \
               (self.today, self.office_id , self.emp_id, self.work_in_time, self.work_out_time)
