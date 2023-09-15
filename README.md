# Installation and Setup

## Prerequisites

Before you proceed, make sure you have the following prerequisites installed on your development environment:

1. **PYTHON**: Run this command to check if you have Python installed on your machine `python --version`. If you don't have it installed; download and install Python on your machine here: https://www.python.org/downloads/. 
2. **Web Server**: You can use Uvicorn to run a local server (for local development).
3. **Database**: FastAPI supports multiple database systems, including PostgreSQL, MySQL, SQLite, Oracle, Microsoft SQL Server, etc.
                 Ensure you have one of these databases installed and configured. PostgreSQL was used for this project. Download postgres here: https://www.postgresql.org/download/
4. **Git**: Git is a version control system used for managing the project's source code. Download git here: https://git-scm.com/downloads
    

## Cloning and Preparing the Laravel Application

Follow these steps to clone and prepare the Laravel application:

### 1\. Clone the Repository

Clone the Laravel repository from Github using the following commands:

```bash
git clone git@github.com:rahmanakorede442/hng_task_two.git
 ```

### 2\. Navigate to Your Project Directory

Change your current working directory to the cloned project folder:

```bash
cd hng_task_two
 ```

### 3\. Install Composer Dependencies

Use Composer to install the project's PHP dependencies:

```bash
composer install
 ```

### 4\. Copy the Environment File

Make a copy of the provided `.env.example` file and name it `.env`:

```bash
cp .env.example .env
 ```

Edit the `.env` file to configure your database connection, application URL, and any other necessary configuration options.

### 5\. Generate an Application Key

Generate an application key for your Laravel application:

```bash
php artisan key:generate
 ```

This key is used for encrypting session and cookie data.

### 6\. Migrate the Database

Run the database migrations to create the necessary database tables:

```bash
php artisan migrate
 ```

### 7\. Install JavaScript Dependencies

If the project uses JavaScript libraries or packages, install them using npm or yarn:

```bash
npm install
# or
yarn install
 ```

### 8\. Start the Development Server

To start a development server, use the following Artisan command:

```bash
php artisan serve
 ```

This will start a development server at `http://localhost:8000`. Access your Laravel application by visiting this URL in your web browser.

## Additional Configuration

- **Web Server Configuration**: For production deployments, configure your web server (e.g., Apache, Nginx) to serve your Laravel application. Refer to Laravel's documentation for server configuration details.
- **Environment Configuration**: Review and adjust the settings in the `.env` file as needed for your specific environment.
- **Artisan Commands**: Laravel's Artisan command-line tool provides various commands to manage your application. Use `php artisan` to see the available commands and their descriptions.


_I hope this helps._
