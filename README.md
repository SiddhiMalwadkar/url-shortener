#  Analytics-Driven URL Shortener

A high-performance backend service built using **FastAPI** and **PostgreSQL** that converts long URLs into short, unique links and tracks detailed user analytics in real time.

---

##  Project Preview

<!-- Replace these with your actual screenshots after uploading to GitHub -->

### 🔹 API Documentation (Swagger UI)
![Swagger UI](./images/swagger.png)

### 🔹 Short URL Creation
![Shorten API](./images/shorten.png)

### 🔹 Analytics Output
![Analytics](./images/analytics.png)

---

##  Features

-  URL Shortening using custom **Base62 encoding**
-  Instant redirection to original URLs
-  Real-time click analytics
-  Referrer tracking (direct, external sources)
-  Device/Browser tracking via User-Agent
-  Scalable backend architecture using FastAPI
-  Relational database design with PostgreSQL

---

##  Tech Stack

| Category        | Technology        |
|----------------|------------------|
| Backend        | FastAPI          |
| Database       | PostgreSQL       |
| ORM            | SQLAlchemy       |
| Language       | Python           |
| Server         | Uvicorn          |

---

## 📁 Project Structure
url_shortener/
│
├── app/
│ ├── main.py # Entry point
│ ├── database.py # DB connection
│ ├── models.py # Database models
│ ├── schemas.py # Request/response schemas
│ ├── crud.py # Business logic
│ ├── utils.py # Base62 encoding
│ └── analytics.py # Analytics routes
│
├── requirements.txt
└── README.md

---

##  API Endpoints

| Method | Endpoint                     | Description              |
|--------|-----------------------------|--------------------------|
| POST   | `/shorten`                  | Create short URL         |
| GET    | `/{short_code}`             | Redirect to original URL |
| GET    | `/analytics/{short_code}`   | Get analytics data       |

---

##  Example Usage

### 🔹 Create Short URL

```json
POST /shorten
{
  "original_url": "https://example.com"
}
🔹 Response
{
  "short_url": "http://localhost:8000/1"
}
🔹 Analytics Response
{
  "total_clicks": 5,
  "referrers": {
    "direct": 5
  },
  "devices": {
    "Chrome": 3,
    "Edge": 2
  }
}
▶️ Run Locally
1. Clone the repository
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
2. Install dependencies
pip install -r requirements.txt
3. Configure Database
Update database.py:-
DATABASE_URL = "postgresql://username:password@localhost:5432/url_db"
4. Run the server
uvicorn app.main:app --reload
5. Open API docs
http://127.0.0.1:8000/docs
