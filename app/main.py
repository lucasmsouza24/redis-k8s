from fastapi import FastAPI
import redis
import os

app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "redis-service")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.get("/visit")
def visit():
    count = r.incr("counter")
    return {"visits": count}

@app.get("/")
def root():
    return {"message": "FastAPI + Redis running in Kubernetes"}
