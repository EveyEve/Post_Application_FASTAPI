from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth,vote
from fastapi.middleware.cors import CORSMiddleware


#will create our models (this will create the posts table automatically)
#now uncommented since I implemented alembic 
#models.Base.metadata.create_all(bind=engine)

#fastapi instance
app = FastAPI()

origins = ["*"]
#CORSMiddleware runs before any request 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#router object - split our path operations cleaner into files 
#include all the routes in the file we indicated
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

#path operation
@app.get("/") 
def root(): 
    return {"message": "Welcome to my post application"} 

