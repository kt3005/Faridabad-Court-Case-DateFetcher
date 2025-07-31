# Faridabad-Court-Case-DateFetcher
A mini web application that allows users to fetch and view public court case details (metadata and order/judgment links) from the Faridabad District Court (eCourts portal), using either:  Case Type + Number + Year )
Here is the complete `README.md` file for your **Faridabad Court Case Data Fetcher** project using mock data with Flask and HTML UI:

---

```markdown
# 🏛️ Faridabad Court Case Data Fetcher (Mock Version)

This is a simple **Flask-based web application** that simulates fetching public court case details from the **Faridabad District Court (eCourts)**. The app currently uses **mock data** to demonstrate functionality in environments where live scraping may not be feasible.

---

## 🔍 Features

- 🎯 Input fields for Case Type, Case Number, and Filing Year
- 🧾 Displays:
  - Parties involved
  - Filing Date
  - Next Hearing Date
  - Order/Judgment links (PDF)
- 🗃️ Logs all queries to a local SQLite database (`queries.db`)
- 🎨 Beautiful frontend with a court-themed background
- ⚠️ Graceful error handling if case not found

---

## 📸 Screenshot

![App Screenshot](https://i.imgur.com/IOACvhq.png)

---

## 🧪 Demo Input

Use the following input to simulate a successful case fetch:

- **Case Type**: `CS`
- **Case Number**: `1234`
- **Filing Year**: `2022`

**Output:**
```

Parties: A vs B
Filing Date: 2022-05-12
Next Hearing: 2025-08-15
Orders: Latest Order (PDF link)

````

---

## 🚀 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/faridabad-court-fetcher.git
cd faridabad-court-fetcher
````

### 2. Install the required Python packages

```bash
pip install flask
```

### 3. Run the Flask server

```bash
python app.py
```

### 4. Open in your browser

```
http://127.0.0.1:5000/
```

---

## 📂 Project Structure

```
faridabad-court-fetcher/
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # Frontend HTML (Jinja2 templating)
├── static/
│   └── sample_order.pdf    # Mock PDF order file
├── queries.db              # SQLite DB created at runtime
└── README.md               # This file
```

---

## ⚙️ Technologies Used

* Python 3.x
* Flask
* HTML/CSS (with inline styles)
* SQLite (via `sqlite3` module)

---

## 📝 Notes

* Currently uses mock data. Future versions can integrate live scraping with CAPTCHA bypass, if needed.
* All inputs are stored with timestamp in a local SQLite database.

---

## 📜 License

This project is released under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Karan Tyagi**
Built as part of a demo for a Court Data Dashboard tool.
