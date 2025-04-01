# The Network (Backend)
A prototype backend for a social media network.
Using SQLAlchemy and FastAPI.

# Running
In general, I test using the included Docker compose file for the database.

The following enviromental variables are used by the compose file, and the server itself.
```bash
DB_NAME # Name of the Database
DB_USER # The username of the database user
DB_PASSWORD # Database User's Password (Used by the Compose as well)
DB_HOST # hostname/ip of the DB Server
DB_PORT # Port of the DB Server.
```