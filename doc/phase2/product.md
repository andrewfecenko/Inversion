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

![](https://github.com/csc301-winter-2016/project-team12/blob/master/doc/phase2/images/main.png)  
Figure 2

![](https://github.com/csc301-winter-2016/project-team12/blob/master/doc/phase2/images/add_entry.png)  
Figure 3

![](https://github.com/csc301-winter-2016/project-team12/blob/master/doc/phase2/images/update.png)  
Figure 4


