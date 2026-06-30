"""
Task: Kubernetes Pod Lister
Description: Retrieves and displays information about pods running in a namespace.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="pods",
    category="kubernetes",
    description="Lists all running pods and their statuses in a target namespace.",
)
def list_pods(namespace: str = "default"):
    """
    Student Task:
    1. Load Kubernetes configuration.
    2. Instantiate the CoreV1Api: `v1 = client.CoreV1Api()`.
    3. Retrieve the list of pods: `v1.list_namespaced_pod(namespace)`.
    4. Format and print a list containing pod names, status, and IPs.
    5. Return the pod details as a list of dicts.
    """
    logger.info(f"Listing pods in namespace: {namespace}")
    raise NotImplementedError("Student Task: Implement list_pods() in automations/kubernetes/pods.py")
