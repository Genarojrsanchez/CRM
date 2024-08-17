# Django CRM System

A lightweight Customer Relationship Management (CRM) system built with Python and Django. This project is designed to manage customer information and track orders, demonstrating the core functionalities of a typical CRM.

## Features

- **Customer Management**: Add, edit, and delete customer records, including names, emails, phone numbers, and addresses.
- **Order Management**: Track customer orders with details like product names, quantities, and order dates.
- **User Interface**: Clean and intuitive UI for easy navigation and management.
- **Security**: Integrated Django’s built-in security features for safe data handling.

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/django-crm.git
   cd django-crm
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser**:

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:

   Open your browser and go to `http://127.0.0.1:8000/` to view the CRM system.

## Usage

- **Customers**: View, add, edit, and delete customer information.
- **Orders**: Manage orders linked to customers, tracking products and quantities.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes. For major changes, it's recommended to open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

You can paste this entire code block into your `README.md` file, and it will display the steps properly when viewed on GitHub, including the code blocks for the commands under each step.
