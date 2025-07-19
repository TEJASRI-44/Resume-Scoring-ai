# 🤖 Resume Screening AI Bot

A simple and intelligent AI-powered Resume Screening App built with **Streamlit**. It automatically extracts important details like **email**, **phone number**, **location**, and matches resumes to a given **job description**. You can also **download results in Excel format**.

---

## 🚀 Features

- Upload multiple PDF resumes 📂
- Paste job description (JD) text 📄
- Extract:
  - Name
  - Email
  - Phone Number
  - Location
  - Matching Score 🔍
- View results in tabular format 📊
- Download table as `.xlsx` Excel file 📥
- Refresh the app with one click 🔄

---

## 🧠 Tech Stack

- **Frontend/UI**: Streamlit
- **Backend**: Python
- **PDF Parsing**: PyMuPDF (fitz)
- **Excel Handling**: Pandas + Openpyxl

---

## 🛠️ Libraries Used

| Library | Purpose |
|--------|---------|
| `streamlit` | Web interface banane ke liye |
| `pandas` | Data ko table me store karne aur Excel file banane ke liye |
| `fitz` (PyMuPDF) | Resume (PDF) ka text extract karne ke liye |
| `re` | Regular expressions se email, phone aur location nikalne ke liye |
| `difflib` | JD aur resume ka match score nikalne ke liye |
| `base64` | Excel download button create karne ke liye |
| `io` | Excel file memory me generate karne ke liye |
| `openpyxl` | Excel file ko properly save/export karne ke liye |

---

## 🧪 How to Run Locally

1. **Clone the repository**

```bash
[[git clone https://github.com/YourUsername/resume-screening-ai-bot.git]
cd resume-screening-ai-bot
