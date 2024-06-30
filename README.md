# API Webserver
## R1 Explain the problem that this app will solve, and explain how this app solves or addresses the problem.

#### Event Management and Registration:
To arrange and handle events is not a simple job. It needs many steps like creating events, managing registrations, tracing attendees, and making sure that all data is saved correctly for easy access when required. Those who participate in the event may also find it difficult to locate an event, register for it and keep track of events they are interested in.
##### Common Issues:
* Event Organization: Coordinating event details like date, time, location, and capacity.
* Registration Management: Handling attendee registrations, including confirming attendance and managing capacities.
* User Management: Ensuring secure user data handling, including roles for organizers and attendees.
#### Solution Overview
The suggested app tackles these problems head-on with a robust event management framework. Users can generate, handle and sign up for events through this system. Let's see how it resolves the particular issues:
##### Event Creation and Management:
* Event Details: Those who arrange events can make events with all the needed details like title, description, date and time, place, organizer details, capacity and status.
* CRUD Operations: The application allows for Create, Read, Update and Delete (CRUD) operations on events. Organizers can effectively handle event details.
##### Registration Management:
* Registration of Attendees: People can sign up for events, and the application will keep a record of their registration information such as status and extra details.
* Capacity Management: The app aids in managing the capacity of an event. It avoids excessive registration and assists with handling attendees effectively.
##### User Management:
* User Roles: The system differentiates between organizers and attendees in order to allow the right access and functionalities based on user roles.
* Data Handling that is Secure: The application manages user data safely by saving passwords in hashed form and guaranteeing protection for all user details.
#### Detailed Breakdown
##### Event Management:
* Create Events: Organizers can make new events by giving needed details. The plan for the event takes care of the method to include events into database.
* View Events: The event blueprint shows a list of all events to both the people who organized them and those attending. Event data is fetched from database by the event blueprint and presented in an easy-to-understand manner.
* Update Events: If there are any changes, organizers can alter event details. The event blueprint is responsible for saving updated information in a correct manner.
* Delete Events: If there are events that have passed or become irrelevant, organizers have the ability to delete them. This helps in maintaining an updated and relevant list of events.
##### User Management:
* Register Users: For new users to sign up, they should give a username, an email and a password. The user blueprint makes sure this information is kept safe.
* Roles for Users: People using the app may possess different roles, like "organizer" or "attendee", that impact their abilities within this application.
* User Authentication: Users can log in securely, with their credentials verified against stored data.
##### Attendee Management:
* Event Registration: People can register for events they want to participate in. The attendee blueprint controls the registration details, linking persons with events.
* Track Registration: The app knows who comes to each event and handles their registration.
* Manage Capacity: The app stops over-registration by verifying the event's maximum capacity before accepting new registrations.

This app makes it easier to organize and handle events, giving a simple solution for those who arrange the event as well as people participating in it. It manages event details, user information and registration processes effectively. The app is easy to use, dealing with typical problems encountered when managing an event

## R2 Describe the way tasks are allocated and tracked in your project
	

Describe the way tasks are allocated and tracked in your project.

## R3 List and explain the third-party services, packages and dependencies used in this app.

1. Alembic (1.13.2)

    Purpose: Database migrations.
    Use: Manages schema changes over time using migrations, which are version-controlled updates to the database schema.

2. Blinker (1.8.2)

    Purpose: Signal handling.
    Use: Implements a signaling framework for event-driven programming, often used in Flask for event notifications.

3. Click (8.1.7)

    Purpose: Command-line interface (CLI) creation.
    Use: Facilitates writing simple and complex command-line interfaces for scripts.

4. Flask (3.0.3)

    Purpose: Web framework.
    Use: Core framework for building web applications in Python.

5. Flask-JWT-Extended (4.6.0)

    Purpose: JWT authentication.
    Use: Adds support for JSON Web Tokens (JWTs) for securing routes and handling authentication.

6. Flask-Marshmallow (1.2.1)

    Purpose: Object serialization/deserialization.
    Use: Integrates Marshmallow with Flask to handle the serialization of objects to JSON and vice versa.

7. Flask-Migrate (4.0.7)

    Purpose: Database migrations.
    Use: Extension for handling database migrations using Alembic with Flask applications.

8. Flask-SQLAlchemy (3.1.1)

    Purpose: Database integration.
    Use: Simplifies database interactions by integrating SQLAlchemy with Flask, providing ORM capabilities.

9. Greenlet (3.0.3)

    Purpose: Lightweight concurrent programming.
    Use: Used internally by libraries like Gevent to manage lightweight, in-process threads.

10. Itsdangerous (2.2.0)

    Purpose: Data security.
    Use: Provides a way to sign data to ensure it hasn’t been tampered with, often used in session management.

11. Jinja2 (3.1.4)

    Purpose: Templating engine.
    Use: Renders HTML templates with dynamic data in Flask applications.

12. Mako (1.3.5)

    Purpose: Templating engine.
    Use: An alternative templating engine to Jinja2, known for performance and flexibility.

13. MarkupSafe (2.1.5)

    Purpose: HTML escaping.
    Use: Ensures that strings are safe for rendering in HTML by escaping special characters.

14. Marshmallow (3.21.3)

    Purpose: Object serialization/deserialization.
    Use: Handles serialization of Python objects to JSON format and validation of incoming data.

15. Marshmallow-SQLAlchemy (1.0.0)

    Purpose: SQLAlchemy integration.
    Use: Extends Marshmallow to work with SQLAlchemy models, simplifying schema creation.

16. Packaging (24.1)

    Purpose: Package version handling.
    Use: Used for parsing and handling package versions, dependencies, and packaging-related tasks.

17. Psycopg2-binary (2.9.9)

    Purpose: PostgreSQL adapter.
    Use: Allows Python applications to connect to PostgreSQL databases using a binary distribution.

18. PyJWT (2.8.0)

    Purpose: JWT encoding/decoding.
    Use: Used to encode and decode JSON Web Tokens for secure transmission of information.

19. Python-dotenv (1.0.1)

    Purpose: Environment variable management.
    Use: Loads environment variables from a .env file, useful for configuration management.

20. SQLAlchemy (2.0.31)

    Purpose: Database ORM.
    Use: Provides a full suite of tools for working with relational databases using an ORM.

21. Typing-Extensions (4.12.2)

    Purpose: Type hinting.
    Use: Provides backports of type hints and other typing features for older versions of Python.

22. Werkzeug (3.0.3)

    Purpose: WSGI utilities.
    Use: Offers various utilities for creating WSGI-compatible web applications, including request/response handling.

## R4 Explain the benefits and drawbacks of this app’s underlying database system.

#### Benefits

1. #### Relational Database Capabilities:

* Data Integrity: PostgreSQL keeps data integrity using constraints like primary keys, foreign keys, and others that help in maintaining dependable relationships between tables (for instance Event, User, Attendee).

* ACID Compliance: This means it is reliable for transactions (Atomicity, Consistency, Isolation, Durability), which are very important in keeping data consistency within multiple step operations.

2. #### Scalability and Performance:

* Horizontal Scalability: This can be made to scale horizontally by methods such as sharding and replication, which distribute data across many nodes for better capacity and performance.

* Advanced Indexing: This allows for different methods of indexing (like B-tree, GIN, GiST) which are very useful in enhancing the speed of queries. It is especially advantageous when dealing with complicated queries and big datasets.

3. #### Extensibility and Ecosystem:

* Large ecosystem: Brings many extensions and integrations (such as spatial data using PostGIS, full-text search via pg_trgm) that boost functionality and adaptability of applications.

* Active community: PostgreSQL has a big and active community that provides support, plugins, and ongoing enhancements.

#### Drawbacks

1. #### Setup and Administration Complexity:

* Initial setup: Configuring PostgreSQL could be more complicated compared to simpler databases, needing knowledge in database administration and possibly longer time for setting up.

* Administration: Needs regular care (such as backups, performance adjustments, security upgrades) to guarantee best functioning and dependability.

2. #### Concurrency and Locking:

* Managing concurrency: Managing concurrent access to data and making sure locking methods are used properly is crucial for preventing contention and loss in performance.

* Transaction isolation levels: Selection of right levels of isolation (like READ COMMITTED, REPEATABLE READ) for achieving a trade-off between data consistency and performance.

3. Resource Consumption:

* Operations that require a lot of resources: Certain advanced features and query optimizations could use more resources like CPU or memory, so they need to be properly provisioned and checked.


#### Summary

For applications that need strong relational database features, can grow in size and require transactional consistency, PostgreSQL is a good option. It provides lots of functions for managing data and improving performance. Also, it has a helpful community and can be extended easily. But developers must consider the difficulty of setting up system, managing administration tasks as well as dealing with problems linked to concurrency and resource control.

## R6 Design an entity relationship diagram (ERD) for this app’s database, and explain how the relations between the diagrammed models will aid the database design.

![alt text](docs/ERD.png)

### ERD Overview
1. Entities:
    * User: Contains user information like Username, Email, Password, and Role.
    Organizer: Represents users who manage events, linked to User.
    * Events: Details about events, including Title, Description, DateTime, Location, Capacity, and Status.
    * Attendees: Tracks event attendance, with Registration Date and Status.
2. Relationships:
    * User to Organizer: One-to-one relationship; each organizer is a user.
    * User to Attendees: One-to-many relationship; users can be attendees for multiple events.
    * Events to Attendees: Many-to-many relationship; events have multiple attendees, and users can attend multiple events.
    * Organizer to Events: One-to-many relationship; each organizer manages multiple events.

### How Relationships Aid Database Design
1. Data Integrity:
    * Foreign keys enforce data consistency, ensuring that every organizer and attendee corresponds to a valid user.
2. Scalability:
    * Supports multiple events and attendees without data duplication, accommodating growth in users and events.
3. Flexibility:
    * Users can serve multiple roles (attendee or organizer), simplifying user management and permissions.
4. Normalization:
    * Reduces data redundancy by organizing data into related tables, simplifying maintenance and updates.
5. Security:
    * Role-based access can be implemented, securing sensitive information based on user roles.
