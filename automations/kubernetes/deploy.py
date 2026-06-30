"""
Task: Kubernetes Deployment Loader
Description: Deploys applications to Kubernetes from manifest YAML files.
"""

from core.logger import logger
from engine import register_task


@register_task(
    name="deploy",
    category="kubernetes",
    description="Deploys Kubernetes resources from a YAML manifest file.",
)
def deploy_manifest(manifest_path: str, namespace: str = "default"):
    """
    Student Task:
    1. Import `kubernetes.client` and `kubernetes.config` and `yaml`.
    2. Load kube-config (either in-cluster config or local config via `config.load_kube_config()`).
    3. Open the manifest YAML file and parse it.
    4. Call the appropriate Kubernetes API depending on the resource type (e.g. Deployment -> AppsV1Api, Service -> CoreV1Api).
    5. Log the resource creation/update status.
    """
    logger.info(f"Applying manifest {manifest_path} to namespace: {namespace}")
    raise NotImplementedError("Student Task: Implement deploy_manifest() in automations/kubernetes/deploy.py")
