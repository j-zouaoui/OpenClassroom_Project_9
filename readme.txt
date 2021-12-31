LITReview -web site: 
The LITReview project is a web application. It provides books review and allow connected person to ask for review and share comment about books or publications. It allows user to:

Installation
This web site can be installed and executed from http://localhost:8000/home/ using the following steps
Installation and execution without pipenv (using venv and pip)
1.	Clone this repository using $ git clone clone https://github.com/j-zouaoui/OpenClassroom_Project_9.git (you can also download the code using as a zip file)
2.	Move to the Project_9 root 
3.	Activate the virtual environment with $ env\Scripts\activate on windows or $ source env/bin/activate on macos or linux.
4.	Install project dependencies with $ pip install -r requirements.txt
5.	Run the server with $ python manage.py runserver
When the server is running after step 5 of the procedure, the LITReview web site can be activate using the following URL: http://localhost:8000/home/.
Usage and detailed endpoint documentation
One you have launched the server, and access to the home page through the url: http://localhost:8000/home/ you can sign up as new user and access to the following activities
	consult a feed containing the latest tickets and user comments that it follows, in chronological order, the most recent first.
	create new tickets to request a review on a book / article.
	create reviews in response to tickets.
	create reviews that are not in response to a ticket. As part of a
	one-step process, the user will create a ticket then a comment by
	response to own ticket.
	view, modify and delete your own tickets and comments.
	follow other users by entering their username.
	see who he follows and follow whom he wants.
	stop following a user
