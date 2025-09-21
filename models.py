from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime, UTC

class Bug(Base):
    __tablename__ = 'bugs'
    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=False, nullable=False)
    status = Column(String(120), unique=False, nullable=False, default='To Do')
    report_date = Column(DateTime, default=lambda: datetime.now(UTC))
    completion_date = Column(DateTime, nullable=True)

    def __repr__(self):
        return f'<Bug {self.title}>'
