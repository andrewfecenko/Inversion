from sqlalchemy import *

engine = create_engine('sqlite:///:memory:', echo=False)

Base = declarative_base()

class Entry(Base):
	__tablename__ = 'entries'
	id = Column(Integer, Sequence('entry_id_seq'), primary_key=True)
	time_created = Column(DateTime(timezone=True), server_default=sql.func.now())
	time_updated = Column(DateTime(timezone=True), onupdate=sql.func.now())
	content = Column(String(256))

Base.metadata.create_all(engine)

Session = orm.sessionmaker(bind=engine)
session = Session()

