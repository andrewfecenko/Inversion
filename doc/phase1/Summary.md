## Product Detail

We want to create a mobile application. potentially including some of the preliminary sections shown in the below image as the base. We want to show users what they're repeatedly doing wrong, so they can stop making those mistakes.

![](https://github.com/csc301-winter-2016/project-team12/blob/master/doc/phase1/images/raw_layout.jpg)

While there are other applications like [Wunderlist][wunderlist-link], which allows you to create todo lists for daily activities, and [Habitica][habitica-link],
which focuses on creating habits to improve your productivity, our application would focus on minimizing mistakes. This is an extra feature that would exist on top of the basic journal. Other journal apps, like [Diaro][diaro-link] seem to focus on recording long thoughts or capturing moments. We want journals with our app to focus on tracking progression. A section like "Day Summary" is there to provide context. What's more important is that the user can figure out what needs to change for them to better achieve their goals, which is where highlighting mistakes is helpful.

[wunderlist-link]: https://www.wunderlist.com/
[habitica-link]: https://habitica.com/static/front/
[diaro-link]: http://www.diaroapp.com/


## Target Audience

Our target audience are students and working adults who are used to current technology, meaning they have had previous experience on other daily journal applications. We want to help those who ccould not be motivated by existing applications that mainly focus on simply creating future tasks. As mentioned in the product detail, our users will benefit better from understanding their past mistakes, and will be motivated to improve their lifestyle by not repeating the same mistakes. As we extend and shape our project further, we will have a more clear idea on who else might want to use the app.


## Method

The idea of highlighting mistakes stems from the idea of inversion, which is a method for solving problems by attempting
to address them backward. Instead of trying to come up with ideas on how to advance towards a goal, a user would try to
avoid things that definitely wouldn't bring him closer to it. Inverting a problem doesn't always work out, but it does
help avoid trouble. It's easy to think of inversion as an avoiding stupidity filter. Users would be required to paste in
their daily mistakes manually, and the app will focus on highlighting more common mistakes the throughout weeks and
months. 


## Construction

We will be coding in Python, and using the [Kivy][kivy-link] framework to build a mobile app that runs on Android (
potentially also on IPhone). There is a front-end component that deals with providing a way to browse journal entries,
add new entries, and review highlighted mistakes. There would be a back-end component that deals with storage and
manipulation of journal data, as well as a section that scans through and extracts information from the highlighted
mistakes. Later on, there should be a way to have both online and offline storage for journal data. 

[kivy-link]: https://kivy.org/


## Potential Challenges

We will have to try our best to differentiate our app from numerous other task-manager/daily-planner apps out in the
market. Programming-wise, our major challenges will relate to how we want to implement the technical parts of "finding
repeated mistakes." Team members working on the back-end will have to improve their knowledge on natural language processing.
On the front-end, issues have to deal mainly with handling increasing code complexity - the initial view codebase should
be extensible, so that more features can be added to the project. Because Kivy uses it's own language for displaying
material on the screen, there won't be too much documentation available on how to structure code.  
