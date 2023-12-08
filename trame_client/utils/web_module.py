import hashlib
from pathlib import Path


def file_digest(file_path):
    h = hashlib.sha256()
    b = bytearray(128 * 1024)
    mv = memoryview(b)
    with open(file_path, "rb", buffering=0) as f:
        while n := f.readinto(mv):
            h.update(mv[:n])
    return h.hexdigest()


def file_with_digest(file_path, digest=None, digest_size=40):
    file_path = Path(file_path)

    if digest is None:
        digest = file_digest(file_path)

    if len(digest) > digest_size:
        digest = digest[:digest_size]

    # Create file with digest name
    output_file = file_path.with_name(f"{file_path.stem}-{digest}{file_path.suffix}")
    output_file.write_bytes(file_path.read_bytes())

    return output_file


def is_relative_to(path, *other_paths):
    # Convert the input path and the base path into absolute paths
    abs_path = path.resolve()
    abs_other_paths = [Path(other).resolve() for other in other_paths]

    # Check if the parts of the base paths are the beginning of the input path's parts
    return all(
        abs_path.parts[: len(base.parts)] == base.parts for base in abs_other_paths
    )


class WebModule:
    def __init__(self, vue_use=None, digest_size=6):
        self._digest_size = digest_size
        self._serving_entries = []
        self._serve = {}
        self._vue_use = []
        self._styles = []
        self._scripts = []

        if vue_use is not None:
            self._vue_use.append(vue_use)

    def _add_file(self, file_path):
        file_path = Path(file_path).resolve()
        if not file_path.exists():
            raise ValueError(f"File {file_path} does not exist")

        for entry in self._serving_entries:
            fs_path, www_path = entry
            if is_relative_to(file_path, fs_path):
                if self._digest_size > 0:
                    file_path = file_with_digest(
                        file_path, digest_size=self._digest_size
                    )

                r_path = file_path.relative_to(fs_path)
                return f"{www_path}/{r_path}"

        raise ValueError(f"No parent found for {file_path}")

    def serve_directory(self, directory_to_serve, www_base_name):
        fs_path = Path(directory_to_serve).resolve()
        if not fs_path.exists():
            raise ValueError(
                f"Directory {fs_path} does not exist - Won't be able to serve it"
            )
        if www_base_name in self._serve:
            raise ValueError(
                f"Entry for {www_base_name} is already set for {self._serve[www_base_name]} and want to override with {fs_path}"
            )

        self._serving_entries.append((fs_path, www_base_name))
        self._serve[www_base_name] = str(fs_path)

    def add_script_file(self, file_path):
        self._scripts.append(self._add_file(file_path))

    def add_style_file(self, file_path):
        self._styles.append(self._add_file(file_path))

    def add_vue_use(self, vue_use):
        self._vue_use.append(vue_use)

    @property
    def module(self):
        return dict(
            serve=self._serve,
            scripts=self._scripts,
            styles=self._styles,
            vue_use=self._vue_use,
        )
