# GitHub-bot

1 - Introduction

  A GitHub bot that automates the creation of new repositories. With a few commands you can automatically create a repository, folder and ".py" file to start working. You can also select if you want a repository to be public or private. As default, the repository will be published under MIT licensing.
  
2 - Technical talking points

  The project it self comes from the ideia to automate boring stuff. For this reason I decided to create this, to automate the creation of a complete workplace to starting coding. It'll be challenging to introduce some new features such as the possibilite to choose which licesence, but imagination is the only limit.

3 - Technologies and Languages
  This project is all writen in Python 3.8 and uses a few libraries:
  
      • OS - To navigate and create a folder (you'll need to change the directory on the source code)
      
      • Time (Sleep) - To take a few seconds to be sure that de URL loaded propelly and the program don't crash
      
      • Selenium - This is the library that has the feature to control the browser to create the repository on GitHub
      
      • Firefox browser developer - Selenium doesn't support google chrome anymore, so firefox is the way on this
      
      • Gecko driver - This is the interface between Selenium and Firefox
      
 
4 - Setup and use
  The only thing you'll need to setup and run this script is a folder with the source code and Gecko driver. Then, just execute the source code on your IDE and thats it.
  
  Once the code is running it'll ask for a few inputs:
  
  • "What are we making today?" - Just enter the name of the project you're creating. This will be the name of the repository, the name of the folder and the name of the ".py" file.
  
  • "Enter your login" - Just type your login on GitHub, or change the variable to your GitHub's login.
  
  • "Enter your password" - Just type your password on GitHub, or change the variable to your GitHub's password.
  
  • "Whats the description of the repository" - This will be the description of the repository, once it creates a repository with a Readme file this variable will be it's content either.
  
  • "Is the repository public?" - This is where you choose between a publibic repository and a private repository. To make a public repository use YES as "y", and NO as "n".
  

5 - Contributions, issues and forking
  Be confortable to make any changes you want. To improve the code, to update the code or just to try to implement a crazy ideia. "Mi casa, su casa", or should I say "mi repositorio, tu repositorio".
  
6 - About me
  Hi there! I'am a undergraduated nutrition student that on a quarentine felt in love for programing. So basically to train coding and apply the knowladge on Selenium I created this bot. It may not be perfect (as well as my English), but I'am trying my best to learn a new field of knowladge.
  
7 - Show your support
  I don't have in mind to be the best programmer in the world, but I'am here to learn from my mistakes. With that said, if you could, please leave a star and point out some improvements I can make on the code. Or even send me a mensage with some tips to make my learning process easier, every help counts. Thanks
  
  
8 - Useful links and tool

Install Selenium:

  • pip install selenium
  
  • https://pypi.org/project/selenium/
  

Download and install Firefox developer:

  • homepage: https://www.mozilla.org/pt-BR/firefox/developer/
  

Links for the web drivers to use with Selenium

  • Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
  
  • Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
  
  • *Firefox: https://github.com/mozilla/geckodriver/releases* - This is what you need
  
  • Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/
  

