# Miniature Invoicing Module

A simple invoicing application built on the **Frappe Framework** to showcase full-stack development skills, including schema design, backend logic, and cloud deployment.

## 🚀 Key Features

* **Invoice Management**: Create, view, and manage invoices.
* **Automatic Calculations**: The system automatically calculates line-item totals and the grand total for each invoice.
* **Role-Based Permissions**: Implemented user roles and permissions to control access to the application.
* **Public-Facing Website**: A basic website page to describe the application, demonstrating Frappe's CMS capabilities.

## 💻 Technology Stack

* **Framework**: Frappe Framework (Python)
* **Frontend**: Frappe Desk (JavaScript)
* **Database**: MariaDB
* **Backend Services**: Redis
* **Environment**: Python 3, Node.js
* **Deployment**: Google Cloud Platform (GCP) running Ubuntu 22.04

## 💡 The Problem-Solving Journey

The primary goal was to build a simple, working application from scratch. This involved overcoming several real-world technical challenges that demonstrated core skills beyond just coding:

1.  **Server Setup & Resource Management**: The initial GCP free-tier server was not configured for development. We successfully resolved **Out of Memory** (SIGKILL: 9) errors by creating a 2GB swap file and fixed **Out of Disk Space** errors by resizing the hard drive to 30 GB.
2.  **Environment Configuration**: Manually installed and configured missing dependencies like Node.js, Yarn, and Cron, and opened the necessary firewall ports on GCP.
3.  **Debugging**: Diagnosed and fixed persistent server startup issues that were caused by subtle configuration errors in the application's hooks, showcasing attention to detail and a systematic debugging process.

## 📊 Application Schema

The application is built around a simple, relational database schema using three main DocTypes:

* **`Customer`**: A master DocType to store customer information (name, email, phone).
* **`Invoice Item`**: A child DocType that links to the main `Invoice` and stores details for a single item (item name, quantity, rate, amount).
* **`Invoice`**: The main transactional DocType that links to a `Customer` and contains a table of `Invoice Item` records.

## ⚙️ How to Set Up

1.  **Clone the repository**: `git clone [repository-url]`
2.  **Install Frappe Bench**: Follow the official Frappe installation guide for a development environment.
3.  **Copy the code**: Copy the contents of the `app_code/` directory into your `frappe-bench/apps/` directory.
4.  **Install the app**: Run `bench --site [your-site-name] install-app invoicing`
5.  **Start the server**: Run `honcho start` and access the application at `http://[your-server-ip]:8000`.

## 📄 License

This project is licensed under the MIT License.
