# inhaler-count-predictor
A web application for people with breathing problems to find the number of times they need to use the inhaler per day based on the atmospheric temperature, air density and the age of that person as these were the factors influencing the usage of inhaler.

The web app was developed using HTML, CSS and Flask framework.  We used Machine Learning to make the prediction model to predict the count of the usage of inhaler.  The Machine Learning model used here is <b>Decision Tree</b>.

<center><img src='https://storage.googleapis.com/devfolio/hackathons/d80d930e94ea4331820c993b019fb0fa/projects/0cec5bb5a01942f78093d2dd66930a51/picgi8ine5qs.png' alt='Web Application'></center>
<hr/>
<center><img src='https://storage.googleapis.com/devfolio/hackathons/d80d930e94ea4331820c993b019fb0fa/projects/0cec5bb5a01942f78093d2dd66930a51/picgec5388e4.png' alt='Web Application'></center>
<hr/>
<center><img src='https://storage.googleapis.com/devfolio/hackathons/d80d930e94ea4331820c993b019fb0fa/projects/0cec5bb5a01942f78093d2dd66930a51/picoge78cn0a.png' alt='Web Application'></center>
<hr/>

we made the machine learning model and trained it with the dataset and saved the trained model in a .pkl file <b>Model.pkl</b>.  On Predictor.py, the trained model i.e. Model.pkl will be loaded and be used for prediction.

We used Flask framework to get the input provided by the user in a webpage and feed it to the ML model and display the prediction result back in the webpage.  

The final result will be displayed as : <b>You will take x to y times the Inhaler</b> in the webpage.

The next stage of this project would be making it as an IOT application where, the application will automatically find the atmospheric temperature and air density and there is no need for the user to enter these as inputs. 
