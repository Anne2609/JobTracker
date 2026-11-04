"""Modelele bazei de date pentru JobTracker."""
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    applications = db.relationship("Application", back_populates="user", cascade="all, delete-orphan")
    companies = db.relationship("Company", back_populates="owner")


class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    owner = db.relationship("User", back_populates="companies")
    industry = db.Column(db.String(100))
    location = db.Column(db.String(150))
    website = db.Column(db.String(255))
    applications = db.relationship("Application", back_populates="company")


class Application(db.Model):
    __tablename__ = "applications"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=False, index=True)
    position = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(30), nullable=False, default="Applied")
    applied_at = db.Column(db.Date, nullable=False)
    notes = db.Column(db.Text)
    user = db.relationship("User", back_populates="applications")
    company = db.relationship("Company", back_populates="applications")
    interviews = db.relationship("Interview", back_populates="application", cascade="all, delete-orphan")


class Interview(db.Model):
    __tablename__ = "interviews"
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey("applications.id"), nullable=False, index=True)
    scheduled_at = db.Column(db.DateTime, nullable=False)
    interview_type = db.Column(db.String(50), nullable=False, default="Online")
    notes = db.Column(db.Text)
    application = db.relationship("Application", back_populates="interviews")
