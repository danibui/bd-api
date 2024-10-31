from fastapi import FastAPI
from routes import appointments, clients, payments, doctors, medical_history, treatments, queries

app = FastAPI()

app.include_router(appointments.router)
app.include_router(clients.router)
app.include_router(payments.router)
app.include_router(doctors.router)
app.include_router(medical_history.router)
app.include_router(treatments.router)
app.include_router(queries.router)
