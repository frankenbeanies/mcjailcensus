mcjailcensus - frontend
=======================

Monroe County Jail Inmate Census - frontend

Forked from the [original repo](https://github.com/thequbit/mcjailcensus) by [Timothy Duffy](https://github.com/thequbit). Please consult his original repo for differences between the Readme and project.

Site viewable at http://mcjailcensus.herokuapp.com

###Why Fork?###

Although the frontend website will be different in nature, it will be heavily reliant on [Timothy Duffy](https://github.com/thequbit)'s original script in order to pull the most current data. As it is really just an offshoot of [Timothy Duffy](https://github.com/thequbit)'s project, it made the most sense to me to fork it. 

###Overview###

This is going to serve as a frontend that can show current booking information and statistics for the Monroe County Jail. As with the original, it is: " a tool that will pull the current PDF off the Monroe County website that has the County Jail Census information
within it.  The tool pulls from this [url](http://www2.monroecounty.gov/sheriff-inmate) and downloads the currently
posted PDF document.  It is important to note that the PDF is not always current, and does not appear to be uploaded at
the same time each day.

Once the script runs, it saves the PDF document locally, converts it to text, and pulls all of the inmate information out of it.  It then saves this information as a large JSON file locally. "  Where it differs is that the data is then consumed by a Django application which can be accessed by the public. 

###Install###

	> pip install Django
    > pip install beautifulsoup4
    > pip install http://pypi.python.org/packages/source/p/pdfminer/pdfminer-20110515.tar.gz

Please ensure that you install that exact version of pdfminer. More recent versions may break the process_pdf command!

###Whats not included?###

For security reasons, I have not included the settings.py file. You will have to do that yourself. Batteries are not included. 
    
###Running Tools###

***All scripts must be installed as in the repo in order to work! I take no liability for damages caused by running scripts***

There is a single script file that will find the pdf, download it, convert it, scrub it, process it, and then push it 
to a json file

    > python ./tools/censusprocessor.py

Another script will take the generated json, and convert it to a csv with the format of last,dob,sex,middle,race,mcid,first .

    > python ./tools/json-readable.py

Another script will take teh generated csv, and fill out a django connected database. The database must be defined via settings.py

    > python dbfiller.py


###Run Django Server###

With a  settings.py file (**that has database options configured**) placed in the lower of the two mcjailcensus directories, from the same directory as manage.py, run the following commands:

	> python ./tools/censusprocessor.py
	> python ./tools/json-readable.py
	> python manage.py syncdb
	> python dbfiller.py
	> python manage.py runserver

Then, from the browser of your choice, navigate to 

	http://localhost:8000

or whatever your configured the runtime url to be. 
    
