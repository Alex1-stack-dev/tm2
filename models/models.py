from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
Base = declarative_base()
engine = create_engine('sqlite:///meet.db')
Session = sessionmaker(bind=engine)
class Athlete(Base):
    __tablename__ = 'athletes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    team = Column(String)
def import_athletes_from_csv(fname):
    import pandas as pd
    df = pd.read_csv(fname)
    session = Session()
    for _, row in df.iterrows():
        athlete = Athlete(name=row['Name'], team=row['Team'])
        session.add(athlete)
    session.commit()
def get_all_athletes():
    session = Session()
    return session.query(Athlete).all()
Base.metadata.create_all(engine)
