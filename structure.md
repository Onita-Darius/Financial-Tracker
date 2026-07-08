Backend:
    Python 3.14
    FastAPI
    PostgreSQL
    SLQAlchemy

Frontend:
    React + Vite
    React Router

Scope:
    User:
        Register
        Login
        Logout
    Accounts:
        Create
        Edit
        Delete
    Categories:
        Create
        Edit
        Delete
    Transactions:
        Create
        Edit
        Delete
        List


DB Tables:
    Users:
        id, email, username, password, created_at
    Accounts:
        id, user_id, name, balance, created_at, last_transaction
    Categories:
        id, user_id, name, color, icon
    Transactions:
        id, account_id, category_id, amount, type, description, date, created_at, updated_at

API ENDPOINTS:
    POST /register
    POST /login
    GET /me 
    GET /accounts
    POST /accounts
    PATCH /accounts/{id}
    DELETE /accounts/{id}
    GET /categories
    POST /categories
    PATCH /categories/{id}
    DELETE /categories/{id}
    GET /transactions
    POST /transactions
    PATCH /transactions/{id}
    DELETE /transactions/{id}