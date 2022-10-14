# CSC301-Assignment2
This repo is for CSC301 Assignment 2, contributed by Tingzhou Gu and Jiabao Leung

Following will be the instuctions on how to use the applications
 - The application is written in python and kivy \- (a python framework). 

# Instructions

User is able to run the .py code along with the .kv code.

The codes in python and kivy can be compiled to installation file for Android and IOS. 
Additionally, kivy itself is able to run in Android and IOS.

Kivy codes can be converted to .apk form in Linux environment.

Converting and debugging on Android devices will take too much workload, completing it is not available before the deadline for this assignment. 

The codes runs well on PC and screen & buttons are resizable, 
so it should be good in any mobile device.

----------------------------------------------------------------------------------------------------------------------------------------------------------

# CSC301 - Assignment 2 Report
### Tingzhou Gu & Jiabao Michael Leung
##### Overview:
For this assignment, we chose to look into developing the checkout price calculator for mobile platforms. This decision was largely informed by the fact that such a mobile application does not require an active network connection and, thus, would potentially be of more use in this context. In order to pick an appropriate tech stack for the application, several points were considered, including ease of development, testing, and deployment. Listed below are several of the options that were explored, along with a brief explanation of our thoughts leading up to our choice of tools for development.  
##### Picking the tech stack:
While researching for our mobile stack, the following options stood out:

- Swift / Kotlin
- Kivy
- BeeWare

###### Swift/Kotlin
Swift and Kotlin are key programming languages for writing iOS and Android applications respectively. While Swift is the successor of Objective-C, Kotlin is a Java-based language developed by JetBrains. While both are extremely popular for their respective platforms, we decided to make our application 

Due to the intended purpose of this calculator, we found a single open-source GUI Python library called Kivy to be sufficient for our mobile stack needs, including developing the graphical interface in the frontend and calculation logic in the backend. Furthermore, because Kivy is based on Python, unit-testing 
