from typing import Optional

from pydantic import BaseModel


# Shared properties
class VacantBase(BaseModel):
    vacancyId: int
    companyId: int
    salary: float
    maxExperience: int
    minExperience: int
    vacancyLink: Optional[str] = None
    skills: list = []
    positionName = str


# Properties to receive on item creation
class VacantCreate(VacantBase):
    company_id: str
    salary: float
    max_experience: int
    min_experience: int
    vacancy_link: Optional[str] = None
    skills: list = []
    position_name = str


# Properties to receive on Vacant update
class VacantUpdate(VacantBase):
    pass


# Properties shared by models stored in DB
class VacantInDBBase(VacantBase):
    vacancy_id: int
    company_id: int
    salary: float
    max_experience: int
    min_experience: int
    vacancy_link: Optional[str] = None
    skills: list = []
    position_name = str


class Config:
        orm_mode = True


# Properties to return to client
class Vacant(VacantInDBBase):
    pass


# Properties properties stored in DB
class VacantInDB(VacantInDBBase):
    pass
