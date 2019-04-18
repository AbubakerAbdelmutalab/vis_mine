Our preprocessing code has been set up as a demo version. Following the step-by-step instructions will create copies of all files used for the project and will not overwrite the submission.


How to run:

1. Query some log files. This is done through query_data_file.py. It uses a REST API to query the Cloudlab's Elasticsearch for log entries. The query itself is determined in query_file.json. The python file parses the json results and writes them into a tab delimited text file containing the timestamp and log message. 

NOTE: This will is not runnable without login credentials to the Cloudlab's Elasticsearch. We cannot provide them, but we have provided the result of this python file in 'logs/10krange.txt'. This file is the basis for our project.

2. Preprocess the log files. This is done with the processing.py file. It opens the text file created in the last step ('logs/10krange.txt'). It parses each line in the file with regex to determine a message type. The result of this file is a csv described in the project report.

3. Look up IP addresses. This is done with the get_location.py file. It queries keyCDN's REST api for location and ISP information about ip addresses in the parsed file. This takes several hours to complete, so if the file is run, a subset of data should be used. 

NOTE: for a demo, we have added a mode that only queries 20 IP addresses through keyCDN. This takes < 1 minute to complete.

4. Convert to Json: We need to then convert the final CSV to a json file for the website. This is done with csvToJson.py. This will write a json file into the web folder for use by the website.


The web code is in the web folder of this project. This website can be run locally by using npm's http-server inside the web folder. The live version of the site is at: https://turbosheep.github.io/vis_project/ 