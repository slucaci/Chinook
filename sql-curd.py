import psycopg2
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the PostgreSQL database connection string
db_url = "postgresql://35389:1234@localhost:5432/chinook"  # Adjust the username, password, and database name

# Create the SQLAlchemy engine
engine = create_engine(db_url)

# Create the base class for declarative models
Base = declarative_base()

# Create a class-based model for the "Programmer" table
class Programmer(Base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# Create a new instance of sessionmaker, then point it to our engine (the db)
Session = sessionmaker(bind=engine)

# Open an actual session by calling the Session() subclass defined above
session = Session()

# Creating the database using declarative_base subclass and the engine
Base.metadata.create_all(engine)

# Creating records on our Programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

sergiu_lucaci = Programmer(
    first_name="Sergiu",
    last_name="Lucaci",
    gender="M",
    nationality="Romanian",
    famous_for="Python"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

# Add each instance of our programmers to our session
# session.add_all([ada_lovelace, alan_turing, grace_hopper, margaret_hamilton, sergiu_lucaci, bill_gates, tim_berners_lee])

# Commit our session to the database
# session.commit()

# updating a single record

# programmer = session.query(Programmer).filter_by(id=17).first()
# programmer.famous_for = "World President"

# session.commit()

# updating multiple records
# people = session.query(Programmer).all()
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

#deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

# defensive programming
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name, programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n): ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer deleted")
#     else:
#         print("Programmer not deleted")




# Query the database to find all Programmers
programmers = session.query(Programmer).all()
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
