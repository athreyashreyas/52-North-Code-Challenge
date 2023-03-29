from ogc_processes_api import OGCAPIClient

# create the wrapper object for the OGC Processes API
wrapper_obj = OGCAPIClient("http://tb17.geolabs.fr:8101/ogc-api")

"""
call various methods of the wrapper object and the processes API, the various methods are:
1. get_conformance()
2. get_process_list(limit = 10)
3. get_process_description(process_id: str)
4. post_process_execution(process_id: str, inputs: dict)
5. get_job_list()
6. get_job_status_info(job_id: str)
7. get_job_results(job_id: str)
8. delete_job(job_id: str)
"""

# print the results of whatever you want to call, I have written a call to get_process_list(), feel free to call any of the above 
# processes

print(wrapper_obj.get_process_list(5))

