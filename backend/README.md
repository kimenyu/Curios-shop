# Web Application Development Prototype Submission

## Overview
This prototype submission demonstrates the development of an e-commerce web application, focusing on frontend and backend functionalities, database management, integration, and deployment. The submission includes explanations and reasoning for each task completed.

### Project Details
- **Project Title:** E-commerce Site Development Prototype
- **Submission Date:** 17/2/2024

## Task 1: Frontend Development
The frontend was developed using the React.js framework to create a customer-facing interface for browsing artifacts and curios. Key functionalities implemented include:
1. Displaying artifacts and curios with relevant details such as name, description, and price.
2. Implementing search and filter functionalities for easy navigation through the product catalog.
3. Designing the interface with responsiveness to ensure optimal viewing across various devices.

## Task 2: Backend Development [link to api documentation](https://njorogekimenyu.pythonanywhere.com/api/swagger/)
Backend functionalities were implemented using Django Rest Framework to handle user authentication and authorization. APIs were developed for:
1. User registration and authentication, including password hashing for security.
2. Authorization checks to restrict access to merchant-specific features. I added a permission on views only for merchants to access specfic features. e.g their curio/prodcut deletion, on creating a product/curio.
3. Security measures to protect against common vulnerabilities. I validated user input, i also used Django's CSRF middleware to protect against CSRF attacks. I also enabled cors for the frontend domain.


## Task 3: Database Management
A relational database schema was designed using PostgreSQL to store user data, product information, and transaction records. Key aspects considered include:
1. Tables/entities for users, products, orders, and services. [Link to entity relationship](https://drawsql.app/teams/house-2/diagrams/tch)
2. Appropriate relationships (one-to-many, many-to-many) between entities. Check the link above
3. Ensuring data integrity and implementing mechanisms for scalability.

## Task 4: Integration and Deployment
Frontend and backend components were integrated into a cohesive web application. Deployment was carried out using PythonAnywhere for the backend and Vercel for the frontend. The deployment process included:
1. Testing methodologies to ensure functionality and performance.
2. Utilization of PythonAnywhere and Vercel platforms for deployment.
3. Measures for scalability, reliability, and security post-deployment.


### Repository Contents
- **Frontend:** React.js framework used for frontend development.
- **Backend:** Django Rest Framework employed for backend development.
- **Database:** Relational database schema designed using Mysql.
- **Deployment:** Backend deployed on PythonAnywhere, frontend deployed on Vercel.
- **Documentation:** Code explanations and reasoning provided in this README.

### Repository Link
[Link to Repository](https://github.com/kimenyu/Curios-shop.git)

