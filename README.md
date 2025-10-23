# Health Hub

A Django-based doctor recommendation system similar to 1mg, where users can search for doctors by specialization and location.

## Features

- **Home Page**: Welcome message with search functionality
- **Doctors List**: Browse and search doctors by name, specialization, or location
- **Doctor Details**: View comprehensive information about individual doctors
- **About Page**: Information about the Health Hub platform
- **Admin Panel**: Manage doctors through Django admin interface
- **Responsive Design**: Bootstrap 5 for mobile-friendly UI

## Technologies Used

- **Backend**: Django 5.2
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Database**: SQLite (default Django database)
- **Styling**: Custom CSS with Bootstrap components

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Steps to Run Locally

1. **Clone or Download the Project**
   ```
   # If cloning from repository
   git clone <repository-url>
   cd healthhub
   ```

2. **Create and Activate Virtual Environment**
   ```
   python -m venv my_dj_env
   # On Windows:
   my_dj_env\Scripts\activate
   # On macOS/Linux:
   source my_dj_env/bin/activate
   ```

3. **Install Dependencies**
   ```
   pip install django
   ```

4. **Run Migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser (Admin)**
   ```
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin username and password.

6. **Run the Development Server**
   ```
   python manage.py runserver
   ```

7. **Access the Application**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### Adding Doctors

1. Log in to the admin panel using the superuser credentials
2. Navigate to "Doctors" section
3. Click "Add Doctor" to create new doctor entries
4. Fill in the required fields: name, specialization, location, experience, contact

### Searching for Doctors

- Use the search bar on the home page or doctors list page
- Search by doctor's name, specialization, or location
- Results are displayed in card format with key information

### Viewing Doctor Details

- Click "View Details" on any doctor card to see full information
- Contact information is displayed for easy access

## Project Structure

```
healthhub/
├── healthhub/              # Main project directory
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── doctors/                # Doctors app
│   ├── __init__.py
│   ├── admin.py            # Admin configuration
│   ├── apps.py
│   ├── models.py           # Doctor model
│   ├── tests.py
│   ├── urls.py             # App URL configuration
│   └── views.py            # View functions
├── templates/              # HTML templates
│   └── doctors/
│       ├── base.html       # Base template
│       ├── home.html       # Home page
│       ├── doctors_list.html # Doctors list page
│       ├── doctor_detail.html # Doctor detail page
│       └── about.html      # About page
├── static/                 # Static files
│   └── css/
│       └── custom.css      # Custom styles
├── db.sqlite3              # Database file (created after migration)
├── manage.py               # Django management script
└── README.md               # This file
```

## Customization

### Adding More Fields to Doctor Model

1. Edit `doctors/models.py` to add new fields
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. Update templates and admin configuration as needed

### Styling Changes

- Modify `static/css/custom.css` for custom styles
- Override Bootstrap classes in templates

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues, please create an issue in the repository or contact the development team.
