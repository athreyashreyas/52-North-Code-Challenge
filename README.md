# Code Challenge for 52° North
Repository for the code challenge given by 52°North as part of GSoC 2023. The project aims to build a wrapper for python clients wishing to use the OGC Processes API. Since a lot of OGC endpoints have similar classes, paths and methods, an API wrapper would be able to abstract away specific request paths and make an efficient design for similar functions and API calls.

The repository thus contains a client for a Command Line Interface (CLI) and a wrapper which can be imported into python scripts.

### Setup and Dependencies 

All the required packages and dependencies can be found in the requirements.txt file. To install them, run the following command in your terminal: 

```python
pip3 install -r requirements.txt
```

### Directory Contents
1. **ogc_proccesses_api.py** - Python file containing the class object whose methods encapsulate the functions of the API. The class is well commented and contains docstrings for all methods. The methods and their behaviour is in accordance with the [OGC Processes API Documentation](https://docs.ogc.org/is/18-062r2/18-062r2.html#toc0). 
2. **print.py** - A very simple python script which makes a wrapper object and prints methods of the wrapper's class. Vary the method and parameters to verify different outputs on the terminal.
<br>
Run the file with the simple terminal command:

```
python print.py
```

3. **cli.py** - A command line interface built with the Click library in python. Using arguments, options and the help menu we can call various functions of the API with simple single line terminal commands. 
<br> 
The command format for using the CLI is:

```
python cli.py {base endpoint url} {method name} {variable parameters name {space} their value}
```

 Some example commands look like:

 ```
 python cli.py http://tb17.geolabs.fr:8101/ogc-api get_process_list --limit 1
 ```
 
```
python cli.py http://tb17.geolabs.fr:8101/ogc-api get_process_description --process_id OTB.SARBurstExtraction
```

 To enclose a dictionary as an input parameter for post_process_execution, please input it in the following form:
 
 ```
 python cli.py http://tb17.geolabs.fr:8101/ogc-api post_process_execution --process_inputs '{"key1":"value1", "key2":"value2" . . . . }'
 ```
 
The dictionary is inputted as a string which is converted to a python dictionary using the json.loads() function in the cli.py file.

