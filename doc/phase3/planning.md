#Planning 

### Initial Planning
##### Front-end
- Make update_entry and collection front end retrieve data from database 
(since we have been using an array of sample data for testing in previous phases).
- Make update_entry front end insert data into database.
- Enable delete/edit buttons in update_entry (retrieve user input and update database).
- Mistakes Summary page: This page displays history of the user’s mistakes. At first, we’ll try to display the most 
commonly appearing  mistakes based on the most frequent nouns and verbs appearing in mistake sentences. 
- Yesterday’s Mistakes page: This page lists yesterday’s mistakes. 
- Improve UI for already existing pages and make designs consistent over different pages.

##### Back-end 
- Implement functions to delete information from the database.
- Implement functions to update information in the database. 
- Implement functions to filter an entry given a specific day. 
- Implement functions to extract most common nouns and verbs from a sentence (used to get information about mistakes).

### Updated plan
Due to team members having busy schedules, we started work late on the project. Some of the features we were planning to implement by March 16th will be delayed to March 28th (Demo day).

##### Front-end
- Creating UI for yesterday’s mistakes and the mistakes summary page was delayed. 
- Making all of the pages (except for the Add entry page and Update entry page) consistent was delayed.
- Making the Collection page (refer to [collect.py](https://github.com/csc301-winter-2016/project-team12/blob/master/collect.py))  retrieve data from the database was delayed.

##### Back-end
- Implementing functions to extract most common nouns and verbs from a sentence was delayed. 


Complete this report with a review and Retrospective: 
Describe how your plan and process actually worked.
The plan did not go as well as we thought it would. Time management was the most challenging factor of phase 3, because of group members’ workloads. Although we have created issues online for all members to see and self-assign, we weren’t able to implement all the features we planned to. Using a self-assign process was sometimes confusing (it’s difficult to tell if you can claim a task for yourself) The process for committing features worked well. Everyone added changes to a feature branch, and followed through with submitting and merging pull requests.


What worked according to plan? What didn’t?
Most of the back-end part was implemented as expected (refer to revised plan). We managed to improve the UI appearance and establish the connection between database and basic data entry/retrieve interfaces on add-entry and update-entry pages, but this is not yet implemented in the collections page. This collections page also needs to be able to generate buttons for each entry.
In the initial planning meeting, we wished to finish the main features of the mistakes review interface. However, we were not able to implement the connection between mistake analysis interface and database in time as well as create the actual page UI. We will work to finish the tasks by our upcoming demo, or else they will be the priority tasks for the next coming phase.

Screenshots here

Any improvement suggestions? Interesting insights?
Definitely we plan to start early in the next phase. As we have to keep working to finish the desired features of our app by the demo date on the 28th, we will try to keep the working flow until the last demo on the April 4th, which is not that far from 28th, as well. One interesting we learned was that even though we self-assigned tasks to oneself through Github instead of actually having a meeting to discuss distribution of work, most members of the team work willing to put effort into the project and looked for jobs they could take charge of. We hope to meet more often in the next phase though, preferably offline, as we discovered offline meeting help greatly in advancing our progress and enhancing overall understanding of current state of the project among our members.

While most members struggled to familiarize themselves with new technologies such as Kivy and SQLAlchemy in the previous phase, there were fewer technical issues in this phase. For most problems we encountered (like database not working as expected, or kivy display limiting grid options), we were able to solve it by discussing with other team members.
