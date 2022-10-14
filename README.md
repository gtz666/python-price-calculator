# CSC301-Assignment2
This repo is for CSC301 Assignment 2, contributed by Tingzhou Gu and Jiabao Leung

The application is written in python and kivy (a python framework). 

Following is the instruction on how to run the application, and our reports.


## Instructions

User is able to run the .py code along with the .kv code.

The codes in python and kivy can be compiled to installation file for Android and IOS. 
Additionally, kivy itself is able to run in Android and IOS.

Kivy codes can be converted to .apk form in Linux environment.
Converting and debugging on Android devices will take too much workload, completing it is not available before the deadline for this assignment. 
The codes runs well on PC and screen & buttons are resizable, 
so it should be good in any mobile device.

Because we don't have the .apk file, we can test the aplication on any PC or laptop devices. The codes is built in PyCharm IDE and kivy virtual enviornment.

To run the codes, here are some advices:

- Installed kivy and python 
- Installed kivy package
- Open Python IDE (In this case, we use pycharm)
- Set up kivy's virtual environment
- Run the application.py file (There is no need to run the .kv file separately)
- For testing, run test.py

----------------------------------------------------------------------------------------------------------------------------------------------------------

# CSC301 - Assignment 2 Report
#### Overview:
For this assignment, we chose to look into developing the checkout price calculator for mobile platforms. This decision was largely informed by the fact that such a mobile application does not require an active network connection and, thus, would potentially be of more use in this context. In order to pick an appropriate tech stack for the application, several points were considered, including ease of development, testing, and deployment. Listed below are several of the options that were explored, along with a brief explanation of our thoughts leading up to our choice of tools for development.  
#### Picking the tech stack:
While researching for our mobile stack, the following options stood out:

- Swift / Kotlin
- Kivy
- BeeWare

###### Swift/Kotlin
Swift and Kotlin are key programming languages for writing iOS and Android applications respectively. While Swift is the successor of Objective-C, Kotlin is a Java-based language developed by JetBrains. While both are extremely popular for their respective platforms, we decided to give our application cross-platform capabilities while maintaining a single codebase. Choosing an option that allowed for cross-platform development would mean more effective resource management in terms of time and manpower, the ability to cater to a wider range of users, and simpler/quicker customization down the road if needed. Thus, we decided to examine other options intended for cross-platform development instead.

###### Kivy
Kivy is an open-source graphical user interface Python library that allows for multi-platform development across platforms inckluding Android, iOS, Linux, and Windows. This was an attractive option because of our relative comfort in Python development. Furthermore, as it is open-source, there are many libraries available to be used should the need arise.

###### BeeWare
Like Kivy, BeeWare is another open-source cross-platform framework based on Python whose mantra is "Write once. Deploy everywhere". 

###### Kivy vs. BeeWare
Due to our relative comfort with Python development, Kivy and BeeWare were both attractive options. However, while both are popular Python mobile application development frameworks, we chose to move forward with Kivy for the following reasons. Due to the intended purpose (and relative simplicity) of this calculator, we found Kivy to be sufficient for our mobile stack needs, including developing the graphical interface in the frontend and calculation logic in the backend. Where BeeWare differs from Kivy is its usage of the respective platform's native UI, meaning that applications developed using this framework would look and feel more familiar for users across various platforms. On the other hand, Kivy's custom UI toolkit means that the application would not have the same native appearance, but a consistent appearance across different platforms instead. Furthermore, we valued Kivy's relative maturity, having been a tried and true technology since 2011 with excellent documentation and open-source resources. Furthermore, because Kivy is Python-based, developing unit-tests would be straightforward for this application, making it suitable for this project. Finally, PyCharm was our choice of development platform, seeing as it is a Python IDE that we are familiar with. Installing and setting up the kivy library was trivial.

#### Database Idea
When this application is in the real world, for example, the users are the cashier in a supermarket. It is useful to have a database for them, and it makes this application more functional. We can have a map with goods id: price, as the database. And inputting id in the price calculator will automatically get corresponded price. It will be easier for the actual user to have access on prices without remembering prices of goods, to use this application.

## Summary
We are doing a mobile application for the checkout price calculator for this assignment. We had three code file in our repo: application.py, Calculator.kv, and test.py. We chose python and kivy (a python GUI interpreter) to develop the application because of our maturity of python and ease of development, and we use a kivy unit test for testing. Since we are doing a mobile application, we were making sure the tech stack we chose is suitable for mobile devices, and screen size is resizable to fit any mobile device. There are no backends and frontends differences, we are focusing on the GUI design and adding different functionality, which is all frontend techniques. We have also considered some database ideas. For example, as we explained above, we could have a map of id: price for the database. This increases usability of the application, users only need a list of goods ids to use this application. 

This application is also easier for testing, because the codes are mainly in python and kivy, we added some arithmetic error checking for the python file, and we added a unit test on the graphical side. We could run test.py to test the kivy file. Maintaining this application is also easier, because the application does not require any Internet connection to run, users can simply update if there is a new version of the application. The application is runnable on our PC devices. We have listed some instructions on how to run is application. 

There are some nessesary assumptions for this application: Users have to input prices in the calculator. Since we didn't have a .apk form of the application, running the program requires the python and kivy environment to run the application. This situation can be improved by converting the files into .apk form and debugging on an Android device. This will only require an Android device to run the application and there is no need for any python and kivy environment.


#### References
Apple Inc. (2022). Swift. Apple Developer. Retrieved October 14, 2022, from https://developer.apple.com/swift/#great <br>
JetBrains. (2022). Kotlin for Android: Kotlin. Kotlin Help. Retrieved October 14, 2022, from https://kotlinlang.org/docs/android-overview.html <br>
Keith-Magee, R. (2022). Beeware. BeeWare. Retrieved October 14, 2022, from https://beeware.org/ <br>
The Kivy Authors. (2022). Welcome to Kivy. Kivy. Retrieved October 14, 2022, from https://kivy.org/doc/stable/ <br>
