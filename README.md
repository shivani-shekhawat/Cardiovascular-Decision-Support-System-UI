
# ASCVD Risk Score Calculator 🫀

A lightweight API + UI application to compute ASCVD (Atherosclerotic Cardiovascular Disease) risk scores based on clinical parameters. Built with **FastAPI**, **PostgreSQL**, and **Docker**, with an optional **Streamlit frontend** for quick demos.

## 📦 Features

- Calculates 10-year ASCVD risk using standard clinical scoring guidelines
- RESTful API built using FastAPI
- Containerized with Docker for easy deployment
- Streamlit UI for non-technical users or demo purposes
- PostgreSQL backend to store and query patient data

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Frontend (optional)**: Streamlit

## 🚀 Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/Cardiovascular-Decision-Support-System.git
    cd ascvd-risk-calculator
    ```

2. Run the API with Docker:
    ```bash
    docker-compose up --build
    ```

3. Access the FastAPI docs:
    ```
    http://localhost:8000/docs
    ```

4. (Optional) Run the Streamlit UI:
    ```bash
    streamlit run ascvd_calculator_app.py
    ```

## 📄 API Documentation

Interactive API documentation is available at `/docs` once the server is running.

## 🤝 Contributing

Feel free to fork, improve, and submit pull requests. Feedback and contributions are welcome!

---

**Disclaimer:** This is a demo project for educational purposes. Not intended for clinical use without validation.
