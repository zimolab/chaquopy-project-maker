import os.path
import platform
from importlib import resources


def get_templates_dir() -> str:
    with resources.path("chaquopy_project_maker", "templates") as res_dir:
        return os.path.abspath(os.path.normpath(str(res_dir)))


def get_builtin_template(template_name: str) -> str:
    return os.path.abspath(
        os.path.normpath(os.path.join(get_templates_dir(), template_name))
    )
