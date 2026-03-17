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