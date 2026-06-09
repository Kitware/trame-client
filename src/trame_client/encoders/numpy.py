import json

import numpy as np

np_version = tuple(map(int, np.__version__.split(".")))
if np_version < (2, 0, 0):
    NP_FLOATS = (np.float_, np.float16, np.float32, np.float64)
    NP_COMPLEX = (np.complex_, np.complex64, np.complex128)
else:
    NP_FLOATS = (np.float16, np.float32, np.float64)
    NP_COMPLEX = (np.complex64, np.complex128)


class NumpyEncoder(json.JSONEncoder):
    """Custom encoder for numpy data types"""

    def default(self, obj):
        if isinstance(
            obj,
            (
                np.int_,
                np.intc,
                np.intp,
                np.int8,
                np.int16,
                np.int32,
                np.int64,
                np.uint8,
                np.uint16,
                np.uint32,
                np.uint64,
            ),
        ):
            return int(obj)

        elif isinstance(obj, NP_FLOATS):
            return float(obj)

        elif isinstance(obj, NP_COMPLEX):
            return {"real": obj.real, "imag": obj.imag}

        elif isinstance(obj, (np.ndarray,)):
            return obj.tolist()

        elif isinstance(obj, (np.bool_)):
            return bool(obj)

        elif isinstance(obj, (np.void)):
            return None

        return json.JSONEncoder.default(self, obj)


def encode(data_structure):
    return json.loads(json.dumps(data_structure, cls=NumpyEncoder))
