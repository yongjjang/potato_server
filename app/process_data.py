from app.database import db_session
from app.models import BranchOffice

def get_office_tables():
    queries = db_session.query(BranchOffice)
    entries = [dict(id=q.id, name=q.name, telno=q.telno, address=q.address, latitude=q.latitude, longitude=q.longitude) for q in queries]
    return entries


def add_office_entry(id, name, telno, address, latitude, longitude):
    row = (id, name, telno, address, latitude, longitude)
    db_session.add(row)
    db_session.commit()


if __name__ == "__main__":
    print(get_office_tables())


