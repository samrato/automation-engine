"""
Task: Kubernetes Pod Log Fetcher
Description: Fetches and saves the logs of a target pod.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="logs",
    category="kubernetes",
    description="Fetches logs from a specific pod and writes them to a file.",
)
def fetch_pod_logs(pod_name: str, namespace: str = "default", output_file: str = "pod.log"):
    """
    Student Task:
    1. Load Kubernetes configuration.
    2. Instantiate the CoreV1Api.
    3. Call the API read_namespaced_pod_log method for the given pod_name and namespace.
    4. Save the returned log string to the output_file.
    5. Return the path of the saved log file.
    """
    logger.info(f"Fetching logs from pod '{pod_name}' in namespace '{namespace}' -> {output_file}")
    raise NotImplementedError("Student Task: Implement fetch_pod_logs() in automations/kubernetes/logs.py")
