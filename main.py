from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, Integer, String
from typing import Optional

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)


class UserRead(BaseModel):
    email: str


class UserCreate(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None


app = FastAPI()


@app.on_event("startup")
async def create_db_tables():
    with engine.begin() as conn:
        Base.metadata.create_all(bind=conn)


@app.get("/users", response_model=List[UserRead])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends()):
    users = db.query(User).offset(skip).limit(limit).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

@app.post("/login", response_model=UserRead)
async def login_user(user: UserCreate, db: Session = Depends()):
    user_obj = db.query(User).filter_by(email=user.email).first()
    if not user_obj:
        raise HTTPException(status_code=404, detail="User not found")
    # if not verify_password(user.password, user_obj.hashed_password):
    #     raise HTTPException(status_code=400, detail="Incorrect email or password")
    return user_obj


@app.post("/logout")
async def logout_user():
    pass
