# Technical Product Report
### What did you build during this phase?
###### Backend
- Implemented the original database structure, as well as methods to insert data and retrieve data from the database.
-  db_model.py includes the information about the database models, which is defined using SQLAlchemy. 
- db_function.py contains methods for inserting data into, and getting data from, the local database. 
- Each journal entry has a specific Entry table associated with it, and there can only be a single Entry per day.
- An Entry has a one-to-one relationship with a Summary table and a Plans table. An Entry also has a one-to-many relationship to a Task table, a CompletedTask table, a Knowledge table, and a FailurePoint table ([db_model.py](https://github.com/csc301-winter-2016/project-team12/blob/phase2-docs/db_model.py) lines 22-27). . 
- The relationship between the tables, as well the structure of the tables, is shown in Figure 1. 
- The tables (aside from Entry) contain content for a specific Entry (e.g., a Task instance contains a task for a specific Entry). 
- All callers from the front-end will use functions defined inside of db_function.py to get information that they need. If they need information about a specific section, such as the tasks associated with a specific entry, then they will get a list of strings returned to them ([db_function.py](https://github.com/csc301-winter-2016/project-team12/blob/phase2-docs/db_function.py) lines 145-151). 
- If a caller wants all of the information about a specific entry, then they can get an EntryContent object, which includes instance variables pointing to a list of strings for each of the sections ([db_functions.py](https://github.com/csc301-winter-2016/project-team12/blob/phase2-docs/db_function.py) lines 26-33). 
- If a caller needs information about all entries, then they can get a Python generator of EntryContent objects ([db_functions.py](https://github.com/csc301-winter-2016/project-team12/blob/phase2-docs/db_function.py) lines 194-196). 

![](https://github.com/csc301-winter-2016/project-team12/blob/master/doc/phase2/images/schema.png)  
Figure 1

###### Frontend
- Main_window interface: The main window page including Entry, Update Entry, Collection, Setting, Lock, and Favoriate buttons where each one links to an appropriate window respectivly (refer to Figure 2).
- Add_entry interface: In this page, the user can input their daily goals. There are three initial entries and the user is allowed to add more entries. If the user has less than three goals for the day, they can remove the entry textbox (refer to Figure 3). On submission, the user’s daily goals are recorded in the backend database.
- Update_entry interface: This page allows users to view and update an individual entry. The entry consists of five sections (Plans for Tomorrow, Goals, Goals Met, and Knowledge Gained), and clicking on the section name opens an accordion panel that contains a list of data in the section (refer to Figure 4). Each section has a form to add new data for the section (new data cannot be displayed dynamically yet).  
- Collection interface: This page allows users to look up past entries. There are buttons for each entry that leads to a details page for that day, and a search bar that allows users to search for a specific entry(refer to Figure 5).

![](https://github.com/csc301-winter-2016/project-team12/blob/master/doc/phase2/images/main.png)  
Figure 2

![](https://github.com/csc301-winter-2016/project-team12/blob/master/doc/phase2/images/add_entry.png)  
Figure 3

![](https://github.com/csc301-winter-2016/project-team12/blob/master/doc/phase2/images/update.png)  
Figure 4

<img src="https://github.com/csc301-winter-2016/project-team12/blob/master/doc/phase2/images/collection.png" style="width:200px;"/>  


Figure 5 

### High-level design of your software.
We are trying to build a journal mobile application. We want our app to focus on tracking progression and minimizing mistakes. Users enter daily information that they might want in a regular journal. They also include information about what they think were their mistakes for the day. While recording detailed entries of users’ every tasks, our app’s database also analyzes the frequent mistakes or goals that users failed to achieve. Ideally, by highlighting users frequent mistaks and failurs, our app will help users become more productive in their daily life. 

### Technical highlights: interesting bugs, challenges, lessons learned, observations, etc.
- Frequently committing and merging each other’s code within a large group was challenging. It will be more efficient if everyone is familiar with the git operations.
- Designing the mapping of flows for the application was considered challenging. As a daily journal application, it is critical to consider how the user would perceive the flow of the application with regards to the main menu. For example, after inputing daily tasks, the user should be directed to ‘update tasks’ so that they can enter more information. But entering the ‘update tasks’ page before ‘add tasks’ page violates the desired flow. How we will manage this mapping by designing the menu system and page redirection is crutial and needs more consideration. 
- Each member working on a different branch and sending a pull request once a reasonable number of task is done worked better because it prevented potential conflicts and it allowed everyone to see what other members are currently focusing on.

### What are you plans for the next phase?

###### Backend
- Create functions for selecting queries regarding certain information. (eg. tasks for Feb. 23, knowledge containing keyword “kivy”, etc.)
- Add “completed” attribute to Task (boolean value)
- Implement functionality to extract failed tasks and display them.
- Implement functionality to calculate what tasks are likely to fail.

###### Frontend
- Implement the frontend interface so that it can interact with the backend database.
- Make sure the window size is compatible with most mobile devices.
- Improve each section’s interface, especially the size of each buttons, padding and spacing.
- Merge ‘Favorites’ and ‘Collections’ pages, add ‘Daily mistakes review’, and remove the lock feature.
- Implement the search box so that it properly filters the entries.
