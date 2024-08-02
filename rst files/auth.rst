Authentication Page
===================

Overview
--------

The Authentication page of the General Maintenance Management System (GMMS) serves as the gateway for users to log in to or register for the system. This page supports different user roles, including customers, technicians, and approvers, providing secure access through separate login and registration forms.

Functionality
-------------

The authentication page facilitates two primary functions:

- **User Registration**: Allows new users to register by providing necessary personal and login information.
- **User Login**: Enables existing users to log into the system using their credentials.

Key Components
--------------

Flash Messages
^^^^^^^^^^^^^^

Feedback to users about their interaction with the login and registration processes is displayed through flash messages:

.. code-block:: html

    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}" role="alert">
                    <span class="icon"></span>{{ message }}
                </div>
            {% endfor %}
        {% endif %}
    {% endwith %}

Registration Form
^^^^^^^^^^^^^^^^^

New users can register for the system by filling out the registration form which captures all necessary details:

.. code-block:: html

    <div class="form-box register">
        <h1>Register</h1>
        <form method="post" action="{{ url_for('auth.auth') }}">
            <!-- Form fields for registration -->
            <button type="submit" class="btn btn-primary mt-3">Register</button>
        </form>
    </div>

Login Form
^^^^^^^^^^

Existing users can log into the system by providing their username and password in the login form:

.. code-block:: html

    <div class="form-box login">
        <h1>Login</h1>
        <form method="post" action="{{ url_for('auth.auth') }}">
            <!-- Form fields for login -->
            <button type="submit" class="btn btn-primary mt-3">Login</button>
        </form>
    </div>

Form Styling
^^^^^^^^^^^^

Both forms are styled distinctively to visually differentiate the registration and login processes:

.. code-block:: css

    .form-box.register { background-color: #5a5a5a; }
    .form-box.login { background-color: #333; }

User Interactions
-----------------

- **Registration**: Users complete the registration form with their details and submit it to create a new account.
- **Login**: Users enter their login credentials to access their accounts.
- **Flash Messages**: Users receive immediate feedback through flash messages displayed at the top of the forms.

Dynamic Behavior
----------------

JavaScript enhances user interaction by managing flash message visibility and other dynamic elements on the page:

.. code-block:: javascript

    window.addEventListener('DOMContentLoaded', (event) => {
        const alertElement = document.querySelector('.alert.alert-success');
        if (alertElement) {
            setTimeout(() => {
                alertElement.style.display = 'none';
            }, 5000);
        }
    });

Conclusion
----------

The Authentication page is crucial for ensuring secure access to the GMMS, supporting different user roles through tailored login and registration functionalities. It provides a clear, user-friendly interface for all types of users to engage with the system effectively.

