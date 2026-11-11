from fastapi import FastAPI
from .database import engine, Base
from .routers import orders

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Order Service", version="1.0.0")

app.include_router(orders.router)


@app.get("/health")
def health():
    return {"status": "healthy", "service": "order-service"}
