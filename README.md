
## 1st part - Code.

This is a simple PySpark project setup. Please setup this project on you laptop and make sure you can run the tests using `make test` (Initially test won't pass). 

Get familiar with the code and the data within the folder `tests/data`.

You will be asked to implement some PySpark transformations on the data during the live coding interview. During the interview you will be allowrd to use any resource online (Google, ChatGPT, etc..)


## 2nd part - Package and Deploy.

Please research in advance how would you deploy and run this code on the cloud. Preferably on GCP Datproc but other platforms will be accepted as well. You'll be asked to explain about these steps and how would you integrate them into the CICD pipeline. 

This code won't be tested but would be nice to have prepared the code (or pseudocode) into the `Makefile` on the blocks:

```make
build:
    # Add commands to build the code here

deploy:
    # Add commands to deploy the code to GCP Dataproc here
```

