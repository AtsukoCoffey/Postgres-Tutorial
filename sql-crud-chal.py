from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
# ignore Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Country" table
class Country(base):
    __tablename__ = "Country"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    people = Column(String)
    color = Column(String)


# ask for a session to create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defind above
session = Session()
# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Programmer table
ireland = Country(
    name="Ireland",
    people="Irish",
    color="Orange"
)

japan = Country(
    name="Japan",
    people="Japanese",
    color="Red"
)

america = Country(
    name="America",
    people="American",
    color="blue"
)

england = Country(
    name="England",
    people="English",
    color="white"
)

# add each instance of our programmers to our session
# session.add(ireland)
# session.add(japan)
# session.add(america)
# session.add(england)

# commit our session to the database
# session.commit()

# updating a single record
# country = session.query(Country).filter_by(name="England").first()
# country.color = "White red"
# session.commit()

# delete a single record
countryInput = input("Enter the country name : ")
country = session.query(Country).filter_by(name=countryInput).first()
# defensive programming
if country is not None:
    print("Country Found: ", country.name)
    confirmation = input("Are you sure you want to delete this record? (y/n) ")
    if confirmation.lower() == "y":
        session.delete(country)
        session.commit()
        print("The record has been deleted")
    else:
        print("The record not deleted")
else:
    print("No records found")


countries = session.query(Country)
for country in countries:
    print(
        country.id,
        country.name,
        country.people,
        country.color,
        sep=" | "
    )