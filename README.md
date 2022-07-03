# Challenge 2:

We need to write code that will query the meta data of an instance within AWS and provide a json formatted output. The choice of language and implementation is up to you.
Bonus Points : The code allows for a particular data key to be retrieved individually

________________________________________________________________________________________________________________________________________________________________


SOURCECODE: ch2.py

WHAT IT DOES? 
      --Give a json-formatted output after performing a metadata query on an AWS EC2 instance.
      --Retrieve the value of a particular data key.
      --It makes use of the http://169.254.169.254/latest/meta-data link-local address. 
      --Instance metatada is provided at this link, but only when you visit it from a running instance.
      
PREREQUISITES: 

      -- 1. Create a Linux EC2 instance on AWS. 
      
      -- 2. SSH into the instance
      
      -- 3. Install git and Python 3 on your instance. [sudo yum install python3 git]
      
      -- 4. Install pipenv. [sudo pip3 install pipenv]
      
      -- 5. Clone the GIT repository [git clone https://github.com/srsahay261984/challenge2]
      
      -- 6. Install Project Dependencies [pipenv install] 
      
      -- 7. Ensure import modules are already present if not do install.
      
      -- 8. Open the repository on your instance 
 
 HOW TO RUN THE SCRIPT:
  
 To get the complete instance metadata json dump, run the below command: 
 
        $ python3 ch2.py
        
 ![image](https://user-images.githubusercontent.com/108597286/177028326-58978bed-b9b8-4426-a487-6193b1402cfc.png)

To get specific metadata, find below the syntax of the command to run:

        $ python3 ch2.py keyname
        
 Examples:
 
 1. $ python3 ch2.py ami-id
 
 ![image](https://user-images.githubusercontent.com/108597286/177028525-8d398930-b5c9-47e6-a90e-b111fe2c87a1.png)

 2. $ python3 ch2.py owner-id
 
 ![image](https://user-images.githubusercontent.com/108597286/177028599-2bd63963-1886-4721-a5f1-fcb6407784b9.png)

 3. $ python3 ch2.py public-hostname
 
 ![image](https://user-images.githubusercontent.com/108597286/177028656-4275a67c-d2e5-4c0c-a913-88ff87df9c63.png)

        
 
