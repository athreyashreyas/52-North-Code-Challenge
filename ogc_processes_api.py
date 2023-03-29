import requests


class OGCAPIClient:

    # constructor for the landing page
    def __init__(self, base_url: str):
        """
        constructor gets initialised according to the OGC Processes API endpoint provided in the object declaration
        """
        self.base_url = base_url

    # Conformance Classes
    def get_conformance(self):
        """
        Delivers information about the list of conformance classes, errors and exceptions are handled appropriately
        :param: NONE
        :return: JSON format as per the API specification in
                 https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_conformance_classes
        """

        conformance_url = self.base_url + "/conformance"
        response = requests.get(conformance_url)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Error:", e)

        return response.json()

    # Process List
    def get_process_list(self, limit=10):
        """
        Delivers information about the list of processes. Errors and exceptions are handled appropriately
        
        :param: limit - integer value to limit the number of results returned
        
        :return: JSON format as per the API specification in
                 https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_process_list
        """

        # dictionary for parameter limit, only modified if limit is not default value and lies between 1 and 10000 as
        # per the API specification
        params_dict = {"limit": 10}

        if 1 <= limit <= 10000 and limit != 10:
            params_dict["limit"] = limit

        process_url = self.base_url + "/processes"
        response = requests.get(process_url, params=params_dict)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Error:", e)

        return response.json()

    # Process Description
    def get_process_description(self, process_id: str):
        """
        Delivers information about the process description, errors and exceptions are handled appropriately as per the
        OGC Processes API specification

        :arg:
            process_id (str): PID of the process whose description the user is querying. An invalid PID will result in
            an HTTP 404 error
        
        :return: JSON format as per the API specification in
                https://docs.ogc.org/is/18-062r2/18-062r2.html#sc_process_description
        """

        process_description_url = self.base_url + "/processes/" + process_id

        response = requests.get(process_description_url)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Error:", e)

        return response.json()

    # Process Execution (post request do later)
    def post_process_execution(self, process_id: str, inputs: dict):
        """
        Provides a function/endpoint to post a job request to the server to execute a process. Depending on the
        description of the process and the negotiated process execution mode, process execution may result in the
        creation of a job resource

        arg:
            process_id (str): string value of the process ID whose job the user wishes to create
            inputs (dict): dictionary of the input parameters for the process ID provided. Each value in the key:value
            pair can be:
                            a simple literal value,
                            an array,
                            a qualified value,
                            a binary value,
                            or a bounding box

        return:
            int: the HTTP response code for the post request. Generally, 200 is a successful post request, 400 is a bad
            request, 500 is an internal server error. Other response codes can be looked up online for more information
            on the status of the post request
        """
        process_execution_url = self.base_url + "/processes/" + process_id + "/execution"

        response = requests.get(process_execution_url, data=dict)

        return response.status_code

    # Job List
    def get_job_list(self):
        """
        Delivers information about the list of job ids and status info, links to results or exceptions, which are
        handled appropriately
        
        :param: NONE
        :return: JSON format as per the API specification in https://docs.ogc.org/is/18-062r2/18-062r2.html
        """

        job_list_url = self.base_url + "/jobs"

        response = requests.get(job_list_url)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Error:", e)

        return response.json()

    # Job Status Info
    def get_job_status_info(self, job_id: str):
        """
        Delivers information about the job's status, links to results or exceptions, which are handled appropriately
  
        :param: NONE
        :return: JSON format as per the API specification in https://docs.ogc.org/is/18-062r2/18-062r2.html
        """

        job_status_info_url = self.base_url + "/jobs/" + job_id

        response = requests.get(job_status_info_url)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Error:", e)

        return response.json()

    # Job Results
    def get_job_results(self, job_id: str):
        """
        Delivers information about the job's results, links to results or exceptions, which are handled appropriately
  
        :param: NONE
        :return: JSON format as per the API specification in https://docs.ogc.org/is/18-062r2/18-062r2.html
        """

        job_results_url = self.base_url + "/jobs/" + job_id + "/results"

        response = requests.get(job_results_url)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Error:", e)
        # documentation says that the response attribute has diff media types? how to handle this? I am simply returning
        # json values
        return response.json()

    # Job Delete

    def delete_job(self, job_id: str):
        """
        Deletes the job with the given job ID as per the API specification in
        https://docs.ogc.org/is/18-062r2/18-062r2.html#Dismiss. If the job does not exist, the server shall return a 404
        error.
        As such, there are no required parameters or headers required for the delete operation
        
        :param: job_id (str): string value of the job ID to be deleted
        :return: HTTP status code of the DELETE Request. 200 is a successful delete request
        """
        delete_job_url = self.base_url + "/jobs/" + job_id

        response = requests.delete(delete_job_url)

        return response.json()
