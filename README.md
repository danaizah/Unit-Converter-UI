# Unit Converter 🔄

A full-stack unit converter built with **React** (frontend) and **Flask** (backend). This project is designed as a learning playground for pytest, React, and full-stack development fundamentals.

---

## Features

- Convert between common units: km ↔ miles, kg ↔ lbs, °C ↔ °F
- React frontend with a clean, interactive UI
- Flask REST API backend
- Pure conversion logic, fully tested with pytest

---

## Project Structure

```
unit-converter/
├── backend/
│   ├── app.py               # Flask app and API endpoints
│   ├── converter/
│   │   ├── __init__.py
│   │   └── logic.py         # Pure conversion functions
│   ├── tests/
│   │   └── test_logic.py    # Pytest tests
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.jsx           # Root component
│   │   ├── components/
│   │   │   └── Converter.jsx # Converter UI component
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 18+
- npm

---

### Backend Setup

```bash
# Navigate to the backend folder
cd backend

# Create and activate a virtual environment
python -m venv .venv

# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py
```

The backend will be running at `http://localhost:5000`.

---

### Frontend Setup

```bash
# Navigate to the frontend folder
cd frontend

# Scaffold the React app with Vite (first time only)
npm create vite@latest . -- --template react

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will be running at `http://localhost:5173`.

---

## Running Tests

```bash
cd backend

# Make sure your virtual environment is activated, then run:
pytest
```

To see more detail:

```bash
pytest -v
```

---

## API Reference

### `POST /convert`

Converts a value from one unit to another.

**Request body:**
```json
{
  "value": 100,
  "from_unit": "km",
  "to_unit": "miles"
}
```

**Success response:**
```json
{
  "result": 62.1371
}
```

**Error response:**
```json
{
  "error": "Unsupported conversion: km to lbs"
}
```

---

## Supported Conversions

| From | To |
|------|----|
| km | miles |
| miles | km |
| kg | lbs |
| lbs | kg |
| °C | °F |
| °F | °C |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React, Vite, JSX |
| Backend | Python, Flask, flask-cors |
| Testing | pytest |
| Communication | REST API, JSON |

---

## Learning Goals

This project is intentionally structured to help you explore:

- ✅ Writing and running unit tests with **pytest**
- ✅ Building reusable components in **React**
- ✅ Creating a REST API with **Flask**
- ✅ Connecting a frontend to a backend via **HTTP/JSON**
- ✅ Keeping business logic separate from UI (testability)

---

## Next Steps / Ideas

- Add more unit categories (speed, area, volume)
- Add conversion history log
- Style the UI with Tailwind CSS or CSS Modules
- Write frontend tests with Vitest or Jest
- Deploy the backend to Render and the frontend to Vercel

---

## License

This project is for learning purposes. Feel free to use, modify, and experiment.
