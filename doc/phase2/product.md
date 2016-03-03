# Technical Product Report
### What did you build during this phase?
###### Backend
- Implemented the original database structure, as well as methods to insert data and retrieve data from the database.
- Each journal entry has a specific Entry table associated with it, and there can only be a single Entry per day. 
- An Entry has a one-to-one relationship with a Summary table and a Plans table. An Entry also has a one-to-many relationship to a Task table, a CompletedTask table, a Knowledge table, and a FailurePoint table. The relationship between the tables, as well the structure of the tables, is shown in Figure 1. 

![](https://github.com/csc301-winter-2016/project-team12/blob/master/doc/phase2/images/schema.png)  
Figure 1
