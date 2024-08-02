Technician Dashboard
====================

Overview
--------

The Technician Dashboard is a crucial interface within the General Maintenance Management System (GMMS). It provides technicians with a centralized and interactive platform to view, manage, and complete work orders. This dashboard is dynamically linked to the backend systems, ensuring real-time updates and interactions.

Functionality
-------------

The dashboard features several key components that enhance the user experience and operational efficiency:

- **Navigation Bar**: Allows users to navigate the system or log out.
- **Sidebar**: Lists work orders that have been approved and are awaiting action.
- **Content Area**: Displays detailed information about the selected work order and allows technicians to complete them.

Key Components
--------------

Navigation Bar
^^^^^^^^^^^^^^

The navigation bar provides basic navigation options and user session management. Here is how it's structured:

.. code-block:: html

    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">GMMS</a>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#" id="logoutBtn">Logout</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

Sidebar for Work Orders
^^^^^^^^^^^^^^^^^^^^^^^

The sidebar dynamically lists the approved work orders, providing a quick overview and access to their details:

.. code-block:: html

    <div class="sidebar">
        <h4>Approved Work Orders</h4>
        <div id="work-orders-list" class="list-group">
            {% for work_order in approved_work_orders %}
            <a href="#" class="list-group-item list-group-item-action" data-id="{{ work_order.id }}">
                <strong>{{ work_order.first_name }} {{ work_order.last_name }}</strong>
                <p>{{ work_order.description | truncate(50) }}</p>
            </a>
            {% endfor %}
        </div>
    </div>

Content Area
^^^^^^^^^^^^

Details of selected work orders are displayed in the main content area, allowing technicians to review and complete tasks:

.. code-block:: html

    <div class="content">
        <div id="work-order-details" class="dashboard-container" style="display: none;">
            <h2>Work Order Details</h2>
            ...
        </div>
    </div>

Interactive JavaScript
----------------------

The dashboard uses JavaScript extensively for dynamic interactions, particularly for handling work order selections and completions:

.. code-block:: javascript

    document.getElementById('work-orders-list').addEventListener('click', function(event) {
        if (event.target.closest('.list-group-item')) {
            event.preventDefault();
            const id = event.target.closest('.list-group-item').getAttribute('data-id');
            fetch(`/technician/work_order/${id}`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById('work-order-details').style.display = 'block';
                    ...
                });
        }
    });

    document.getElementById('complete-btn').addEventListener('click', function() {
        ...
    });

User Interactions
-----------------

Technicians interact with the dashboard through various elements:

- **Logging Out**: By clicking the logout button in the navigation bar.
- **Viewing Work Orders**: By selecting work orders from the sidebar, which loads their details into the content area.
- **Completing Work Orders**: By filling out details in the content area and submitting them for completion.

Conclusion
----------

The Technician Dashboard is designed to streamline the workflow of maintenance technicians by providing a user-friendly and responsive interface to manage work orders efficiently.

