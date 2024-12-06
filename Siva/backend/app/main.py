from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import youtube_router, scrapy_router, pdf_router

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React's localhost
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(youtube_router.router, prefix="/youtube", tags=["YouTube"])
app.include_router(scrapy_router.router, prefix="/scrapy", tags=["Scrapy"])
app.include_router(pdf_router.router, prefix="/pdf", tags=["pdf"])


@app.get("/")
async def root():
    return {"message": "Welcome to the SIH Backend API"}
