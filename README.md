# Tasty Pizza

![The website is responsive](/document/I-am-responsive.png)

- Demo website:
  [Tasy Pizza](https://tasty-pizza-d95969cf03fc.herokuapp.com/)
- Link to the pizzatasty repo: [Github repo](https://github.com/Dhiaa-alomari/pizzatasty)

# Contents

- [Design](#design)
- [Wireframe](#wireframe)
- [Key Features](#key-features)
- [Admin page](#admin-page)
- [Models](#models)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [Manual testing](#manual-testing)
- [Authentiction testing](#authentication-testing)
- [Bugs](#bugs)
- [Credits](#credits)

## Goals

Website Goals for Tasty Pizza Restaurant

The goal of the Tasty Pizza website is to create a fully functional and user-friendly online platform that allows customers to easily interact with the restaurant and its services. The website aims to enhance the customer experience through the following features:

- Allow users to reserve a table for their preferred date and time using a simple and intuitive booking form.

- Enable users to book multiple tables while ensuring that reservations do not overlap on the same date and time, with at least a one-hour interval between bookings.

- Provide users with the ability to add, edit, or cancel their reservations easily.

- Display the restaurant’s menu in an attractive and organized way so customers can explore available pizza options and dishes.

- Allow users to register and create personal accounts to manage their reservations more efficiently.

- Tasty Pizza is co-owned by two partners who oversee daily operations and manage staff divided into two teams, ensuring the restaurant remains open every day.



## Design

- User-Centered Design

  - The website design is centered around the user experience, with a strong focus on simplicity and ease of navigation. Users can quickly access essential information such as the menu, table reservations, and location details. Clearly defined sections like “Welcome to Tasty Pizza” and “Find Your Best Food” guide visitors smoothly through the website and enhance usability.

- Visual Appeal and Authenticity

  - The homepage features high-quality food photography that highlights the richness and variety of the pizzas. These visuals play a key role in creating an authentic and engaging experience, helping users feel connected to the restaurant and its offerings.

- Minimalistic yet Informative Layout

  - The layout follows a minimalistic approach while still providing all necessary information. Clean sections and concise text allow the visuals to stand out, ensuring users are not overwhelmed. Important details such as contact information, opening hours, and the reservation system remain easily accessible.

- Color Palette

  - The color scheme was carefully selected to reflect the brand identity of Tasty Pizza:

  - Primary Color (#061918): Used for the header and footer to create a strong and elegant foundation.

  - White (#FFFFFF): Applied to backgrounds and text areas to improve readability and contrast.

  - Red (#FF0000): Used as an accent color, especially for active navigation links, to draw attention and enhance interaction.

  - Body Background: black for a soft, neutral feel.

  - Dish Description Background: red, a warm and subtle tone that improves text readability and adds visual comfort.

  - Text Color (Black): Used for meal title and  to maintain clarity and simplicity.

- Typography

  - The typography was chosen to ensure readability while maintaining a modern, professional, and elegant appearance. The selected fonts support clear content presentation and contribute to a consistent visual identity that aligns with the Tasty Pizza brand.

- Design Process
  - Research and Inspiration

  - The design process began with research into modern restaurant websites, focusing on usability, visual aesthetics, and the impact of food imagery on user engagement.

- Branding and Visual Identity

  - Creating a strong brand identity was a key objective. A logo was designed to represent Tasty Pizza’s classic pizza heritage with a modern touch. Colors, fonts, and imagery were carefully selected to convey warmth, authenticity, and a high-quality dining experience.

- Responsive Design

  - Since many users access websites via mobile devices, responsive design was prioritized from the beginning. The layout adapts seamlessly across mobile, tablet, and desktop screens, ensuring a consistent and enjoyable experience on all devices.

- Wireframing and Layout Design

  - Wireframes were used to plan each page layout, emphasizing simplicity and intuitive navigation. The homepage was designed to showcase appealing food imagery alongside clear calls to action, such as exploring the menu and booking a table.

- Finalization and Launch

  - The final design of the Tasty Pizza website delivers a welcoming, vibrant, and user-friendly experience. Every element—from the color palette and typography to imagery and layout—was thoughtfully crafted to engage users, highlight the restaurant’s offerings, and streamline the online reservation process.



## Wireframe.

- Mobile wireframe:

![home page](/document/home-mobile-mockup.png)![menu page](/document/menu-mobile-mockup.png)![register page](/document/register-mobile-mockup.png)

---

- Desktop wireframe:
  ![wireframe for desktop](/document/home-mockup.png)
  ![wireframe for desktop](/document/menu-mockup.png)
  ![wireframe for desktop](/document/register-mockup.png)![wireframe for desktop](/document/login-mockup.png)


## Key Features

- Home page

  - The homepage greets users with a visually appealing image of a delicious meal, immediately capturing attention and setting the mood for the dining experience.
    ![Home-page](/document/homepage-1.png)

  ***

  - A menu of vibrant, high-quality food images offers users a glimpse of the restaurant's dishes, enticing them to explore more or place an order.
    ![Pizza menu page](/document/menupage.png)

  ***

  - The **About Us** section effectively communicates the restaurant’s 15-year journey, emphasizing a deep connection to the pizza world culinary traditions. It tells a story that appeals to both long-time fans and new visitors.
    The text welcomes everyone, from first-time visitors to regulars, making it clear that the experience is more than just about food—it’s about memorable dining moments.
    ![Who is Tasty pizza](/document/homepage-2.png)

  ***

  - The **address** section provides essential contact details and opening hours, ensuring that customers can easily reach the pizza restaurant or plan their visit.
    ![Who is Tasty pizza](/document/homepage-3.png)

---

- Register Page

  - A Friendly Registration Form:

  - The form is simple, allowing users to sign up with minimal effort.
  - Fields include

    - Username:
    - Password:
    - Password Confirmation:
    - login page link.

  - Login page Link for Existing Users:

    - If a user already has an account, they can easily switch to the Login page via the link: **_Already a member? Login._** This reduces friction for returning users, offering a seamless experience.
      ![Register Page](/document/registerpage.png)

---

- Login Page

  - Simple Layout: Clean, minimalist design with a split layout—restaurant image on one side, login form on the other.

  - Login Form: Includes fields for username, password, and a prominent **Login** button for easy access.
  - New User Call to Action: Clear link to register for users without an account, improving user flow.
    ![login form](/document/loginpage.png)

---

- BOOKINGS page

  - Simple Booking Form: Users can easily select a date, time, and number of guests to book a table.

  - Availability Info: Clear indication that the restaurant operates between 11 AM and 11 PM.

  - Confirmation Button: A prominent “Book Now” button to finalize reservations quickly.
    ![booking page](/document/bookingpage.png)

  ***

- Booking page , book table page & edit booking page :
  - Booking Details Display: Shows user’s current booking with details like date, time, and number of guests.
  - Cancel Booking Option: Includes a clear and clickable "Add Booking", "Edit booking" and "Cancel booking". - Click on add booking it will take you to book a table form.
  - Click on edit booking it will take you to booking page with current booking you wish to update it.
  - Click on cancel booking will delete reservation.
    ![my booking page](/document/bookingpage.png)
    ![edit booking page](/document/edit-booking-page.png)
    ![book table page](/document/book-table-page.png)

## Admin page

- This is the Django admin dashboard, a built-in feature that allows superusers to manage and interact with models and data from the web interface.
  - Site administration panel:
    - This panel gives access to different sections of your Django application.
  - Sections and Models:
    - ACCOUNTS:
      - Email addresses: Manage email addresses associated with user accounts.
    - AUTHENTICATION AND AUTHORIZATION:
      - Groups: Manage user groups and permissions.
      - Users: Add, view, edit, or delete users in the application.
    - BOOKING:
      - Bookings: Manage bookings made on the website.
      - Tables: Handle table-related information (likely referring to tables in a restaurant setting).
    - DJANGO SUMMERNOTE:
      - Attachments: Manage file attachments using the Django summernote package.
    - MENU:
      - Manage restaurant menu items and can easily add it here.
    - SITES: Manage configurations related to the **sites** framework, often used for multi-site setups.
    - Recent Actions Panel:
      - On the right side, it displays a list of recent actions performed by the logged-in admin user, such as adding, changing, or deleting objects.(in this case, menu items).
    - Header:
      - The header includes links for the admin to view the site, change the password, and log out.
        ![admin page](/document/admin.page.png)
    ***
    - This is the **Add menu** form in the Django admin interface. It allows the admin to add a new menu item with the following fields:
      - **Name:** The name of the menu item.
      - **Description:** A text area to describe the menu item.
      - **Price:** The cost of the item.
      - **Image:** An option to upload an image for the menu item.
      - At the bottom, there are buttons to save the entry, save and add another item, or save and continue editing the current item.
        ![admin page](/document/add.menu.png)
    ***
    - This is the Django admin interface's "Select booking to change" page. It shows a list of bookings currently stored in the system.
      ![booking admin page](/document/booking.admin.png)
    ***
    - Admin interface for **Table** management:
      This admin panel allows the site owner to manage the restaurant's table capacities easily. Through this interface, the owner can create and configure tables by specifying their seating capacity.
      ![admin page for add table](/document/admin.add.table.png)
    ***
    - Current tables overview in admin panel:
      This section of the admin panel displays the current list of tables available in the restaurant, ordered by their seating capacity. Each table shows its capacity, allowing the site owner to easily manage and modify the table arrangement. The list contains tables with capacities ranging from 1 to 10 seats, giving flexibility to accommodate different group sizes.
      ![admin current table](/document/admincurrent.1.png)

---

## Models

- Booking Model.
- Represents a reservation made by a user for a table.
  - user: Many-to-One → A user can have multiple bookings, but each booking belongs to one user.
  - table: Many-to-One → A table can have multiple bookings, but each booking is for one table.
  - date & time: Stores reservation date and time.
  - guests: Number of guests (1-10), with validation and predefined choices.
  - If a user or table is deleted, related bookings are removed.

---

- Bookings Model
  ![field list](/document/model.booking1.png)

---

- Menu Model
  ![field list](/document/menu.model.png)


## Technologies

    - Python Modules:

      asgiref==3.11.0
      bleach==6.3.0
      certifi==2026.1.4
      charset-normalizer==3.4.4
      cloudinary==1.44.1
      dj-database-url==3.1.0
      Django==6.0.1
      django-allauth==65.14.0
      django-cloudinary-storage==0.3.0
      django-summernote==0.8.20.0
      gunicorn==24.1.1
      idna==3.11
      packaging==26.0
      pillow==12.1.0
      psycopg2-binary==2.9.11
      python-dotenv==1.2.1
      pytz==2025.2
      requests==2.32.5
      six==1.17.0
      sqlparse==0.5.5
      tzdata==2025.3
      urllib3==2.6.3
      webencodings==0.5.1
      whitenoise==6.11.0


- Django:
  - Main Python framework for project development.
  - django-allauth is used for managing user accounts in the booking system.
  - Django's views handle database queries, while the Django Templating Engine renders the data onto the site pages, ensuring a dynamic and responsive user experience.
---
##  Deployment:
-   Deployment paltforms:
  - Heroku: Cloud-based deployment platform.
  - ElephantSQL: Database hosting service.
  - Github: Version control platform.
  ### Running the Project Locally:
    -   To run this project on a local machine, follow these steps.
        1.  Clone the repository from GitHub:
            -   ``git clone https://github.com/Dhiaa-alomari/pizzatasty.git``
        2.  Navigate to the project folder:
            -   ``cd tasty-pizza``
        3.  Install the required dependencies:
            -   ``pip install -r requirements.txt``
        4.  Set up environment variables:
            -   Create a .env file in the root directory and add the required environment variables such as:
            -   ``SECRET_KEY=your_secret_key``
            -   ``DATABASE_URL=your_database_url``
        5.  Run database migrations:
            -   ``python manage.py migrate``
        6.  Start the development server:
            -   ``python manage.py runserver``
        7.  Open the application in your browser:
            -   ``[python manage.py migrate](http://127.0.0.1:8000)``
  ### Push Code from Code Editor(IDE) Locally to Github:
    -   All code from code eidtor program (e.g.: visual studio code) was pushed to Github using the following steps:
        1.  ``git add .``
        2.  ``git commit -m "Commit message``
        3.  ``git push``
  ### Deployment to Heroku
    -   This project is deployed using Heroku.
        1.  Create an account or login to:
            -   [Heroku](https://www.heroku.com/)
        2.  Create a new app:
            -   Click New
            -   Select Create new app
            -   Enter the app name (e.g., tasty-pizza)
            -   Choose Europe region.
        3.  Connect the project to GitHub:
            -   Go to the __Deploy__ tab.
            -   Select GitHub as the deployment method.
            -   Connect your GitHub account.
            -   Search for the repository name and connect it.
        4.  Add environment variables:
            -   Go to the __Settings__ tab.
            -   Click __Reveal Config Vars__.
            -   Add required variables such as:
            -   ``SECRET_KEY``
            -   ``DATABASE_URL``
            -   ``DEBUG``
        5.  Deploy the application:
            -   Go to the __Deploy__ tab.
            -   Select the branch (usually ``main`` or ``master``).
            -   Click __Deploy Branch__.
        6.  Once deployment is complete, click __Open App__ to view the live project.

- [Back To Up](#tasty-pizza)
---
- Packages Used:
  - Development Tools:
    - VSCode: Visual studio code IDE used for coding and file transfer between editor and repository.
    - GitHub: Version control and repository hosting.
    - Balsamiq: Wireframe models for site design.
    - Global css: Styling the text throughout the site.
- Django Documentation:
  - Code Institute: Course help to create the project.
  - Reference for achieving CRUD functionality and associated views.
  - Django-allauth Documentation: Guide for implementing authentication features correctly.


## Manual testing

- Manual test for home page.
  ![manual list](/document/manual.test.first.png)

---

- Manual test for menu page.
  ![manual list](/document/manual.test.menu1.png)

---

- Manual test for login page.
  ![manual list](/document/manual.test.login.png)

---

- Manual test for register page
  ![manual list](/document/manual.test.register.png)

---

- Manual test for booking.

| Test item                           | Test Carried Out                                    | Result                                                 | Pass/Fail |
| ----------------------------------- | --------------------------------------------------- | ------------------------------------------------------ | --------- |
| Select a current or future date     | Choose a valid date                                 | Date is accepted                                       | PASS      |
| Select a past date                  | Choose a date in the past                           | "Date Invalid" notification appears                    | PASS      |
| Select a time within allowed range  | Choose a time between 11:00 AM - 10:00 PM           | Time is accepted                                       | PASS      |
| Select a time outside allowed range | Choose a time before 11:00 AM and 10:00 PM or after | "Time Invalid" notification appears                    | PASS      |
| Select a past time for today        | Choose a past time for the current day              | "Time Invalid" notification appears                    | PASS      |
| Leave date field empty              | Try submitting without selecting a date             | Error message appears                                  | PASS      |
| Leave time field empty              | Try submitting without selecting a time             | Error message appears                                  | PASS      |
| Submit with valid inputs            | Choose a valid date, time, and guest number         | "Booking is successful"message appears                 | PASS      |
| Cancel booking                      | Click on cancel booking                             | "Cancel booking successful"message appears             | PASS      |
| Edit booking                        | Click on the existing booking you wish to edit      | Details for chosen booking appears in the booking page | PASS      |

---

- Automatic Testing
  - Testing Menu app. - Testing is essential to ensure that our application’s features and components work as expected. This suite of tests focuses on verifying the functionality of the Menu model and related views in the application. These tests ensure that: - The data models behave correctly when creating and accessing menu items. - The views render the appropriate templates, load content correctly, and display expected data to users.
    ![auto test](/document/menu.crud.png).

---

- Testing Booking App.
  ![booking app test](/document/booking.crud.png)
  - Test Cases.
    - test_user1_cannot_update_user2_booking.
      - Logs in as User1 and attempts to update User2’s booking.
      - The update should fail, and the booking should remain unchanged.
    - test_user1_cannot_cancel_user2_booking.
      - Logs in as User1 and attempts to cancel User2’s booking.
      - The request should return a 404 error, as User1 has no permission to cancel it.
    - test_user1_cannot_book_for_user2.
      - Logs in as User1 and creates a booking.
      - The booking should be assigned to User1 (not User2), ensuring users can only book for themselves.


## Authentication testing.

- All pages are went through the URI test and passed
  ![html test](/document/html.valid.png)

---

- Css test. All CSS files went through a validater test, result; no error found.
  ![css test](/document/css.valid.png)

---

- Jshint.
- link for js code test: [jshint](https://jshint.com/)
  - Bookings js.
    - Metrics.
    - There are 2 functions in this file.
      Function with the largest signature take 1 arguments, while the median is 1.
    - Largest function has 11 statements in it, while the median is 5.5.
    - The most complex function has a cyclomatic complexity value of 3 while the median is 2.
  - main js.
    - Metrics.
    - There are 3 functions in this file.
    - Function with the largest signature take 1 arguments, while the median is 1.
    - Largest function has 2 statements in it, while the median is 1.
    - The most complex function has a cyclomatic complexity value of 2 while the median is 1.
    ***
  - Pep8
    - Link for: [test python files](https://pep8ci.herokuapp.com/)
    - All Python code has been thoroughly tested, and the results show **no errors were found.**
  - Lighthouse
    - Lighthouse .This test is been done on my laptop.  
      ![light house test](/document/lighthouse-test.png)


## Bugs.

- Duplicate ID Errors:
  - Issue: I received multiple errors for duplicate id attributes in HTML elements (e.g., menu-image, text, title, etc.).
  - Cause: IDs in HTML must be unique within a page. Having duplicate IDs can cause conflicts, especially with JavaScript and styling.
  - Fix: Updated elements to use unique IDs or used class attributes instead of id.
- Image Accessibility Issues:
  - Issue: Some images were missing alt attributes, leading to warnings about accessibility.
  - Fix: Added descriptive alt attributes to all images to ensure better accessibility.
- CSS Validator Errors:
  - Issue: CSS validation produced errors due to incorrect usage of certain properties, like justify-content: baseline.
  - Fix: Updated CSS to use the correct properties (e.g., justify-content: center).
- Test Failures Due to Incorrect String Representation:
  - Issue: One of my tests failed because the ** str** method in my Menu model was returning the wrong string ("Menu object (1)" instead of "Spaghetti").
  - Cause: The ** str** method was incorrectly defined outside the class.
  - Fix: Moved the ** str** method inside the Menu class so it correctly returns the name of the menu item.
- User Could Book a Table in the Past:
  - Issue: Initially, users were able to book tables for times in the past, which was not allowed and created incorrect data in the booking system.
  - Fix: A solution was implemented to prevent users from booking tables in the past by handling timezones and validating booking times:
    - Installed the pytz library for timezone handling.
    - utils.py: Updated to check if the booking time is in the future based on the user's timezone.
    - views.py: Modified to receive the user's timezone from the frontend and validate the booking time.
    - main.js: Added JavaScript to capture the user's timezone.
- Bugs is not fixed:
  - none.


## Credits

- Images for the entire project.
  - <https://www.freepik.com>
  - <https://www.google.se/>

- I used AI tools for supporting(Chatgpt, claudi).

- [Back To Up](#tasty-pizza)
