Approver Dashboard
==================

Overview
--------

The Approver Dashboard within the General Maintenance Management System (GMMS) serves as the control panel for approvers to review, approve, or reject work requests. It facilitates efficient management of pending requests and ensures a streamlined process for handling maintenance tasks.

Functionality
-------------

This dashboard allows approvers to:

- View a list of pending work requests.
- Access detailed information for each request.
- Make decisions to approve or reject requests directly from the dashboard.

Key Components
--------------

Navigation Bar
^^^^^^^^^^^^^^

The navigation bar provides essential links and a logout option, ensuring easy navigation and secure session management:

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

Sidebar: Work Requests
^^^^^^^^^^^^^^^^^^^^^^

The sidebar lists all pending work requests, enabling quick navigation and selection of specific tasks for detailed review:

.. code-block:: html

    <div class="sidebar">
        <h4>Work Requests</h4>
        <div id="work-orders-list" class="list-group">
            {% for work_order in pending_work_orders %}
            <a href="#" class="list-group-item list-group-item-action" data-id="{{ work_order.id }}">
                <strong>{{ work_order.first_name }} {{ work_order.last_name }}</strong>
                <p>{{ work_order.description | truncate(50) }}</p>
            </a>
            {% endfor %}
        </div>
    </div>

Content Area: Work Order Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The main content area displays detailed information about a selected work request, along with options to approve or reject:

.. code-block:: html

    <div class="content">
        <div id="work-order-details" class="dashboard-container" style="display: none;">
            <h2>Work Order Details</h2>
            <p><strong>Customer Name:</strong> <span id="customer-name"></span></p>
            <p><strong>Email Address:</strong> <span id="email-address"></span></p>
            ...
            <button id="approve-btn" class="btn btn-success">Approve</button>
            <button id="reject-btn" class="btn btn-danger">Reject</button>
        </div>
    </div>

Interactive JavaScript
----------------------

Dynamic interactions within the dashboard are handled through JavaScript, enhancing user experience by providing real-time response and updates:

.. code-block:: javascript

    document.getElementById('work-orders-list').addEventListener('click', function(event) {
        if (event.target.closest('.list-group-item')) {
            event.preventDefault();
            const id = event.target.closest('.list-group-item').getAttribute('data-id');
            fetch(`/approver/work_order/${id}`)
                .then(response => response.json())
                .then(data => {
                    document.getElementById('work-order-details').style.display = 'block';
                    ...
                });
        }
    });

User Interactions
-----------------

Approvers use the dashboard to:

- **Log Out**: Securely exit the dashboard.
- **Review Requests**: Click on any work request to view its details.
- **Make Decisions**: Use the 'Approve' or 'Reject' buttons to finalize the status of requests.

Conclusion
----------

The Approver Dashboard is designed to empower approvers with the tools they need to efficiently manage and respond to maintenance requests, ensuring timely processing and high operational standards within the GMMS.

