## Setup
  - Create a fork of this repo with the following naming convention ```[first-name]-[last-name]-jenkins-build-project```
  - login to the jenkins console with supplied credentials
    
    http://3.21.225.172:8081/
   
## Project
  You need to create two jenkins build projects for each branch of this repo. ```simple``` and ```build-required```.
    
## ```simple```
  1. Create a jenkins build project with the naming convention [first-name]-[last-name]-simple
  2. The build needs to trigger anytime there is a push to the ```simple``` branch
  3. The build needs to copy files from the ```simple``` branch to the server folder ```/var/www/jenkins-projects/[first-name][last-name]-simple```
      - your build needs to create the folder if it does not already exist
  
  After the build verify you see the following text when going to ```http://3.21.225.172/[first-name][last-name]-simple```

  ![image](https://user-images.githubusercontent.com/31535228/147724558-972b0bdf-cc8a-4bae-97b0-2dc3f197087d.png)

## ```build-required```
  1. Create a jenkins build project with the naming convention [first-name]-[last-name]-build-required
  2. Trigger anytime there is a push to the ```build-required``` branch
      - your build needs to create the folder if it does not already exist
  4. Create and activate a python venv inside your new ```build-required``` folder
  5. Install required python packages inside your new venv from the included ```requirements.txt``` file
  6. Run the python file with the following argument ```/var/www/jenkins-projects/[first-name][last-name]-build-required```
  
  After the build verify you see the following text when going to ```http://3.21.225.172/[first-name][last-name]-build-required```
  
 
  ![image](https://user-images.githubusercontent.com/31535228/147724984-7dcdf22d-becb-4a5a-9ca5-f5ef4eb4d79a.png)
  
