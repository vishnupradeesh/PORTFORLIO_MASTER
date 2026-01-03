"""
FastAPI Portfolio Application
Author: Vishnu Pradeesh N

Usage:
    1. Install dependencies: pip install fastapi uvicorn jinja2 python-multipart
    2. Run the server: uvicorn main:app --reload
    3. Open http://localhost:8000 in your browser
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr
from typing import Optional
import os
from db import BackendDatabase

# Initialize database
db = BackendDatabase()

# Initialize FastAPI app
app = FastAPI(
    title="Vishnu Pradeesh N - Portfolio",
    description="Senior Software Engineer Portfolio",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")


# Pydantic model for contact form
class ContactForm(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str


# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the main portfolio page"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/contact")
async def submit_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...)
):
    """
    Handle contact form submission
    
    In production, you would:
    - Save to database
    - Send email notification
    - Add rate limiting
    """
    # Log the contact submission (replace with database/email in production)
    print(f"""
    New Contact Submission:
    Name: {name}
    Email: {email}
    Subject: {subject}
    Message: {message}
    """)

    db.insert_contact(name, email, subject, message)
    print(db.fetch_all_contacts()) # Just to demonstrate DB interaction
    
    # For now, redirect back to contact section with success message
    # In production, you'd want to add flash messages or return JSON
    return RedirectResponse(url="/#contact", status_code=303)


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy", "version": "1.0.0"}


# Run with: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
