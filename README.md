# AI-miss-u
By Estelle Ocran and Junior Garcia

A digital representation of your loved ones. 

## Description

The advent of machine learning and artificial intelligence has revolutionized our use of and interaction with technology. From recommender systems to self-driving cars, AI has permeated almost every aspect of our daily lives to the point where we are not even cognizant of its presence. One aspect we were interested in exploring is the effect AI has, and will continue to have, in rekindling human relationships. Although it feasible to envision a future where AI and technology acts as deterrent to human relationships due to the lack of interpersonal interactions that exists between humans, we envisioned a hopeful future where AI helps humans get closer together. The aforementioned aspiration resulted in **AI-miss-u**, a AR/VR digital representation of your loved ones. 

Using state-of-the-art AI algorithms, AI-miss-u takes in any of the following inputs from someone's loved one: text data, video data, or image data, to create an AR/VR digital representation that acts and talks exactly like your loved one. The more data you feed in, the more the digital representation will resemble your loved one. This digital representation can be accessed through any piece of technology with access to the Internet. To make the experience more immersive, users can customize  AI-miss-u so that they can access their loved one through their browser using Virtual Reality, thier phone using Augmented Reality, through sms/messenger/whatshapp via the chatbot component, or all of the aforementioned. The idea is to give users the ability to customize their AI-miss-u experience to fit the communication method that best fits the type of relationship they have with their loved one. Using this product, users can bring back to life loved ones that have passed away, friends that are too far away, or even recreating digital representations of famous individuals.

## Process and Implementation


AI-miss-u 

For our speculative design project, we wanted to make a prototype of the output AI-miss-u produces after being trained. As such, we use <a href="https://aframe.io/">A-Frame</a> to create a VR experience in the browser and <a href="https://chatterbot.readthedocs.io/en/stable/tutorial.html">Chatterbot</a>, a python library to create chatbots. As such, we used general html,css,javascript for our frontend and <a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a>, a Python web franework, for our backend. 

In terms of the front end implementation, we leveraged Aframe and free 3D models on the internet to create the VR experience. We depended heavily on stackoverflow and the A-frame docs in order to code the Virtual Reality aspect of the project. As we both were new using this framework, we founded quite difficult to work around it. However, given its simplicity and minimalistic approach, we were still able to produce something tangible despite our hurdles.

For the backend, we based our code heavily on this <a href="https://github.com/chamkank/flask-chatterbot">repo </a>, which provides a very minimum implementation of the chatbot in Flask. We had some issues installing the chatbot library in our computers, but other than that, the backend ran smoothly.

## Reflection and Evaluation

All in all, we are happy we came up with a very minimal implementaton of AI-miss-u. Since we were both using technologies we were new with, it probably would have been nice to have more than one week in order to make prototype that is closer to what we envisioned the final product will look like. 
