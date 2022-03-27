from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Float, REAL, Text, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .business import Bussiness


class Vacant(Base):
    vacancy_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey("business.companyId"))
    salary = Column(Float)
    max_experience = Column(Integer)
    vacancy_link = Column(String)
    min_rxperience = Column(Integer)
    skills = Column(Text)
    position_name = Column(String)
    active = Column(Boolean)
    company = relationship("Business", back_poulates="vacancies")
