Here is **one clean and production-ready `README.md`** for your Mailing Microservice:

```markdown
# 📧 Mailing Microservice  
A simple and scalable mailing microservice built with Node.js & Express.  
It supports **default SMTP credentials from `.env`** and also allows **user-provided SMTP settings** in each API request.

---

## 🚀 Features
- Send emails using **Nodemailer**
- Supports **Gmail, Outlook, Zoho, Custom SMTP**
- Use **default SMTP values** from `.env`
- OR **override SMTP credentials** per request
- Clean architecture (Controller → Service → Utils)
- HTML documentation served at `/`

---

## 📁 Project Structure
```

mailing-service/
├── public/
│   └── index.html             # Documentation page
├── src/
│   ├── controllers/
│   │   └── mail.controller.js
│   ├── services/
│   │   └── mail.service.js
│   ├── utils/
│   │   └── mailer.js
│   ├── routes/
│   │   └── mail.routes.js
│   ├── app.js
├── .env
├── package.json

```

---

## 🔧 Environment Variables (`.env`)
```

DEFAULT_MAIL_HOST=smtp.gmail.com
DEFAULT_MAIL_PORT=587
DEFAULT_MAIL_USER=[example@gmail.com](mailto:example@gmail.com)
DEFAULT_MAIL_PASS=yourpassword
DEFAULT_MAIL_FROM=Your App [example@gmail.com](mailto:example@gmail.com)

```

---

## 📦 Installation

### 1. Install dependencies
```

npm install

```

### 2. Start the server
```

npm start

```

Server runs by default on:
```

[http://localhost:3000](http://localhost:3000)

````

---

## 📚 API Endpoints

### **POST** `/api/mail/send`  
Send an email using either default SMTP or custom SMTP.

---

### ✅ **Send using DEFAULT SMTP (from .env)**

**Request Body**
```json
{
  "to": "user@example.com",
  "subject": "Hello",
  "text": "This is a test message"
}
````

---

### ✅ **Send using CUSTOM SMTP**

**Request Body**

```json
{
  "to": "user@example.com",
  "subject": "Hello",
  "text": "Custom SMTP Email",
  "smtp": {
    "host": "smtp.office365.com",
    "port": 587,
    "user": "custom@outlook.com",
    "pass": "yourpass",
    "from": "My App <custom@outlook.com>"
  }
}
```

---

## 🖥️ Documentation UI

Visit:

```
will revel soon
```

This serves your custom `index.html` documentation page.

---

## 📜 License

This project is free to use for personal and commercial purposes.

---

If you want, I can generate the **index.html docs page** also.
