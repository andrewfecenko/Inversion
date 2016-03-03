# Process Report
### Initial Planning
###### Your definition of “Scrum master”
Our Scrum master is Abrar, and his main tasks include:
- Distributing tasks: He distributes a fair amount of work to each of the group members based each individual's technical skills and experience. Since some of us are more experienced than others, he held several short meetings to ensure that everyone was on the same page and that no one was left behind.
- Managing repository: He always watches out for our repository, so that no conflicts or overwrites happen. He also set up a Wiki page about correctly using Github.
- Communication: He frequently communicates with both the backend group and the frontend group to let each other know of the current status of our sprint.

###### How did you estimate task size?
Each team member first writes their own estimation of tasks on paper and exchages ideas during the meeting. The way to come up with an estimation for each individual is to describe the corresponding feature and ask yourself what the complexity and priority is in implementing it according to your experience. The size of tasks should be relative to one another, and not depended solely on each team member’s personal programming skills. After comparing answers between team members, we negotiate and reach the final consensus as a team. The rule of thumb is always to keep the average stable velocity of the whole team.

### Sprint Backlog
###### What did you initially plan to build?
We were initially planning to build a mobile journal application with basic functionalities. Specifically, the backend group’s main task was to design a database schema and create models for database.Their initial tasks also included writing programs for database interaction, such as functions that fitlter or insert data, which were to be used in the frontend. The frontend group’s initial task was to build a working application that allows simple interactions such as displaying journal entries to the user and letting them input and send data. Each member of the frontend group were assigned one of the main views of the applications (start page, “Enter Tasks”, “Update Task”, “Collection”) at the beginning of the sprint.

- Link to google doc for product backlog:
[product_backlog](https://docs.google.com/document/d/1uXtG43CzZRig-FC1BOYNw3aYHi4ZhYMMwEpc99hQ6J8/edit)

- Issues:
[issues](https://github.com/csc301-winter-2016/project-team12/issues)

######How did you plan to build it?
We first break down the main features of the application into several tasks, then roughly estimate the size and order of tasks based on our previous software developing experience. The estimation may not be precise since we did not have a clear picture of what exact tasks we need for each feature and how we will implement them in details. As team members work on their task throughout the sprint, they may find some tasks taking longer than the estimated time, while others may finish their work earlier than expected. In this case, we re-estimate and update the tasks to make sure the teamwork is still effecient.
For the task assignment, our approach is to focus on the skills gap that identify tasks. For example, most of us did not have sufficient experience with Kivy at the frontend, thus we formed pairs so that knowledge can be shared during the developing process and hence enhance productivity. 


### Update Meetings
###### Feb. 23, 2015: Everyone @Google Hangout
- Discussed the plans for this phase.
- Came up with the product and sprint backlog.
- Broke down the tasks, decided on their sizes and split them fairly among everyone.
- Abrar shared some resources to help with learning Kivy.

######Feb. 27, 2016: Abrar, Andrew, Chris @BA
- Discussed basic structure for page layouts, including what buttons should be on the main page and what functions each pages will serve.
- Some frontend tasks got reassigned and completed by other members.
- Implemented basic database model sqlalchemy. This turned out to be less than a L-size task, but was important and needed to be done first nonetheless.
- Tested some code for database interaction to check if database was properly set up.

######Mar. 01, 2016: Abrar, Elsie, Asako @ BA
- Reported progress in the frontend.
- Discussed what exactly needs to be present in each section.
- Deffered frontend implementation of unimportant sections, such as ‘Favortites’ and ‘Settings’, and sections whose systems are not yet implemented yet, such as ‘Review Mistakes’.
- Reassigned tasks for the frontend group.
- Decided to at least complete simple prototype of the application. (We still need to have a working application before the demo.)

######Mar. 02, 2016: Elaine, Angel, Elsie, Asako @ BA
- Discussed the communication between different pages of the application.
- Discussed the common problems the frontend members are having with Kivy.
- Shared knowledge regarding challenges such as sizing in Kivy and passing variables between .kv files and .py files.
- Elaine and Angel collaborated on the “Collection” page.

### Burndown chart
![](https://github.com/csc301-winter-2016/project-team12/blob/master/doc/phase2/images/burndown.png) 

Y-axis represent days. Large, Medium, Small size tasks were converted to 3, 2, 1 days.


### Review & Retrospective
###### How did your plan evolve?
- Tasks that were simply not done (and why)
We did not yet implement the key feature of our application - ‘Review mistakes’. The reason is that it heavily depends on other features. It would be better to implement it in the next phases when all the other features are already implemented properly.

- Tasks that were split before being completed (and why)
When creating functions to interact with the database, we decided to split the task so we first implement functions for simply creating and extracting different attributes of a day Entry. With these functions at hand we could test our database easier. We will also create functions for filtering queries in phase 3, given appropriate information. (date, topic, etc.)

###### Provide thoughtful, retrospective reflection on your process
- Identify decisions that worked well 
The assignment of tasks worked as expected. Despite some reassignments of tasks and reordering of priority, all team members finished their part of the work and some even did additional tasks.

- Identify decisions that didn’t work well
The interaction between backend group and frontend group was not as efficient as expected. Both groups had their own group meetings, which resulted in lack of communication between the two groups.

- Suggest concrete improvements
We were not consistant with team meetings and met whenever we could, but only members who could show up participated. We should come up with a more solid weekly meeting time (with ideally everyone showing up).




