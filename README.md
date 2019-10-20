# hello-python
Hello python gets tested, built by Travis and sent to Cloud Foundry.

#### Running the app
Required packages to run the app are `python and pip`.  
It's assumed you're running GNU/Linux or Apple™️ Mac OS X.  
Clone or download the repository.  
Install python dependencies by running `pip install src/requirements.txt`.  
Export the port you're going to use, for example `8080` with `export PORT=8080`.  
There's also an environment script which you can source for your convenience.  
Now you can run the application by using `python src/hello.py`.

#### Testing the app
The test folder contains some tests.  
To run them, execute your favourite python test framework from the root directory,
of course after setting your desired port.
For example `pytest` or `nosetests`.
