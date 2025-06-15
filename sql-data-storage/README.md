# SQL Data Storage Project

This project implements a scalable SQL data storage solution. It is designed to facilitate the ingestion, storage, and management of data using a structured approach with an Object-Relational Mapping (ORM) framework.

## Project Structure

- **src/**: Contains the source code for the application.
  - **db/**: Contains database-related files.
    - **connection.py**: Establishes a connection to the SQL database.
    - **models.py**: Defines the data models (tables) for the SQL database.
    - **utils.py**: Contains utility functions for database operations.
  - **ingest/**: Contains files responsible for data ingestion.
    - **load_data.py**: Loads data into the SQL database.
  - **main.py**: Entry point for the application.

- **requirements.txt**: Lists the dependencies required for the project.

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd sql-data-storage
   ```

2. **Install Dependencies**
   Ensure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure Database Connection**
   Update the database connection settings in `src/db/connection.py` to match your SQL database configuration.

4. **Run the Application**
   Execute the main application:
   ```
   python src/main.py
   ```

## Usage

- The application will connect to the specified SQL database and load data as defined in `src/ingest/load_data.py`.
- Modify the data loading logic in `load_data.py` to suit your data sources.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.