# portfolio_and_blog

## Presentation :
It's just a portfolio to speak about me, show my realization and a blog to share my oppinions, progressions and difficulties about code, project management, and freelancing.

## 1/ Learn more about the developper and this realizations (portfolio)
__As a__ visitor \
__I want__ to go on the portfolio website \
__In order__ to see all the realizations \
__And__ see the detail of a project \
__And__ learn more about the developer \
__And__ find your social networks (github, linkedin)

## look_details_project :
__Given__ a visitor want to consult the details to a realization \
__When__ he clik on a card realization \
__Then__ a modal show him the synopsys of the project with the technologies
__And__ he can clik on the button __Go__ to go on the real project

## about_me :
__Given__ a visitor want consult the "about me" section \
__When__ he click on the "about me" link in the navbar \
__Then__ he is redirected on the good section in the onepage portfolio

## all_my_project :
__Given__ a visitor want to consult the realization section \
__When__ he click on the realization link in the navbar \
__Then__ he is redirected on the good section in the onepage portfolio

## go_on_my_project :
__Given__ a visitor want to see a real project \
__When__  he click on the button __Go__ in the modal of the realization details \
__Then__ he is redirected outside of the portfolio on the project

## User stories bonus :
__As a__ visitor \
__I want__ to go to a specific realization \
__In order__ to see the detail of realization (technologies, design, project management, skills) 

__As a__ visitor \
__I want__ to go to the "about me" section \
__In order__ to learn more about soft skills developper

__As a__ visitor \
__I want__ to contact the developper \
__In order__ to ask something

## 2/ Contact him (portfolio)
__As a__ visitor \
__I want__ to go on the contact page \
__In order__ to send a message to the developper

## go_to_contact_form :
__Given__ a visitor want to contact the developper \
__When__ he click on the contact link in the navbar \
__Then__ he is redirect to the form page

## send_a_message :
### (success)
__Given__ a visitor want to send a message to the developper \
__When__ he fills out the form \
__And__ clicks send \
__Then__ the system check that the forms is ok \
__And__ send the email to developer \
__And__ redirect the visitor to the homepage \
__And__ display a message "your message was sent correctly"

### (fail)
__Given__ a visitor want to send a message to the developper \
__When__ he is filling out the form incorrectly \
__Then__ the system don't redirect him
__And__ display the errors in the form

## 3/ Consult article (blog):
__As a__ visitor \
__I want__ to go on the developper blog \
__In order__ to consult article
__And__ leave a comment

## go_to_my_blog :
__Given__ a visitor want to go on my blog \
__When__ he click on the blog link in the navbar \
__Then__ he is redirected on the main blog page \

## consult_an_article :
__Given__ a visitor want to read an article \
__When__ he click on the resum card article in the main page \
__Then__ he is redirected to the selected article

## leave_a_comment :
__Given__ a visitor want to leave a comment about an article \
__When__ he write the comment at the bottom of the article and send it \
__Then__ the system record the comment in the db
__And__ reload the page to display him

## edit_a_comment :
__Given__ a visitor wants to modify his comment \
__When__ he click on the pencil icon \
__And__ rewrite the comment
__And__ validate 
__Then__ the system update the db
__And__ reload the page to show the edit message

## delete_comment :
__Given__ a visitor wants to delete his comment \
__When__ he click on the bean \
__Then__ the system delete the comment to the db \
__And__ reload the page to show that it is deleted

__Given__ the admin want to delete a comment \
__When__ he click on the bean \
__Then__ the system delete the comment to the db \
...

## 4/ Create article (blog) :
__As a__ bloger \
__I want__ to create an article or a series of articles
__In order__ share my experiences and assimilate him

__Given__ the blogger want to go on the back-office
__When__ he go on the admin page
__Then__ the system ask him to be connected

__Given__ the blogger want to be connected to the admin
__When__ he give username and password
__Then__ the system redirect him to the django admin page

__Given__ the connected bloger to the django admin want to create an article \
__When__ he write the article and send it now \
__Then__ the system record it in the db
__And__ display it in the blog

__Given__ the connected bloger to the django admin want to create a category
__when__ he creates the category
__Then__ it is record in db 
__And__ display to the blog page

__Given__ the blogger want to programize the send of an article
__When__ he creates the article and choice a date of publication
__Then__ the system send the article to the blog when the date is comming

## User stories bonus (blog) : 

__As a__ visitor \
__I want__ to consult an article \
__In order__ to read it

__As a__ visitor \
__I want__ to see all the categories \
__In order__ to consult only the article that interest me

__As a__ visitor \
__I want__ to leave a comment \
__In order__ to share my oppinion about the article

__As a__ bloger \
__I want__ to write an article \
__In order__ to share my experience

__As a__ bloger \
__I want__ to create series of article \
__In order__ to deal with a larger subject

__As a__ bloger \
__I want__ to programize a publication of article \
__In order__ to write my subjects in advance 
