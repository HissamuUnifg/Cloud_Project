# Cloud_Project
This is a simple project for educational purposes. The main objective is to serve as an example project that the students can use to practice basic deployment's activities.

# Instalation
The installation process is quite simple and direct. 

Assuming you are using an Ubuntu distro, you just have assure you have python3 installed e clone de repository in a folfer of your preference.

After cloned, navigate to the project directory and use apt to instal pip: 
> sudo apt install pip
 
You then, may start a virtual env using venv (using a virtual environment is optional but recommended).

> cd your_project_path
> python -m venv venv
> source venv/bin/activate
 
After that, you just have to install the dependencies listed in the requirements.txt file
> pip install -r requirements.txt
 
Now you can go take a cup of coffe while all deps and modules are installed...
Now, you should be able to run the app, justa typing

> flask run
 
Expected output in your terminal: 

* Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Don't forget to follow the advice to change to a production WSGI when using in production.

 
