from sqlalchemy.orm import Session
from app import crud
from app.schemas.business import BusinessCreate, BusinessInDBBase, BusinessUpdate
from app.tests.utils.utils import random_email, random_lower_string
from datetime import date

def test_create_business(db: Session) -> None:
    name =random_lower_string()
    link = random_lower_string()
    contact_first_name= random_lower_string()
    contact_last_name=random_lower_string()
    contact_phone_number=random_lower_string()
    contact_email=random_email()
    country= random_lower_string()
    
    business_in = BusinessInDBBase(name=name,link=link,contact_first_name=contact_first_name, contact_last_name=contact_last_name, contact_phone_number=contact_phone_number, contact_email=contact_email, country=country, date_added=date.today())    
    business = crud.business.create(db=db, obj_in=business_in)
    assert business.name == name
    assert business.link == link
    assert business.contact_first_name == contact_first_name
    assert business.contact_last_name == contact_last_name
    assert business.contact_phone_number==contact_phone_number
    assert business.contact_email == contact_email
    assert business.country == country


def test_get_business(db: Session) -> None:
    name =random_lower_string()
    link = random_lower_string()
    contact_first_name= random_lower_string()
    contact_last_name=random_lower_string()
    contact_phone_number=random_lower_string()
    contact_email=random_email()
    country= random_lower_string()
    
    business_in = BusinessInDBBase(name=name,link=link,contact_first_name=contact_first_name, contact_last_name=contact_last_name, contact_phone_number=contact_phone_number, contact_email=contact_email, country=country, date_added=date.today())    
  
    business = crud.business.create(db=db, obj_in=business_in)
    stored_business = crud.business.get(db=db, company_id=business.company_id)
    assert stored_business
    assert business.name == stored_business.name
    assert business.link == stored_business.link
    assert business.contact_first_name == stored_business.contact_first_name
    assert business.contact_last_name == stored_business.contact_last_name
    assert business.contact_phone_number==stored_business.contact_phone_number
    assert business.contact_email == stored_business.contact_email
    assert business.country == stored_business.country


def test_update_business(db: Session) -> None:
    name =random_lower_string()
    link = random_lower_string()
    contact_first_name= random_lower_string()
    contact_last_name=random_lower_string()
    contact_phone_number=random_lower_string()
    contact_email=random_email()
    country= random_lower_string()
    business_in = BusinessInDBBase(name=name,link=link,contact_first_name=contact_first_name, contact_last_name=contact_last_name, contact_phone_number=contact_phone_number, contact_email=contact_email, country=country, date_added=date.today())    


    business = crud.business.create(db=db, obj_in=business_in)

    country2 = random_lower_string()
    business_update = BusinessUpdate(country=country2)
    business2 = crud.business.update(db=db, db_obj=business, obj_in=business_update)

    assert business.name == business2.name
    assert business.link == business2.link
    assert business.contact_first_name == business2.contact_first_name
    assert business.contact_last_name == business2.contact_last_name
    assert business.contact_phone_number==business2.contact_phone_number
    assert business.contact_email == business2.contact_email
    assert business.country == business2.country
    assert business.company_id == business2.company_id

def test_delete_business(db: Session) -> None:
    name =random_lower_string()
    link = random_lower_string()
    contact_first_name= random_lower_string()
    contact_last_name=random_lower_string()
    contact_phone_number=random_lower_string()
    contact_email=random_email()
    country= random_lower_string()
    business_in = BusinessInDBBase(name=name,link=link,contact_first_name=contact_first_name, contact_last_name=contact_last_name, contact_phone_number=contact_phone_number, contact_email=contact_email, country=country, date_added=date.today())    

    business = crud.business.create(db=db, obj_in=business_in)
    business2 = crud.business.remove(db=db, company_id=business.company_id)
    business3 = crud.business.get(db=db, company_id=business.company_id)
    assert business3 is None
    assert business2.company_id == business.company_id
    assert business2.name == name
    assert business2.link == link
    assert business2.contact_first_name == contact_first_name
    assert business2.contact_last_name == contact_last_name
    assert business2.contact_phone_number==contact_phone_number
    assert business2.contact_email == contact_email
    assert business2.country == country

