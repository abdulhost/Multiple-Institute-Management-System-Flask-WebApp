# School Management System

A Flask-based web application mimicking eSkooly Pro, with dashboards, modules, demo mode, multi-language support, and payment integration.

## Setup

1. **Install Dependencies**:
   - Ensure Python 3.8+, Node.js, and SQLite are installed.
   - Run:
     ```bash
     # Linux/Mac
     chmod +x setup.sh
     ./setup.sh
     ```
     ```cmd
     # Windows
     setup.bat
     ```

2. **Configure Environment**:
   - Create `.env`:
     ```env
     SECRET_KEY=your-secret-key-here
     JWT_SECRET_KEY=your-jwt-secret-key-here
     PAYPAL_CLIENT_ID=your-paypal-client-id
     STRIPE_SECRET_KEY=your-stripe-secret-key
     ```

3. **Run Application**:
   - Activate venv:
     ```bash
     # Linux/Mac
     source venv/bin/activate
     ```
     ```cmd
     # Windows
     venv\Scripts\activate
     ```
   - Run:
     ```bash
     python app.py
     ```
   - Open `http://localhost:5000`.

## Features
- Dashboards for Super Admin, Admin, Headmaster, Teacher, Student, Parent
- Modules: Students, Attendance, Exams, Grades, Timetable, Fees, Payroll, Library, Inventory, Transport, Hostel, Notifications, Reports
- Try Demo mode (read-only, 15-minute timeout)
- Multi-language support (English, Arabic, Hindi)
- Payment integration (QR code, PayPal, Stripe)

## Troubleshooting
- Ensure `.env` keys are set.
- Change port in `app.py` if `localhost:5000` is busy.
- Run `pip install -r requirements.txt` if setup fails.