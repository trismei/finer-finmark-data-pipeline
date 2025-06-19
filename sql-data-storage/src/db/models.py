from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Date, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EventLog(Base):
    __tablename__ = 'event_logs'
    
    event_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, nullable=False)
    event_type = Column(String, nullable=False)
    product_id = Column(String, nullable=False)
    amount = Column(Numeric(10,2),  nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)

class MarketingSummary(Base):
    __tablename__ = 'marketing_summary'
    
    event_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    users_active = Column(Integer, nullable=False)
    total_sales = Column(Numeric(10,2), nullable=False)
    new_customers = Column(Integer, nullable=False)
    report_date = Column(Date, nullable=False)
    report_time = Column(Time, nullable=False)

class TrendReport(Base):
    __tablename__ = 'trend_report'
    
    event_id = Column(Integer, primary_key=True, autoincrement=True)
    week_start = Column(Date, nullable=False)
    week_end = Column(Date, nullable=False)
    avg_users = Column(Integer, nullable=False)
    sales_growth_rate = Column(Numeric(5,3), nullable=False)

