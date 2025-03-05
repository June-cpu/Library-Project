# Library Management System

## 📌 Project Overview

This project is a **Library Management System** built using Flask and Python. It allows users to add books, register members, borrow, and return books. The system maintains a structured catalog using a **Binary Search Tree (BST)** for efficient book searching.

## 🚀 Features

- **Book Management:** Add, search, borrow, and return books.
- **Member Registration:** Register members with unique IDs.
- **Flask Web Interface:** Simple web-based UI to interact with the library.
- **BST Catalog:** Uses a **Binary Search Tree** to store and manage books efficiently.
- **Flash Messages:** Displays feedback messages for user actions.
- **Testing Module:** Includes unit tests for library functionalities.
- **Styled UI:** Uses **HTML & CSS** to present a clean interface.

## 📂 Project Structure

```
📦 library-management
├── app.py          # Main Flask application
├── library.py      # Core Library, Book, Member, and BST logic
├── tests.py        # Unit tests for the system
├── templates/
│   ├── index.html  # Web interface
├── static/
│   ├── styles.css  # CSS styles for UI
├── README.md       # Project documentation
```

## 🔧 Setup & Installation

### 1️⃣ Clone the Repository

```sh
git clone <repository-url>
cd library-management
```

### 2️⃣ Create a Virtual Environment (Recommended)

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```sh
python app.py
```

The server will start, and you can access it at `http://127.0.0.1:5000/`.

## 🎨 API Endpoints

| Endpoint       | Description                               |
| -------------- | ----------------------------------------- |
| `/`            | Home page (Library Dashboard)             |
| `/add_book`    | Adds a new book                           |
| `/add_member`  | Registers a new member                    |
| `/borrow_book` | Allows a member to borrow a book          |
| `/return_book` | Allows a member to return a borrowed book |

## 🧪 Running Tests

To run the unit tests, execute:

```sh
python tests.py
```

## 📝 Future Improvements

- Implement a **database** for persistent storage.
- Add **user authentication** for better security.
- Introduce **RESTful API** endpoints for external integrations.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests to improve the system!

📌 **Created by:** [Junaid Tafader]

