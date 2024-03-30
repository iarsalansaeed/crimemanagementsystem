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
1. [Core Domain Chart](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/class-uml/core-domain-chartt.png) - This chart shows domain, subdomains, and interactions of a crime management system, offering a detailed overview & workflow<br>
2. [Context Mapping Diagram](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/class-uml/context-mapping-cms.png) - Context mapping clarifies how different pieces fit together in complex systems. <br>
3. [Event storming diagram](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/class-uml/event-storming.png) - Event storming is a teamwork method to understand complex ideas better. <br>

## 4. Metrics
[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/project/overview?id=iarsalansaeed_crimemanagementsystem)

Few metrics that are listed below: 

- Quality Gate Status [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ShrutiPatil2223_Student-Management-System&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=iarsalansaeed_crimemanagementsystem)

- Bugs [![Bugs](https://sonarcloud.io/component_measures?metric=new_bugs&view=list&id=iarsalansaeed_crimemanagementsystem)](https://sonarcloud.io/summary/new_code?id=iarsalansaeed_crimemanagementsystem)

- Code Smells [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=ShrutiPatil2223_Student-Management-System&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=iarsalansaeed_crimemanagementsystem)

- Duplicated Lines [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=ShrutiPatil2223_Student-Management-System&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=iarsalansaeed_crimemanagementsystem)

- Lines of Code [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=ShrutiPatil2223_Student-Management-System&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=iarsalansaeed_crimemanagementsystem)

- Maintainability Rating [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ShrutiPatil2223_Student-Management-System&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=iarsalansaeed_crimemanagementsystem)

- Security Rating [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ShrutiPatil2223_Student-Management-System&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=iarsalansaeed_crimemanagementsystem)

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
These unit test files are created to validate the functionality of inserting data into the database and checking the database connection. The test_add_data method ensures that new records can be successfully added.
1. [Unit test 1](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/unittest.py) - This file is used to insert bulk dummy data into database by using a for loop.
2. [Unit test 1](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/unit-test2.py) - This however is used to only enter a single record into the database, I have used it when I had an issue with insertion at application, I used these and then solved my issue in application too.

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
I have created DSL related  to my project, the dsl file is in yaml format, and it is used by execute.dsl to update and create record at database. The example here is for update record along with screen shot.
1. [Yaml file](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/update_record.yaml) - contains my column names and name for what opration it is used, here it is UpdateRecord.
2. [Interpreter File](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/execute_dsl.py) - Upon the execution of this code, The records are updated in the database.
3. [ScreenShot](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/dsl-update-records.png) - Results after the interpreter file execution.

## 11. Functional Programming
1. [Immutable Data Structure](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/criminal.py#L13-L27) - The use of StringVar() from Tkinter to create immutable data structures for storing multiple attributes of criminals such as case ID, criminal number, name etc. While StringVar() itself is mutable, it's used in a way that the underlying value doesn't change after initialization, simply acting as an immutable data structure in the context of my application.<br>
2. [Side Effect Free Functions](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/criminal.py#L334-L384) - My functions such as add_data(), update_data(), delete_data(), and others, primarily deal with database operations and UI interactions. While they do have side effects (such as modifying the database or displaying message boxes), they encapsulate these side effects within their "specific tasks". The rest of the program remains unaffected by these operations, making the functions relatively side-effect-free within their respective domains.<br>
3. [Use of Higher Order Functions](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/criminal.py#L213-L216) - form of higher-order function usage in the event handling mechanisms of Tkinter. For example, when I binded a function to a button click (command=self.add_data), you're essentially passing a function (add_data) as a parameter to another function (button's command handler). This shows a basic form of higher-order function usage in a GUI framework.<br>
4. [Functions as Parameters that Return Values](https://github.com/iarsalansaeed/crimemanagementsystem/blob/main/criminal.py#L428-L462) - My code demonstrates the use of functions as parameters indirectly through the event handling mechanisms in Tkinter. For example the add_data(), update_data(), delete_data(), functions are passed as callbacks to button widgets. Additionally, while not explicitly shown, functions in Python can also return values, which could be utilized in a similar fashion if needed.<br> 
