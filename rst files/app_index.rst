Welcome Page
============

Overview
--------

The Welcome Page of the General Maintenance Management System (GMMS) serves as the initial landing page for all users. It provides a brief introduction to the system and guides users to the authentication process for further interaction.

Design and Layout
-----------------

The page is designed with simplicity and user engagement in mind, featuring a full-screen background image and an overlay centering the introductory text and call-to-action button.

Background
^^^^^^^^^^

The background of the page sets the tone for the user experience with a full-cover image that relates to the theme of maintenance management.

.. code-block:: html

    body {
        background-image: url('https://reftech.id/wp-content/uploads/2022/11/ezgif.com-gif-maker-2.jpg');
        background-size: cover;
        background-position: center;
    }

Overlay Content
^^^^^^^^^^^^^^^

A semi-transparent overlay contains the welcome message and the 'Get Started' button, ensuring readability against the background image.

.. code-block:: html

    <div class="overlay">
        <h1>Welcome To The GMMS</h1>
        <p>GMMS (General Maintenance Management System) helps you manage and track all your maintenance requests efficiently. Whether you're a technician, approver, or customer, our system ensures smooth operations and timely maintenance management.</p>
        <button class="btn btn-primary get-started-btn" onclick="window.location.href ='/auth?form_type=login'">Get Started</button>
    </div>

Text and Button Styling
^^^^^^^^^^^^^^^^^^^^^^^

The text within the overlay is styled for clear visibility and aesthetic appeal, while the button is designed to prompt user action.

.. code-block:: css

    .overlay {
        background-color: rgba(0, 0, 0, 0.7);
        color: white;
        padding: 40px;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .overlay h1, .overlay p {
        font-size: 2rem;
    }
    .overlay p {
        font-size: 1.2rem;
        margin: 20px 0;
    }
    .get-started-btn {
        margin-top: 30px;
        font-size: 1.2rem;
        padding: 10px 20px;
    }

User Interaction
----------------

The primary interaction on this page is the 'Get Started' button, which directs users to the authentication page where they can log in or register.

.. code-block:: javascript

    <button class="btn btn-primary get-started-btn" onclick="window.location.href ='/auth?form_type=login'">Get Started</button>

Conclusion
----------

The Welcome Page is thoughtfully designed to introduce the GMMS and guide users smoothly into the system. It ensures that users are well-informed about the system's purpose before proceeding to log in or register, setting the stage for a seamless user experience.

