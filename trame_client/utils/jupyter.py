from IPython.core.getipython import get_ipython
from pathlib import Path


def get_kernel_id():
    kernel = get_ipython().kernel
    conf = kernel.config
    for key in conf:
        if "connection_file" in conf[key]:
            conn = Path(conf[key]["connection_file"])
            return conn.stem[7:]


__ALL__ = [
    "get_kernel_id",
]
