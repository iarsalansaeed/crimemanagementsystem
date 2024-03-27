# crimemanagementsystem
Criminal Management System
Overview
The Criminal Management System is a graphical user interface application developed using the Tkinter library in Python. It provides a platform for managing criminal records, allowing users to input and store information about criminals.


## 1. Git as VCS
I have used git before for out VCS or as SCM. 
It keeps track of changes in project, collaborate with others, and manage different versions of your code easily, share your code with fellow and allowing them to contribute with access limitation etc, like fork and PR etc. Its makes the work seamless and more faster. It allows users to manage their codebase efficiently, revert changes if needed, and work on different features concurrently.


## 2. UML Diagrams
UML diagrams :<be>
1. [Activity Diagram](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/class-uml/activity-diagram.jpg) - Activity Diagram shows the working of Crime management system.
2. [Sequence Diagram](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/class-uml/sequence-diagram.jpg) - This diagram shows the connection between objects by showing messages.
3. [Use Case Diagram](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/class-uml/Use-case-diagram.jpg) - This Use Case Diagram shows the interaction between CMS GUI and user/administrator.
4. [Class Diagram](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/class-uml/class-diagram.jpg) - The class diagram shows the structure and relationships of classes in a system.

## 3. DDD
1. [Core Domain Chart](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/class-uml/core-domain-chartt.png)<br>
2. [Context Mapping Diagram](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/class-uml/context-mapping-cms.png) <br>
3. [Event storming diagram](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/class-uml/event-storming.png)<br>

## 4. Metrics
[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/project/overview?id=iarsalansaeed_crimemanagementsystem)


## 5. Clean Code Developement - CCD
Clean code Developement [Cheatsheet](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/cheatsheet.txt).

Examples:
Following are the transformation example of many lines of code into fewer lines of code, more readable and reusable.<br>
1. [Example 1](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/criminal.py#L29-L40) - Setting up variable one by one to setting up variable by using a function, by this way our code lines becomes short and is easily understandable.<br>
2. [Example 2](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/criminal.py#L286-L315) - Another example of CCD where I was writing one by column name and assigning it a specific width. It was repeating thing so I thought why not use a function and do it. I then used a function and did it, code is very clean and understandable.
3. [Example 3](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/criminal.py#L403-L426) - Here for filling my form as I fetch data, I needed to use all variables, tried it one on one it was much of work repeated so again used function and a variable named 'variables' to loop over and make the code clean.<br>

## 6.& 7. Build and CI/CD
I have used Jenkins for the build and Continuous Integration/Continuous Deployment (CI/CD). My project is in Python, hence I have used Jenkins with which I am used to working, Python doesn't require build as java programs require for which Maven, Ant etc are used. 

Jenkins LogIn [LogIn Page]()<br>
Setting SCM [SCM - Setup](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/jenkins/SCM-jenkins-linking.png) - This is SCM stage setting up by configuring the pipeline.<br>
Build Trigger [Build - Trigger](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/jenkins/Build-triggers.png) - In this stage, I have configured my project's build trigger, as to when it should be triggerd.<br>
This is a screenshot of the whole [CI/CD](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/jenkins/Jenkins-ci-cd.png) pipeline.<br>
Whole Pipeline output - [Pipeline Status - Console Output](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/jenkins/jenkins-complete-ci-cd.png)<br>

## 8. Unit tests

## 9. VS Studio IDE
I love using VS because it's super handy and has lots of cool stuff. It helps me write and test my code, and it's easy to use. Plus, it works great with Git, which is awesome for keeping track of changes in my projects.<br>
Code . : My most fav shortcut, In terminal, code . opens the current directory in VS Code.<br>
Ctrl + S: Save current file.<br>
Ctrl + F5: Run application without debugging.<br>
Ctrl + F: Find text in your code.<br>
Ctrl + H: Replacement of text.<br>
Ctrl + Shift + F: Find in files across your entire solution.<br>
Ctrl + D: Duplicate the current line.<br>
Ctrl + Shift + L: Delete the current line.<br>
Ctrl + Shift + ~: Open terminal.<br>
Ctrl + K, D: Format the document to the default settings.<br>
Ctrl + Shift + B: Build your solution.<br>
Ctrl + .: Open the Quick Actions and Refactorings menu.<br>

## 10. Domain Specific Language (DSL)

## 11. Functional Programming
