Customer Dashboard
==================

Overview
--------

The Customer Dashboard is an integral component of the General Maintenance Management System (GMMS). It provides customers with an interactive interface to submit new maintenance requests and manage their personal information. The dashboard is designed to be user-friendly, ensuring a seamless experience for customers engaging with maintenance services.

Functionality
-------------

The dashboard is structured to offer comprehensive functionalities:

- **Navigation Bar**: Facilitates basic navigation and session management.
- **Flash Messages**: Displays messages back to the user (e.g., success or error messages).
- **Request Form**: Allows customers to submit new maintenance requests directly through the dashboard.

Key Components
--------------

Navigation Bar
^^^^^^^^^^^^^^

The navigation bar at the top provides a consistent navigational interface and includes a logout option for user session management:

.. code-block:: html

    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">GMMS</a>
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="#" id="logoutBtn">Logout</a>
                </li>
            </ul>
        </div>
    </nav>

Flash Messages
^^^^^^^^^^^^^^

Flash messages are used to provide feedback to the user after actions such as form submission:

.. code-block:: html

    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}" role="alert">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}

Customer Request Form
^^^^^^^^^^^^^^^^^^^^^

The form within the dashboard allows customers to submit detailed maintenance requests, providing necessary details that are required for processing:

.. code-block:: html

    <form id="requestForm" method="post">
        <div class="form-group">
            <label for="firstName">First Name</label>
            <input type="text" class="form-control" id="first_name" name="first_name" required>
        </div>
        <div class="form-group">
            <label for="lastName">Last Name</label>
            <input type="text" class="form-control" id="last_name" name="last_name" required>
        </div>
        <!-- Additional form fields -->
        <button type="submit" class="btn btn-primary submit-btn">Submit</button>
    </form>

Interactive JavaScript
----------------------

JavaScript enhances the user interface by handling interactive elements such as the logout process:

.. code-block:: javascript

    document.getElementById('logoutBtn').addEventListener('click', function(event) {
        event.preventDefault();
        window.location.href = '/auth?form_type=login';
    });

User Interactions
-----------------

Customers interact with the dashboard primarily through:

- **Logging Out**: By clicking the logout button, effectively ending their session.
- **Form Submission**: By filling out and submitting the maintenance request form, initiating a service request.

Conclusion
----------

The Customer Dashboard is crucial for enabling direct customer engagement with the maintenance management process. It simplifies the process of requesting services and provides immediate feedback and updates through a clean, intuitive interface.

