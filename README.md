# easyfinance
Creating a three page financial calculator that is built into a docker container and operated through a cloud service provider.
For the calculators I made one that can calculate monthly loan payments, one that can calculate investment growth over time, and one
that calculate retirement savings. I did this with a clean and responsive deisng with dark UI gradient and it is fully containerized and
cloud hosted.

# Frontend
For the Frontend I used HTML, bootstrap.

# Backend
For the backend I used python and flask

# Styling
For styling I used the googlge fonts Bebad Neue + Sora and also used a custom css file which had a dark theme with blue accents.
I was apart of the polling team app and the style I used was based on what we did for that project since I liked it.

# Containerization
For containerization I used docker.

# Cloud Deployment
I used google cloud run via docker plus artifact regisrty for my cloud deployment.
link to website: https://easyfinance-app-880122042222.us-west1.run.app/

# How to run Locally
follow these steps in your terminal to run it locally  
git clone https://github.com/Ctreziok/easyfinance.git  
cd easyfinance  
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
python main.py  
