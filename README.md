# FastAPI Portfolio Template

A modern, futuristic portfolio website built with Python FastAPI and Jinja2 templates.

## 🚀 Quick Start

### 1. Setup Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your Images

Place your images in the `static/images/` folder:
- `profile.jpg` - Your profile picture
- `hero-bg.jpg` - Hero section background
- `project-fruit.jpg` - Fruit Ripening project image (optional)
- `project-daynight.jpg` - Day-Night project image (optional)

### 4. Run the Server

```bash
uvicorn main:app --reload
```

### 5. Open in Browser

Navigate to: http://localhost:8000

## 📁 Project Structure

```
fastapi-templates/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── static/
│   ├── css/
│   │   └── styles.css  # All CSS styles
│   └── images/         # Your images go here
│       ├── profile.jpg
│       ├── hero-bg.jpg
│       └── ...
└── templates/
    ├── base.html       # Base template with common elements
    └── index.html      # Main portfolio page
```

## ✨ Features

- 🎨 Modern, futuristic design with glassmorphism effects
- 📱 Fully responsive layout
- 🌙 Dark theme with cyan/teal accents
- ⚡ Smooth animations and transitions
- 📧 Contact form (configure backend for email)
- 🔗 Social media links
- 📊 Skills visualization
- 💼 Project showcase

## 🔧 Customization

### Update Personal Info

Edit `templates/index.html` to update:
- Name and tagline
- About section content
- Work experience
- Skills list
- Project details
- Contact information
- Social media links

### Modify Styles

Edit `static/css/styles.css` to customize:
- Colors (CSS variables at the top)
- Fonts
- Spacing
- Animations

### Add More Pages

1. Create a new template in `templates/`
2. Add a route in `main.py`:

```python
@app.get("/new-page", response_class=HTMLResponse)
async def new_page(request: Request):
    return templates.TemplateResponse("new-page.html", {"request": request})
```

## 📧 Contact Form Backend

The contact form currently logs submissions. To add email functionality:

```python
import smtplib
from email.mime.text import MIMEText

@app.post("/api/contact")
async def submit_contact(...):
    # Send email
    msg = MIMEText(f"From: {name}\nEmail: {email}\n\n{message}")
    msg['Subject'] = subject
    msg['From'] = 'your-email@example.com'
    msg['To'] = 'your-email@example.com'
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your-email@example.com', 'your-app-password')
        server.send_message(msg)
    
    return {"status": "success"}
```

## 🚀 Deployment

### Deploy to Render

1. Push to GitHub
2. Connect to Render.com
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Deploy to Railway

1. Push to GitHub
2. Connect to Railway
3. It will auto-detect FastAPI and deploy

### Deploy to DigitalOcean App Platform

1. Push to GitHub
2. Create new App on DigitalOcean
3. Select your repo
4. Configure run command: `uvicorn main:app --host 0.0.0.0 --port 8080`

## 📝 License

MIT License - Feel free to use and modify for your own portfolio!

---

Built with ❤️ using FastAPI & Jinja2
