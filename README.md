# Milestone Project 3

This README should be considered alongside the PDF file Milestone_3_wireframes which illustrates some of the developments detailed in this document. This PDF file is available in the root directory of this project [here](/Milestone_3_wireframes.pdf).

## Project introduction
This project is designed to function as a Wikipedia-style website but specifically targeted towards people with an interest in Irish history. Posts will be approved by an admin (with functionality to allow for a specific admin profile to be developed at a later date) while anyone can write a post and send it for approval. As there are currently no restrictions on who can approve posts, this entire loop (public post submission, review of said post, posting of this post on the landing page) is available in its entirety to a user currently visiting the site. The website is responsive to different size devices, and was designed with a deliberately simple style to reflect the content (see section on “UX”)

### User Stories
There are several types of users who would be potential customers of the website.

1. An individual interested in reading biographies of major Irish historical figures at home on their computer
2. Individuals interested in browsing biographies of major Irish historical figures at home or while travelling on their mobile phones
3. Someone who is an expert on Irish history or particular Irish historical figures who wishes to share their knowledge in a public forum
4. An admin who wants to help maintain high standards for the articles submitted by approving or rejecting the posts submitted by those in category 3. 

These user needs were met by:

- Allowing for a clear, minimalist design, with the biographical/dictionary articles placed front and centre.
- Having the titles of the biographies collapsed by default, allowing users to scan them and then expand out the article they are most interested in. 
- Having a website that allowed full navigation regardless of where the user was on the site (and by designing the site to only have three pages, with the primary content delivered immediately on the launch page).
- Experts in Irish history (or indeed anyone who wishes to post) are provided with a dedicated page for inputting a post for approval by the administrative staff (at this point anyone can use this functionality – user profiles are a future feature of this project). 
- Admins have a dedicated page for approving posts, which presents potential posts in a simple style (similar to how they are presented on the main page). This page allows for admins not only to approve or reject posts, but also edit them to correct small errors (should the project get launched on a broader scale a dedicated administrator’s code would be created to ensure no meaningful changes were made without the poster’s permission).
- Having a collapsible UI. Given the deliberately pared back nature of the project, the degree to which the material presented changes at different viewpoints is relatively subtle. 

There are also certain benefits to developing this website for the developer:

1. Demonstrating the developer’s flask skills
2. Demonstrating the developer’s ability to design clear, functional websites with little superfluous material (no/limited scope creep)
3. Demonstrating the developer’s usefulness in the field of Modern Irish history which, while obviously well-populated by academic experts, has a considerable deficit of well-produced online content. 

## UX
From an early stage I decided to keep the app to a single page to start. As it was primarily a biography site, emphasising key figures in Irish history with collapsible headings to save space, I did not see the need to introduce distinct categories or several pages for different types of information. As the scope of the website expanded, I could consider adding multiple different pages, potentially:

- People
- Events
- Locations

With more that could be potentially added. These categories could be applied to the post when reviewed by the administrator, or could be suggested from a list by the poster in the first place. This type of website would of course require multiple pages and some sort of sorting/search functionality. For now, the website will function as a simple crowd-sourced biography website, with posts having to be approved before they are published to the main page (albeit through a non-login protected page).

Early drafts of the website considered using images for each post (see [wireframe document](/Milestone_3_wireframes.pdf) ), but this was left out of the final project in favour of simple icons indicating the biographical nature of each post. If the project is to be expanded in the future, different icons could be used to represent different categories of entries. Images were avoided given the user-provided nature of the content – having previously worked in exhibition design, I know that obtaining copyright permission for images can be a long and difficult process, and this applies especially to images which you do not personally know the source of. Allowing users to upload their own photographs for posts would place an inordinate burden on the administrators to verify their copyright and requiring the administrators to provide images for each post would also be very time consuming. Text on the other hand can be readily checked for plagiarism using a range of online platforms (Turnitin for example). 

In terms of UX and appearance, Materialize was used for the appearance of the website. I mainly did this to experiment with a new set of pre-built CSS. As can be seen in the static/style.css directory, significant custom CSS was introduced to fix/amend certain aspects of the Materialize framework (most of which is explained in the comments in that file). I wanted to go for a minimalist appearance, with the biographical articles occupying front and centre of the project. 

The colour scheme changed over the course of the project (see [wireframes](/Milestone_3_wireframes.pdf) ). Originally a more attention grabbing purple and orange theme was chosen, but this in hindsight seemed too garish given the more reserved nature of the material being displayed. Instead, a more muted green theme was chosen to emphasise both the serious nature of the content and the national focus of the biographies. Button highlights were modified for certain button prompts, but this was done subtly to fit in with the broader theme (see the shade contrast when the button to submit a biography is hovered over for example). The colourscheme was chosen and developed with the assistance of the web app [coolors](www.coolors.co).

The font chosen was “Sen”, taken from Google Fonts, with San Serif as a backup incase there was any issue loading this external font. This font was chosen for its business-like but also clean and relatively stylish appearance. To me the font seemed somewhat reminiscent of that for the London Underground (while obviously literally and legally distinct), an implication which I believe only reinforces the historical associations of the website. 

## Features

### Existing Features

1. Approval of posts

One basic feature that I wanted from the start was for all user-made posts to have a default Boolean value of ‘approved’ which would be ‘false’. Admins would then be able to change that value to True using some variety of interface on the website itself (thereby approving the post). I would then write some python script to iterate over both the admin and the user posts, and only upload those which had the ‘approved’ value set to ‘True’. This feature provide difficult to implement – see the “testing” section for further detail. 

2. 'CRUD' functionality

The website clearly demonstrates all aspects of the CRUD requirements of the module:
- Posts are created by clicking on the 'Write a biography' link at the top right of the page.
- Pages are read out to the launch page (as long as they have been approved).
- Posts can be deleted either from the launch page or in the 'Approve posts' section.
- Posts can be both edited and updated with the value of 'approved: "true"'.









### Features left to implement

Early ideas for the project centred around an Irish-history centred Wikipedia style website, but one where all entries were approved/checked by myself as an expert on the topic. Any user could create a post for the website, but every post on creation would be given a Boolean attribute “approved” which would be default set to “False”. These posts would be run over by an if/else loop in Python which would check the Boolean value of “approved”, and if it was “False” the post would not be published. The purpose of this would be to make sure that no posts were published before I had read them and manually changed the “approved” value to “True”. 

In order to make sure that no posts are left without being read for long periods of time, I will set up an alert in which I will automatically be sent an email whenever a post is made for the website. This will prevent any posts slipping past my notice. 

Ultimately, the project ended up being simpler than that detailed above. I spent a long time trying to figure out both the email notification system and the implementation of login authentication, installing Flask-Mail and Flask-Login into the project and developing other parts of my database to house users, but ultimately decided that both were beyond the scope of the project as defined by the Code Institute. These features would be essential for the project to be feasible as a fully deployed project, but my familiarity with Flask-Login and Flask-Mail would have to be developed significantly (even after many hours working with it, I still could not get this functionality present in the project and decided to focus my effort on meeting the criteria for the milestone project).

In a longer-term perspective for the project, it is apparent that the Update and Delete functionality could be open for misuse, as users could delete and amend each other’s posts if these options were publicly available. As mentioned, incorporating user-profiles (with myself as the administrator) would solve this problem in the longer term. 










### Testing

## Settling on a development environment

Due to the continued transfers from different workspaces by the Code Institute, I decided to try and do all my coding on my local machine, using a virtual environment set up in Python. This proved to be very challenging, with many teething problems coming up as I tried to do something that was not covered by the Code Institute course. I believe this will prove useful for my future professional development as a software developer, but it also proved time consuming and frequently frustrating. In particular, it required developing my understanding of how databases like MongoDB Atlas communicate with servers, how ports work, and how environmental variables work outside of the closely controlled environment of Cloud9 (which by this point had already been shut down). 

I made quite a bit of progress setting up the various connections on my local server, but encountered significant difficulties getting MongoDB Atlas to communicate with my local server through python, so eventually moved to GitPod, mainly for the higher level of support through Slack for that IDE. From there I started plugging in the various platforms I needed to get up and running, but faced significant obstacles trying to set up environmental variables to store sensitive user information (mainly my own MongoDB login details). Eventually, after incorrectly creating them in the ‘workspace’ directory, with tutor support I set up my env.py file in the main directory ‘third_milestone_project’, placed it in a .gitignore file, and managed to connect this to my central python app, testing its functionality with a “hello world” style test message. From this point onwards the connections with Heroku and MongoDB Atlas had been made, and now I could focus on the actual coding/design of the project.

## Creating the approval functionality

The most significant testing challenge came in developing the approval functionality for admins to allow posts created by users to be released to the launching page. 

Creating the python script to iterate over whether posts had the attribute “true” proved straightforward, and I correctly drafted it on only my second attempt. As can be seen in the file 'posts.html', a basic jinja script allows a python 'if' loop to run which checks whether the attribute 'approved' is equal to the Boolean 'true'. If it is, it gets published on the launch page. I proved this by inserting a test 'false' entry into my database which did not print when I ran the page again.

Figuring out how to give a collection the default key:value pair proved very challenging, but ultimately the solution ended up being very simple. At the start I did not know how to set a default value in Atlas MongoDB. I thought there were potentially two ways of doing this. 

With that in mind, I went looking for solutions that either:
    a) triggered a certain package of script when the submit button on the form was pressed (this is what I essentially did to fix my approval page)
    b) meant that whenever the new entry was created in the database, Atlas automatically gave it the key value pair of ‘approved: false’ (much like it already did by giving each entry an automatic ID number). 

I eventually realised that it was not actually necessary to have a default value of approved:false which I would change to approved:true - I could simply have the form submit without the value of 'approved' at all, which would result in the entry being excluded by the if loop regardless.

This left the problem of updating each entry to input the key value pair of 'approved:true' for every entry I deemed appropriate. I had discovered that if the 'approved:true' value was put at the end of the document (as opposed to immediately after the ID), the if loop did not register it for publication. This problem baffled me, and I had to then research how to resolve this situation. For while it might be possible for me to log into AtlasDB and manually insert a value of 'approved: true' after the ID on AtlasDB's GUI, this was not exactly an elegant solution. I did realise, however, that any update where I added a new key-value pair of 'approved:true' to the end of my document would not then be read. I had to figure out not just how to insert the key-value pair of 'approved:true' using flask, but also to specify where in the document (immediately after _id) this pair was inserted.

Eventually, i settled on a workaround (seen in approveposts.html) where essentially the entire form was resubmitted but simply hidden from the user, with the "approved: 'true'" value simply being the first value submitted to the database. 

** note ** I realised towards the end of the project, when putting together the approval page (the last page of the project) that assigning a Boolean to a key:value pair in MongoDB using Flask required some parsing which did not seem necessary - the value could be set as a string with a similar result for my current purposes. 

## Testing the user stories

1.

2.

3.

4.


## Deployment


























## Bibliography/influences:

The most obvious influence for much of the code in this project was the Mini Project in Data Centric Development. Many of the central loops were heavily influenced by that project, although the approval process was developed by myself. 
Miguel Grinberg's Flask tutorials were very useful for understanding fully the functionality of what I was doing (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
Traversy media have some useful videos on a variety of topics - the videos on MongoDB on YouTube proved useful for double-explaining some key concepts (https://www.youtube.com/watch?v=-56x56UppqQ)
The two example articles had their text taken from Wikipedia. 
