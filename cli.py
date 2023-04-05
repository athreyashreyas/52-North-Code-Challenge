import click
import json 

from ogc_processes_api import OGCAPIClient


# @click.echo("Welcome to the OGC Processes API Wrapper!")
@click.command()
# ask for a base url whose default value is http://tb17.geolabs.fr:8101/ogc-api
@click.argument("base_url", default="http://tb17.geolabs.fr:8101/ogc-api", type=str, nargs=1)
# name of the function to be called
@click.argument("function", default="get_process_list", type=str, nargs=1)
@click.option("--process_id", type=str, default="", help="Process ID for OGC Process whose API endpoint is queried")
@click.option("--job_id", type=str, default="", help="Job ID for the job whose API endpoint is queried")
@click.option("--limit", type=int, default=10, help="Limit for the number of jobs to be returned")
@click.option("--process_inputs", type = str, default = "{}", help = "Process inputs for the process execution")

def fetch(base_url, process_id, job_id, limit, function, process_inputs):
    """
    A CLI program which acts as a medium for API calls for the OGC Processes API, the functions available are:
        1. get_conformance()
        2. get_process_list(limit = 10)
        3. get_process_description(process_id: str)
        4. post_process_execution(process_id: str, process_inputs: dict)
        5. get_job_list()
        6. get_job_status_info(job_id: str)
        7. get_job_results(job_id: str)
        8. delete_job(job_id: str)
    """
    wrapper_obj = OGCAPIClient(base_url)
    if function == "get_conformance":
        click.echo(wrapper_obj.get_conformance())
    elif function == "get_process_list":
        click.echo(wrapper_obj.get_process_list(limit))
    elif function == "get_process_description":
        click.echo(wrapper_obj.get_process_description(process_id))
    elif function == "post_process_execution":
        input_dict = json.loads(process_inputs)
        click.echo(wrapper_obj.post_process_execution(process_id, input_dict))
    elif function == "get_job_list":
        click.echo(wrapper_obj.get_job_list())
    elif function == "get_job_status_info":
        click.echo(wrapper_obj.get_job_status_info(job_id))
    elif function == "get_job_results":
        click.echo(wrapper_obj.get_job_results(job_id))
    elif function == "delete_job":
        click.echo(wrapper_obj.delete_job(job_id))
    else:
        print("Invalid function name. Please try again.")


if __name__ == "__main__":
    fetch()
