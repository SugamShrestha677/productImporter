# Product Importer

A Django project for importing and managing products.

## Features
- Product upload and management
- Excel file import
- Admin interface

## Setup
1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```sh
   python manage.py migrate
   ```
4. Start the development server:
   ```sh
   python manage.py runserver
   ```

## Usage
- Access the admin panel at `/admin`.
- Upload products using the provided interface.

## Folder Structure
- `importer/` - Django project settings
- `products/` - Product app (models, views, etc.)
- `templates/` - HTML templates

## License
MIT
