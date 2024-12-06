from fastapi import FastAPI, HTTPException, Depends, Request
from typing import Optional
from pydantic import BaseModel
from rag.inference.chat import ChatService

app = FastAPI()

chat_service = ChatService()


@app.middleware("http")
async def capture_user_ip(request: Request, call_next):
    # Capture user IP address from request
    user_ip = request.client.host
    # Pass user IP to the path operation function
    response = await call_next(request)
    return response


class QueryRequest(BaseModel):
    user_query: str
    user_ip: str


db_name = "SIH"
collection_name = "pdfs"


@app.post("/query")
async def query_endpoint(request: QueryRequest):
    try:
        response = chat_service.chat(
            request.user_query,
            db_name,
            collection_name,
            user_ip=request.user_ip
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@app.get("/")
async def root():
    return {"message": "FastAPI is running"}
