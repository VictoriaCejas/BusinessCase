from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Bussiness(Base):
    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    link = Column(String)
    date_added = Column(Date)
    contact_first_name = Column(String)
    contact_last_name = Column(String)
    contact_phone_numer = Column(String)
    contact_email = Column(String)
    country = Column(String)
