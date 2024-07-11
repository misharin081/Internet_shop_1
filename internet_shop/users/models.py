# from sqlalchemy import Column, Integer, String, ForeignKey, Text, Float, Date
# from database import Base
#
# class Users(Base):
#     __tablename__ = "Users"
#     id = Column(Integer, primary_key=True)
#     email = Column(String(20), nullable=False)
#     hashed_password = Column(String(16), nullable=False)
#     role = Column(Integer, ForeignKey("Roles.id"), nullable=False)
#
#
# class Roles(Base):
#     __tablename__ = "Roles"
#     id = Column(Integer, primary_key=True)
#     role_name = Column(String(10), nullable=False)
#
#
# class Client(Base):
#     __tablename__ = "clients"
#     id = Column(Integer, primary_key=True)
#     full_name = Column(String(100), nullable=False)
#     phone_number = Column(String(20), nullable=False)
#
#
# class Products(Base):
#     __tablename__ = "products"
#     id = Column(Integer, primary_key=True)
#     product_name = Column(String(200), nullable=False)
#     category = Column(ForeignKey("categories.id"), nullable=False)
#     description = Column(Text)
#     cost = Column(Float)
#     count_of_sells = Column(Integer, default=0, nullable=False)
#     discount = Column(Float, default=0.0, nullable=False)
#
#
# class Categories(Base):
#     __tablename__ = "categories"
#     id = Column(Integer, primary_key=True)
#     category_name = Column(String(50), nullable=False)
#
# class OrderHistory(Base):
#     __tablename__ = "history"
#     id = Column(Integer, primary_key=True)
#     product = Column(ForeignKey("products.id"), nullable=False)
#     date = Column(Date, nullable=False)
#     quantity = Column(Integer, default=1, nullable=False)
#     full_cost = Column(Float, nullable=False)
#     client = Column(ForeignKey("clients.id"), nullable=False)


