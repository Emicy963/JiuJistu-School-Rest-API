# Training Management API

A Django-based REST API for managing martial arts students, tracking their progress, and handling class attendance. Built with Django Ninja for efficient API development.

## Features

- Student Management (CRUD operations)
- Belt Progression Tracking
- Class Attendance Recording
- Progress Monitoring
- Age-based Belt Restrictions

## Technologies

- Python 3.x
- Django
- Django Ninja
- SQLite (default database)

## Installation

1. Clone the repository

```bash
git clone https://github.com/Emicy963/JiuJistu-School-Rest-API
cd JiuJistu-School-Rest-API
```

2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run migrations

```bash
python manage.py migrate
```

5. Start the development server

```bash
python manage.py runserver
```

## API Endpoints

### Students

- `POST /api/` - Create a new student
- `GET /api/students/` - List all students
- `PUT /api/students/{student_id}` - Update student information
- `GET /api/progress_student/?email_student={email}` - Get student progress

### Class Management

- `POST /api/class_held/` - Record completed classes

## Data Models

### Student

- `name`: String (max length 255)
- `email`: Email (unique)
- `date_birth`: Date
- `belt`: Choice (B-White, A-Blue, R-Purple, M-Brown, P-Black)

### CompletedClass

- `student`: ForeignKey to Student
- `date`: Date
- `now_belt`: String (current belt when class was completed)

## Belt System

The API implements a structured belt progression system:

- White Belt (B)
- Blue Belt (A)
- Purple Belt (R)
- Brown Belt (M)
- Black Belt (P)

Note: Students under 18 years old cannot receive Blue, Purple, Brown, or Black belts.

## Input Validation

- Email must be unique for each student
- Class quantity must be greater than zero
- Age restrictions are enforced for belt progression
- Belt assignments are validated against the defined choices

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

## License

This project is under the MIT license. View the archive `LICENSE` for more details.

## Contact

Cafu Dev [Emicy963](https://github.com/Emicy963)
