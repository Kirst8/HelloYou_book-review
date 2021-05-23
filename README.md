# HelloYou_book-review
Code institute Milestone 3

# The book blog 
#### Data centric project / milestone 3 

The purpose of this site is to show the knowlegde of python SQL and MongoDB , and i can Implement this into and idea folling the CRUD process. 
The sites aim is to be user friendly , easy to navigate the user should add update review and delete books from their profile 
Hopefully this can encourge users to read more because after all reading and reading more is a great disipline 
to have.
#Contents
-Introduction

-Demo

-UX

-UXStrategy
  -Scope
  -Structure
  -Skeleton
  -Surface
  -Technologies Used
-Features

-Existing Features

-Features Left to Implement

-Testing

-Deployment

-Credits

-Content

-Media

-Acknowledgments

-UX
-Strategy
-I wanted users of my book review website to be able to view book information and book reviews. I also wanted users to be able to upload their own books if it is not provided already, edit any information they believe to be incorrect and delete any information they have provided! I am also providing book recommendations via the reviews posted in the hope to get users to use my amazon affiliate link, which a link is also provided with every book.

#Scope
##User	
###User Stories
I would like this site to be as versatile as possible so it could reach people who love to or people who only like to read every now and again  . I would like book reviews to be encouraged so that all readers can look view and decide if they would like to purchase the book from the links provided 

###Structure
The Home page will be a full static image and the Navbar will be set throughout pages so users can always be directed back to to pages no matter where they are upon visiting the site.

On the home page there will be a jumbotron card will a sign up form and login button if you have already registered   

The Registerd profile page the users can dashboard to view, edit and delete any posts they have made. They can also upload profile information and a profile photo which will be displayed against any posts they make.

The All Reviews page displays every review on the site, it should have who posted the review by the username, date, book and ratings, the page is purely just to view all the reviews on the site but you can link to a specific books page.

The All books page displays every book on the site with the ability to search the database. all book will be displayed in a Thumbnails and a category sections for more specific views. 

The Add books page is a form that allows a logged in user to add books but you will be asked to add a review as well 

The Review page is a simple form with 2 inputs. The first is the review itself, the second is the star rating. Again only someone logged in can leave a review, but if a user has already left a review then they are redirected towards there account where they can edit the original post. The Edit Review page is virtually a duplicate of the Add review page but the user can update the original post.

The delete page is the same if you are deleting your account, If you like to delete a revieww you only delete your review but if you delete a book, all reviews with the book will be deleted as well and the book will not appear on the database no longer

Skeleton
Homepage / Landing Page

All Reviews

Recommendations

All Books

Book Details

Add Book

Add Review

Account / User Page

Surface
The site has a full page background throughout but on everypage except the homepage it is displayed behind a container with a white background this gives it a clean and simple design, it also avoids any issues with contrast between background and fonts, it also makes it look alot cleaner on smaller devices as full page backgrounds do not display correct on iOS devices. The font throughout is roboto as this is very clean and readable. The Navbar and Footer are both the same shade of grey and have the same colour font. All book Thumbnails are displayed the same on everypage to bring a uniformity to my website. All the Pages follow a similar layout also keeping my application looking clean and simple.

Back to Top ⤴️

Technologies Used
Here is a list of all the technologies used throughout the project!

Balsamiq Mockups 3
I have used Balsamiq to create my wireframes.
[wireframes.pdf](https://github.com/Kirst8/HelloYou_book-review/files/6527605/wireframes.pdf)

Python3
I have used Python3 to create my server-side application.

HTML5
I use HTML to create the basic structure of my book review website.

CSS3
CSS gives my site its look and style.

JQuery
JQuery is used to initialize a few components and generally improve user experience.

Flask
I have utilised the flask micro-framework to speed up the overall process. I have also used multiple modules such as flask-pymongo, flask-paginate, session and many more.

MongoDB
I have chosen to use MongoDB as my database as this is what I feel most comfortable using.

Font Awesome
Font Awesome was used for all of my icons.
 ⤴️

Features
The main features of my site are the ability to view a vast array of books and post reviews on each of these books, Post more books, link to buy books, edit reviews and also see the recommendations.

Existing Features
 Users can sign up via the homepage signup form. Once signed in they will be able to leave reviews, view their profile, edit their profile and post more books.
 If a user already has an account they are able to login via the login modal which is available through the Call to Action on the Navbar and the sign up form.
 A user can only leave one review per book, if they try to add another a toastr notifcation will let the user know they will have to edit the original review.
 A user can post a book via the Add book page, this will add the book to the database and send the user to the page that has just been created, here they can add a review or edit if they have made an error.
 A search bar is available so users can search for a book instead of crawling through hundreds of pages.
Features Left To Implement
 Due to using an existing dataset I was limited to the data I had been provided as such I have not got information such as genre or category. In the future I plan to use my own data which does provide all the information I want.
 In the Future I plan to have Friends / Followers where you are able to view other users profiles, books people are reviewing and what they like. Also providing a means to message or comment on each others pages.
 At the moment the Add book form is unmoderated so if a user uploads incorrect data, rude data etc then it will just be uploaded. In the future I plan to moderate all posts so I can keep my database clean.
 The search bar needs to be more exact as at the moment it works but it doesnt always give you what you expect.
 A Contact page is missing incase any users feel the need to get in touch or have any suggestions etc. This will need to be implement and will not be an issue but is not essential at this time.
Back to Top ⤴️

Testing
I have done all my testing manually and throughout production of my website. Whenever I have made a change to something I have tested any possible ways in which it could fail such as when I created my all reviews page and I was testing by adding reviews from different users I found a user without a profile image would break the page as it could not display the profile image for that user.

All the python code is linted and debugged by gitpod so I have not had to worry about syntax or format as this has let me know throughout when I have not been using the correct syntax or I have input my code incorrectly. I have also been using Flask which uses Jinja2 as its template engine which lets me know of any bugs within my code also giving me a pointer to which part of my code is failing. All the HTML and CSS pass validation with W3 Validators but HTML does throw up errors due to the fact I am using jinja2 templating and it does not recognise this but other than the expected errors everything else passes.

My site is responsive on multiple media devices and viewports. I used googles DevTools to test all the different viewport resolutions, I also did this on Opera and firefox. I generally had no issues with this as I mainly used MDBootstraps preset classes to help create a flexbox layout keeping everything nice and centered, in a clear order and very responsive. I was able to keep my custom CSS to a minimum due to the way in which I used the framework I was able to keep my code nice and clean. All the pages respond correctly and every link acts in the expected way. I've had no console errors within my code and again act as expected.

During development I noticed that when a user without a profile photo posts a review they review actually breaks a few pages such as all reviews and the specific book page. The pages are looking for a profile photo to display for these reviews but cannot find one and throws an error. To fix this I decided to force users to upload a photo, I plan to automatically have a placeholder image uploaded to the database when a user creates an account but this was a quick and easy fix for now.

Another bug is with the top ratings sortation, My database already has average ratings and my users input there own ratings which calculates a user average ratings whcih is where the issue occcurs. When a user selects top ratings they are given the collection of books in order of top rating first but because I have two ratings fields to sort through it places all the user ratings first from 5 down to 1 and then the average rating from 5 - 1. I am not sure how to fix this right now and it doesnt cause too much of an issue at this time so I have chosen to leave for the time being and when I can think of a solution I will implement.

Here are a few of the manual processes i've done to test my code:

NavBar:

Throughout development I checked all links would respond correctly. By clicking links I was able to confirm this.
Next I went into chrome devtools and turned on mobile response to confirm the Toggler button appears, I would click to confirm the button worked correctly.
Once the links were displayed I clicked each to confirm the navbar opened the page and closed the navbar as intended.
I also checked all available viewports within devtools to makes sure it displayed correctly.
Social links were also checked to makes sure they opened a new tab and of course the correct page.
All tests came were a success and I cannot recall any issues throughout development.
Footer:

My footers navigation works as intended when clicked.
Once the Quick Links had been selected I tested to see if they opened the correct pages in new tabs.
I tested each viewport size to see if it resonsed as expected.
All tests were successful and no errors except with styling occured.
Responsivness:

I went to inspect on chrome and chose various viewports, checked to see any display issues.
If issues were discovered I would use Unicorn Revealer to see any hard to find padding / margin issues.
If data did not display properly I added relevant media queries or edited javascript or content until it was correct.
I then chose the responsive option on the viewports and checked as many resolutions as possible.
I repeated the processes for any errors in what was displayed.
I also checked the responsiveness on my personal iPhone and work Android as Devtools I find is not always 100% correct.
If any errors did occur I corrected them accordingly.

I slected each page to make sure each button was responsive
add review books login and logout functions worked correctly
then I wanted to make sure that all cards were responsive and no overall
Login modal

Once logged in I navigate profile button.
The I would add a review to make sure that each form input was was validation
The submit button worked correctly , Submit button however was not return to profile page



I first select a book I want to add a review for and press the add review button.
I fill out the form and all the fields are required and all the fill out this field error appears if a field has been forgotten.
Once submitted I am redirected to the books page with my new review at the top as expected.
I then check the all reviews page to see if my review has been added in which it has.
I also check my account page which also shows the newly added review.
To check to see if I can still add more reviews to the same book I click the edit button again on the book and im given an error that I have already reviewed this book as i expected.
Edit Review Form.

To test the edit review form I first go to the account page and select the edit button for the review I want to change.
I am given virtually the same form as the Add review page and I fill it out again.
Once submitted I am redirected back to my account where I can see the updated review.
I then check then all reviews page and can see it has updated.
The books page has also updated so everything works as expected.
A few times during development I would find that one of the reviews would not update this was for various reasons but was fixed by how the page form updates the databases.
Delete Buttons.

For the delete buttons I firstly log in and navigate to my account.
Next I select the delete button on one of the reviews, this brings me to a delete page asking if i really want to delete the review.
Once confirmed the review is deleted from the account page, all reviews and the book page as expected.
Next I checked the delete book button by first adding a fake book entry and adding a couple reviews.
I then select the delete button and am taken to the delete confirmation page which I confirm and am brought back to the all books page.
I check the all reviews page to check to see if all the reviews have deleted which they have.
Finally the delete user button, I created a fake account and then pressed the delete account button.
The same Confirmation page is displayed and I confirm my delete.
This brings me back to the homescreen with a warnng to let the user know their account is deleted.
Back to Top ⤴️

Deployment
I am currently deploying my website on Heroku deploying from the master branch. My Github Repository and Heroku are linked and are currently set to automatic deploys as I was having issues using multiple machines when I was using Heroku Git originally. Due to this all commits will deploy from the master branch automatically. The site can be viewed at https://github.com/Kirst8/HelloYou_book-review. For my site to run in Heroku I have had to supply a requirements.txt file to let Heroku and any other developers know what dependencies are needed for my site. I have also supplied a Procfile which lets heroku know the process type of my application.

Commiting to Github
Using my terminal window I firstly use git pull https://github.com/Kirst8/HelloYou_book-review to pull the most upto date version of my repository.

Once upto date I edit everything I need to and use git add . to stage all the edited files for commiting.

Using git status I usually view to see I have staged all the files I want to and I have no unwanted files being commited.

Next using git commit I commit to the local Repository and then git push to finally push the changes to the master branch.

Deploying to Heroku
Firstly I needed to go to my Account dashboard, here I can select New and Create New App.

I chose a unique app name, the region of Europe and then pressed create app.

Once Created I was brought to the deploy section of my app, here I decided to chose to deploy with Github.

Heroku then asked for the repo name of my app I wished to deploy.

I selected connect once my repo was found and I was then able to commit to the master branch on Github. It will then Deploy Automatically as I have automatic deploys turned on.

The site is almost deployed but I then needed to go to the settings section and let Heroku know of any enviroment variables such as the ip, Port, Secret key and database URI.
Cloning the repository
To run this repository locally:

Click "Code" at the top of this repository.
Select Download Zip or Copy the URL to your clipboard.

Open up Terminal and select the location in which you wish to clone this directory.
Then type git clone and copy https://github.com/Kirst8/HelloYou_book-review
Press enter and you will have succesfully cloned this Repository.

Installing dependencies
Installing Dependencies is very simple and I have supplied a requirements.txt to help with this process. Once the repository has been cloned before it can be ran the user will need to open the terminal on their IDE and type pip3 install -r requirements.txt. All the dependencies should now download and you are ready to go.

Back to Top ⤴️

Credits

Content

Book Database To fill my website with Books I found a Dataset online and uploaded this into MongoDB.
Media
Book Background This is the picture used throughout the site as the background.

Favicon I have used this Icon as the Favicon.

Acknowledgments

Flask Documentation Helped me with the syntax and any queries I had with the flask Framework

I used SlackCI and thats where I did reslove most of my issues when they came Like my heroku deployment and why database with not connceting and it was simple things like mispelling of database name and not undating my requirements txt file  

Materialize for project layoy and various form inputs and validation and colour palates
w3 Schools w3 Schools was used for when I needed a little help my modal forms 
