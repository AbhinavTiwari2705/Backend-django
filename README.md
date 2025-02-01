# FAQ Management API (Django + SQLite)

## 📌 Overview
This is a FAQ Management API built using Django and SQLite. The application allows users to:
- Add FAQs with multilingual support.
- Retrieve FAQs in different languages.
- Efficiently manage FAQ content with automatic translation.

## 🛠 Tech Stack
- **Backend**: Django, Django Rest Framework (DRF)
- **Database**: SQLite (default for Django)
- **Translation**: Google Translate API (or any other translation service)
- **Caching**: Redis (for caching translations)
- **Text Editor**: CKEditor for rich text answers

## 📂 Project Structure
```
📦 faq-system
├── 📂 faqs/
│   ├── 📂 migrations/ # Database migration files
│   ├── 📂 models/ # Django Models (FAQ model)
│   ├── 📂 serializers/ # DRF serializers
│   ├── 📂 views/ # Views for handling API requests
│   ├── 📂 urls/ # URLs for API endpoints
│   └── tests.py # Unit tests
├── 📂 config/ # Django project settings
│   └── settings.py # Application configurations
├── manage.py # Django management commands
├── requirements.txt # Project dependencies
└── README.md # Documentation
```

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/faq-system.git
cd faq-system
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and configure the following variables:
```bash
PORT=8000
GOOGLE_TRANSLATE_API_KEY=your_google_translate_api_key
```

### 4️⃣ Start the Server
Since SQLite is the default database for Django, there’s no need to configure any additional database setup beyond running migrations.
```bash
python manage.py migrate
python manage.py runserver
```

### 5️⃣ Run in Development Mode
For auto-reloading during development, you can use the Django development server.
```bash
python manage.py runserver
```

## 🛠 API Endpoints

### ✅ Create a New FAQ (Auto-Translate to English)
- **Endpoint**: `POST /api/faqs/`
- **Request Body**:
```json
{
  "question": "What is Django?",
  "answer": "Django is a web framework."
}
```
- **Response**:
```json
{
  "question": "What is Django?",
  "answer": "Django is a web framework.",
  "translations": {
    "hi": {
      "question": "डjango क्या है?",
      "answer": "डjango एक वेब फ्रेमवर्क है।"
    },
    "bn": {
      "question": "ডjango কি?",
      "answer": "ডjango একটি ওয়েব ফ্রেমওয়ার্ক।"
    }
  },
  "_id": "unique_faq_id",
  "__v": 0
}
```

### ✅ Retrieve All FAQs (Default: English)
- **Endpoint**: `GET /api/faqs/`
- **Response**:
```json
[
  {
    "question": "What is SQL?",
    "answer": "SQL is structured query language."
  },
  {
    "question": "Capital of India?",
    "answer": "Delhi"
  }
]
```

### ✅ Retrieve FAQs in a Specific Language
- **Endpoint**: `GET /api/faqs/?lang=hi`
- **Response (Translated to Hindi)**:
```json
[
  {
    "question": "SQL क्या है?",
    "answer": "SQL संरचित क्वेरी भाषा है"
  },
  {
    "question": "भारत की राजधानी?",
    "answer": "दिल्ली"
  }
]
```

### ✅ Retrieve Specific FAQ in a Specific Language
- **Endpoint**: `GET /api/faqs/?lang=hi&id=<faqid>`
- **Response (Specific FAQ translated to Hindi)**:
```json
{
  "question": "भारत की राजधानी?",
  "answer": "दिल्ली"
}
```

## 🧪 Running Tests
To run unit tests:
```bash
python manage.py test
```

## 🐳 Docker Support
To run using Docker:

### 1️⃣ Build the Docker Image
```bash
docker build -t faq-api .
```

### 2️⃣ Run the Container
```bash
docker run -p 8000:8000 faq-api
```