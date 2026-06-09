from pathlib import Path
import logging
import shutil
from dataclasses import dataclass
from urllib.parse import urlparse
from .utils.web_module import file_digest

from .module import (
    USER_PROVIDED_SCRIPTS_DIR_PATH,
    USER_PROVIDED_SCRIPTS_SERVE_URL_PREFIX,
    USER_PROVIDED_UMD_SCRIPTS_DIR_PATH,
    USER_PROVIDED_ES_SCRIPTS_DIR_PATH,
)

logger = logging.getLogger(__name__)


def clean_user_provided_scripts(folder: Path):
    files_to_keep = {"__init__.py", ".gitignore"}

    for item in folder.iterdir():
        if item.is_file() and item.name not in files_to_keep:
            item.unlink()

        if item.is_dir() and item.name not in files_to_keep:
            clean_user_provided_scripts(item)


@dataclass
class UserDefinedFunction:
    name: str
    script: "ExternalScript"


@dataclass
class ExternalScript:
    name: str
    script_original_file_path: Path | str
    function_names: list[str]
    is_umd_module: bool
    umd_global_var_name: str | None
    namespaced_script_file_path: Path | None = None

    def __post_init__(self):
        if isinstance(self.script_original_file_path, str):
            parsed = urlparse(self.script_original_file_path)

            if not all([parsed.scheme, parsed.netloc]):
                msg = f"String must be a valid URL. Received: '{self.script_original_file_path}'"
                raise ValueError(msg)
        else:
            dest_base_path = (
                USER_PROVIDED_UMD_SCRIPTS_DIR_PATH
                if self.is_umd_module
                else USER_PROVIDED_ES_SCRIPTS_DIR_PATH
            )

            script_file_hash = file_digest(self.script_original_file_path)

            self.namespaced_script_file_path = Path(
                f"{script_file_hash}_{self.script_original_file_path.name}"
            )

            shutil.copy2(
                self.script_original_file_path,
                dest_base_path / self.namespaced_script_file_path,
            )

    @property
    def module_path(self) -> str:
        if self.is_umd_module:
            return self.umd_global_var_name

        if isinstance(self.script_original_file_path, str):
            # We have a URL, let's return it as-is
            return self.script_original_file_path

        url_prefix = USER_PROVIDED_SCRIPTS_SERVE_URL_PREFIX
        es_module_prefix = USER_PROVIDED_ES_SCRIPTS_DIR_PATH.name

        return (
            url_prefix / es_module_prefix / self.namespaced_script_file_path
        ).as_posix()

    @property
    def module_type(self) -> str:
        return "umd" if self.is_umd_module else "es"

    def function(self, name: str | None = None) -> UserDefinedFunction:
        if not name:
            try:
                assert len(self.function_names) == 1
            except AssertionError:
                msg = """
                    Ambiguate call to function() without an explicit name.
                    Explicitly specify the function name using the name parameter.
                """
                raise ValueError(msg)

            name = self.function_names[0]

        return UserDefinedFunction(name=name, script=self)


EXTERNAL_SCRIPTS_MAP = {}


def get_external_script_from_name(name: str) -> ExternalScript:
    try:
        return EXTERNAL_SCRIPTS_MAP[name]
    except KeyError as e:
        msg = f"No external script associated with name {name}"
        raise ValueError(msg) from e


def register_user_provided_script(
    script_file_path: Path,
    *,
    function_names: list[str],
    name: str,
    umd: bool = False,
    umd_global_var_name: str | None = None,
) -> ExternalScript:
    if name in EXTERNAL_SCRIPTS_MAP:
        logger.warning("overwriting already registered script %s", name)

    if not EXTERNAL_SCRIPTS_MAP:
        clean_user_provided_scripts(USER_PROVIDED_SCRIPTS_DIR_PATH)

    EXTERNAL_SCRIPTS_MAP[name] = ExternalScript(
        name,
        script_file_path,
        function_names,
        is_umd_module=umd,
        umd_global_var_name=umd_global_var_name,
    )
    return EXTERNAL_SCRIPTS_MAP[name]
