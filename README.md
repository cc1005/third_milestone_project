First Draft of Readme

Early ideas for the project centred around an Irish-history centred Wikipedia style website, but one where all entries were approved/checked by myself as an expert on the topic. Any user could create a post for the website, but every post on creation would be given a Boolean attribute “approved” which would be default set to “False”. These posts would be run over by an if/else loop in Python which would check the Boolean value of “approved”, and if it was “False” the post would not be published. The purpose of this would be to make sure that no posts were published before I had read them and manually changed the “approved” value to “True”. 
In order to make sure that no posts are left without being read for long periods of time, I will set up an alert in which I will automatically be sent an email whenever a post is made for the website. This will prevent any posts slipping past my notice. 
Is there functionality have my Python script create a new page and plug it in every time a new post gets approved? This might be fairly complex.

Planning and development

Due to the continued transfers from different workspaces by the Code Institute, I decided to try and do all my coding on my local machine, using a virtual environment set up in Python. This proved to be very challenging, with many teething problems coming up as I tried to do something that was not covered by the Code Institute course. I believe this will prove useful for my future professional development as a software developer, but it also proved time consuming and frequently frustrating. In particular, it required developing my understanding of how databases like MongoDB Atlas communicate with servers, how ports work, and how environmental variables work outside of the closely controlled environment of Cloud9 (which by this point had already been shut down). 
I made quite a bit of progress setting up the various connections on my local server, but encountered significant difficulties getting MongoDB Atlas to communicate with my local server through python, so eventually moved to GitPod, mainly for the higher level of support through Slack for that IDE. From there I started plugging in the various platforms I needed to get up and running, but faced significant obstacles trying to set up environmental variables to store sensitive user information (mainly my own MongoDB login details). Eventually, after incorrectly creating them in the ‘workspace’ directory, with tutor support I set up my env.py file in the main directory ‘third_milestone_project’, placed it in a .gitignore file, and managed to connect this to my central python app, testing its functionality with a “hello world” style test message. From this point onwards the connections with Heroku and MongoDB Atlas had been made (albeit over a long and fairly arduous period), and now I could focus on the actual coding/design of the project.

Design

From an early stage I decided to keep the app to a single page to start. As it was primarily a biography site, emphasising key figures in Irish history with collapsible headings to save space, I did not see the need to introduce distinct categories or several pages for different types of information. As the scope of the website expanded, I could consider adding multiple different pages, potentially:
	People
	Events
	Locations
With more that could be potentially added. These categories could be applied to the post when reviewed by the administrator, or could be suggested from a list by the poster in the first place. 

Functionality

One basic feature that I wanted from the start was for all user-made posts to have a default Boolean value of ‘approved’ which would be ‘false’. I would then have to manually change that value to True. I would then write some python script to iterate over both the admin and the user posts, and only upload those which had the ‘approved’ value set to ‘True’.
Happily, creating the python script to iterate over this proved straightforward, and I surprised myself by correctly drafting it on only my second attempt. As can be seen in the file 'posts.html', a basic jinja script allows a python 'if' loop to run which checks whether the attribute 'approved' is equal to the Boolean 'true'. If it is, it gets printed. I proved this by inserting a test 'false' entry into my database which did not print when I ran the page again.
This proved somewhat of a challenge. At the start I did not know how to set a default value in Atlas MongoDB. I thought there were potentially two ways of doing this. One was having a hidden option on the form page itself which was already filled in with ‘False’ and would be submitted with the rest of the form, but this seemed like a cheat workaround instead of actually developing this functionality in the back end (if it would have worked at all).

With that in mind, I went looking for solutions that either:
    a) triggered a certain package of script when the submit button on the form was pressed
    b) meant that whenever the new entry was created in the database, Atlas automatically gave it the key value pair of ‘approved: false’ (much like it already did by giving each entry an automatic ID number). 

CRUD functionality

In the case of websites with user-created content, it is a challenge to incorporate the Update and Delete functionality of CRUD as it could be open for misuse, as users could delete and amend each other’s posts if these options were publicly available. 
One solution (if I was at a more advanced stage in my course) would be to create user profiles who have certain permissions to do these two functions (making them admins for the site). I would initially be the only individual with these powers, which could be extended to other users as the project grew and appropriate candidates were found.
At the mid-point of this project, this concept was considered too complex to incorporate into the project as it was. My solution, in order to demonstrate that I understood and could deploy CRUD functionality, was to create a separate webpage which only I knew the URL for (with no links in the actual website itself) which would have Update and Delete functionality built into it. This would basically be an admin page, and once I figure out how to create user profiles at a later date could be linked in to the main website as a section of the site only available to admins. 

Bibliogrpahy/influences:
Miguel Grinberg's Flask tutorials were very useful for understanding fully the functionality of what I was doing (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
Traversy media have some useful videos on a variety of topics - the videos on MongoDB on YouTube proved useful for double-explaining some key concepts (https://www.youtube.com/watch?v=-56x56UppqQ)
