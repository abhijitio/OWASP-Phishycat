# phishycat

<h1> What is OWASP Phishycat ? </h1>

<p> OWASP Phishycat is a Phishing Detection Framework. 

OWASP Phishycat is a phishing detection framework. Idea here is to guess the original domain that attacker is trying to phish. Next, it performs the test by doing real time image comparison and DOM analysis of both web pages (Original domain and phishing domain). </br>
Original domains should be registered in our database before we go for testing. Once it guess the domain name then it compares the real time images of both web pages (phishing site and original website) . Attacker will try to make the web page design look similar to original website as much as possible. If both images are similar to each other, then next step is to compare DOM of both web pages. If it does not match then there is a high chance that it is  a phishing site. Because, we can say two web pages are similar only when every elements of the pages are identical. In this case, we have similar looking two websites but their DOM is different. </br>
Currently, this project also include a Chrome Browser plugin “PhishBlocker” to communicate between browser and back end server. It sends the URL to backend Python Flask server. Server perform the phishing test and respond. User get a javascript alert box with written “Phishing Detected” in the browser. </br>
It can be integrated with any other platform. You just need to send a POST request to running server and receive the response. </br>
This is not a complete project. This is very very basic prototype. It needs continuous improvement</p>
 <p> Please check the Wiki for a brief introduction :- </br>
 <b><a href="https://github.com/abhijitio/phishycat/wiki/About-PhishyCat">Wiki</a></b></p>
 
 <h1> Technology Used :- </h1>
 
 <p>We are using Python Flask as back end server. Which can be accessed here:- localhost:5000 </br>
 Phishblocker, a chromium browser based plugin written in Javascript.</br>
 Testing Platform :- Ubuntu 16.04.2 LTS</p>
 
 
 <h1>How to Use :- </h1>
 
 <p>There are few modules that you need to install. </br>
 We are using virtualenv (It is not necessary. It depends on your choice). To install virtualenv and flask, please follow this <a href="https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world">guide.</a> </br>
 Go to project directory and follow the steps (We have used virtualenv here, you can skip that part if you are not using), </br>
 $cd phishycat </br>
 $. venv/bin/activate </br>
 $pip install pillow </br>
 $deactivate </br>
 $flask/bin/pip install selenium </br>
 $flask/bin/pip install filedepot </br>
 $flask/bin/pip install simhash </br>
 $./run.py</p>
 
 
 <h1>References (Special Credits) :- </h1>
 
 <p> Here are some online resources that helped me. I strongly recommend you to go through them to understand it better. Share with your friends and spread the knowledge</br>
 <a>https://gist.github.com/astanin/626356</a></br>
 <a>http://norvig.com/spell-correct.html</a></br>
 <a>http://leons.im/posts/a-python-implementation-of-simhash-algorithm/</a></p>
 
 
