## Scrape Digging

**Project management**  

https://github.com/jodiefostersarmy/scrapedigging/projects/1

**Overview**  

This app will search music mixes from the internet and give the user the results, much like Google and their search engine. You can create your own mix playlists and play from the app.  

It is a search engine, music mix database, listen later playlist, and track identifier that will return the music track details from a mix for song reference.

It is based on https://listennotes.com and https://getpocket.com/. 


#### Installation
To maximise the benefit of this app, you will need Python3.8 installed and begin to follow the steps below to set it up.  

- Clone the repo: ``` git clone https://github.com/jodiefostersarmy/scrapedigging```

- Move into the repo directory: ```cd scrapedigging/```
- Install a virtual environment: ```pip3 install venv```
- Create a virtual environment: ```python3 -m venv venv```
- Activate the virtual environment: ```source venv/bin/activate```
- Install the dependencies from the requirements.txt file: ```pip3 install -r requirements.txt```
- Run the app: ```python src/main.py```  

#### CI/CD
The CI/CD pipeline has been created using GitHub actions and uses Python3.8 and Pip3 to run the latest stable version of Ubuntu. The pipeline kicks off by pushing on main repo.

Once it pulls from main, it will install the dependencies outlined in the [packages used section](#packages-used).  

#### Usage

#### Packages Used


#### Wireframes
**Landing Page**  

This is where the user will first land, and will be able to access search functionality. However, saving searches or creating playlists can only be accessed with member log in credentials. The layout is sparse and minimal to minimise distractions, similar to the google search bar. 

Members can search by genre, artist, radio station or record label.

![Landing Page](/docs/wireframes/1.png)

**Log in page**  

The page changes into a form which the user will fill in with their details to log into their dashboard, or if they aren't members they can click the sign up button that will take them to a new page.

![Log in Page](/docs/wireframes/2.png)

**Sign up page**  

Much like the log in page, the sign up page will take in a name, email and password of the user's choosing, that must be at least 6 characters long. The idea is that the forms have an intuitive flow, so that each form should be simple and concise and not need a form wizard.

![Sing up Page](/docs/wireframes/3.png)

**Dashboard**  

The dashboard will be custom to each user.
But it will have:
  - Search function
  - Users' saved favourite mixes
  - Create playlists button
  - Notifications for new mixes from followed artists or music stations
  - Edit user profile button, which takes to edit profile page.
  - Logout button

![Dashboard Page](/docs/wireframes/4.jpg)

**User Profile**

This page allows the user to change/upload their first and last name, password and profile page image. It will also allow them to logout or delete their account if they wish to. 

![User profile Page](/docs/wireframes/5.png)

**Playlist**  

This page allows the user to add to a previous playlist, delete an old playlist or create a new playlist. It also allows the user to add or remove mixes in this window. This is intended to folder the users mixes into preferred groups.

![Playlist Page](/docs/wireframes/6.jpg)

**Search/Add/Remove Mix**

When the user selects to "Add" a mix to the playlist, it will bring up the search bar, the results are returned to the user just like the regular guest functionality, however once the user clicks into a selected mix, it will have the button for the functionality to "ADD" to the a playlist of your choosing. The user will be able to add the mix to multiple playlists and will be depicted by the tick for addition confirmation.

In these wireframes also outline the search functionality. In the results wireframe, the search will first run through all saved and favorited mixes in the database before calling out to the scraper. These will show first with additional information that tells the user that there is a similar mix in a playlist or favorites.

![Mobile search, add and remove Page](/docs/wireframes/7.jpg)

![Desktop search, add and remove Page](/docs/wireframes/8.jpg)

#### WIP DB Schema  

