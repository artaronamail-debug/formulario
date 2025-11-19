from sqlalchemy import create_engine, Column, Integer, String, Text, DECIMAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "sqlite:///./properties.db"  # SQLite database file

Base = declarative_base()

class PropertyType(Base):
    __tablename__ = "property_types"
    type_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    properties = relationship("Property", back_populates="property_type")

class Operation(Base):
    __tablename__ = "operations"
    operation_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    properties = relationship("Property", back_populates="operation")

class Location(Base):
    __tablename__ = "locations"
    location_id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    neighborhood = Column(String, index=True)
    province = Column(String)
    country = Column(String)
    latitude = Column(DECIMAL(10, 8))
    longitude = Column(DECIMAL(11, 8))

    properties = relationship("Property", back_populates="location")

class Property(Base):
    __tablename__ = "properties"
    property_id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    title = Column(String)
    description = Column(Text)
    price = Column(DECIMAL(10, 2))
    currency = Column(String)
    surface_area_m2 = Column(DECIMAL(10, 2))
    num_rooms = Column(Integer)
    num_bathrooms = Column(Integer)
    status = Column(String) # e.g., "available", "sold", "rented"

    property_type_id = Column(Integer, ForeignKey("property_types.type_id"))
    operation_id = Column(Integer, ForeignKey("operations.operation_id"))
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    # agent_id = Column(Integer, ForeignKey("agents.agent_id"), nullable=True) # Uncomment if you add Agent model

    property_type = relationship("PropertyType", back_populates="properties")
    operation = relationship("Operation", back_populates="properties")
    location = relationship("Location", back_populates="properties")
    # agent = relationship("Agent", back_populates="properties") # Uncomment if you add Agent model
    images = relationship("Image", back_populates="property")

class Image(Base):
    __tablename__ = "images"
    image_id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey("properties.property_id"))
    url = Column(String)
    description = Column(Text, nullable=True)
    order = Column(Integer)

    property = relationship("Property", back_populates="images")

# Setup database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
