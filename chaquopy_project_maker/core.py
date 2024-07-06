import os.path
from typing import Literal, List, Dict, Any

from PyQt6.QtWidgets import QApplication
from cookiecutter.main import cookiecutter
from pyguiadapter.interact import ulogging, upopup

from chaquopy_project_maker import utils

DEFAULT_TEMPLATE_NAME = "HelloChaquopy"
REQUIRED_MIN_SDK = 21
RECOMMENDED_MIN_SDK = 24

tr = QApplication.tr
ulogging.enable_timestamp(True)


def get_user_configs(**configs) -> dict:
    user_configs = {}

    for key, value in configs.items():
        if value is not None:
            user_configs[key] = value
    return user_configs


def check_sdk_version(min_sdk: int, compile_sdk: int, target_sdk: int):
    if min_sdk <= 0:
        raise ValueError(tr("The min sdk version must be greater than 0"))
    if compile_sdk <= 0:
        raise ValueError(tr("The compile sdk version must be greater than 0"))
    if target_sdk <= 0:
        raise ValueError(tr("The target sdk version must be greater than 0"))
    if min_sdk < REQUIRED_MIN_SDK:
        raise ValueError(
            tr(
                f"The min sdk version is lower than Chaquopy’s requirement of {REQUIRED_MIN_SDK} "
            )
        )
    if min_sdk < RECOMMENDED_MIN_SDK:
        ulogging.warning(
            tr(
                f"The min sdk version is lower than the recommended minimal version ({RECOMMENDED_MIN_SDK}). "
                f"You may experience some problems in some circumstances. It is recommended to set the min sdk "
                f"version to {RECOMMENDED_MIN_SDK} or higher."
            )
        )


def make_project(
    project_template: str,
    output_dir: str,
    project_name: str,
    package_name: str,
    min_sdk: int,
    compile_sdk: int,
    target_sdk: int,
    abi_arm64_v8a: bool,
    abi_armeabi_v7a: bool,
    abi_x86: bool,
    abi_x86_64: bool,
    agp_version: str,
    kgp_version: str,
    chaquopy_version: str,
    gradle_wrapper_url: str,
    java_source_compatibility: str,
    java_target_compatibility: str,
    jvm_target: str,
    plugin_maven_repos: List[str],
    dependency_maven_repos: List[str],
    python_version: str,
    python_command: str,
    pyc_src: Literal["None", "False", "True"],
    pyc_pip: Literal["None", "False", "True"],
    pyc_stdlib: Literal["None", "False", "True"],
    python_source_set_name: str,
    python_source_set_dir: str,
    pip_index_url: str,
    pip_extra_index_urls: List[str],
    pip_requirements: List[str],
    static_proxy_classes: List[str],
    extract_packages: List[str],
    extra_configs: Dict[str, Any],
):
    project_template = project_template or ""
    project_template = project_template.strip()

    if not project_template:
        ulogging.warning(
            tr("Project template is not specified. The default template will be used.")
        )
        project_template = utils.get_builtin_template(DEFAULT_TEMPLATE_NAME)

    output_dir = output_dir or ""
    output_dir = output_dir.strip()
    if not output_dir:
        ulogging.warning(
            tr(
                "Output directory is not specified. The Project will be generated in the current directory."
            )
        )
        output_dir = "./"

    check_sdk_version(min_sdk, compile_sdk, target_sdk)

    python_source_set = None
    if python_source_set_name and python_source_set_dir:
        python_source_set = {
            "name": python_source_set_name,
            "dir": python_source_set_dir,
        }

    maven_repos = {
        "plugin": plugin_maven_repos or [],
        "dependency": dependency_maven_repos or [],
    }

    pip = {
        "index_url": pip_index_url or "",
        "extra_index_urls": pip_extra_index_urls or [],
        "requirements": pip_requirements or [],
    }

    static_proxy = {
        "classes": static_proxy_classes or [],
    }

    extract_packages = {
        "packages": extract_packages or [],
    }

    extra_configs = extra_configs or {}

    user_configs = get_user_configs(
        project_name=project_name,
        package_name=package_name,
        min_sdk=min_sdk,
        compile_sdk=compile_sdk,
        target_sdk=target_sdk,
        abi_arm64_v8a=abi_arm64_v8a,
        abi_armeabi_v7a=abi_armeabi_v7a,
        abi_x86=abi_x86,
        abi_x86_64=abi_x86_64,
        agp_version=agp_version,
        kgp_version=kgp_version,
        chaquopy_version=chaquopy_version,
        gradle_wrapper_url=gradle_wrapper_url,
        java_source_compatibility=java_source_compatibility,
        java_target_compatibility=java_target_compatibility,
        jvm_target=jvm_target,
        python_version=python_version,
        python_command=python_command,
        pyc_src=pyc_src,
        pyc_pip=pyc_pip,
        pyc_stdlib=pyc_stdlib,
        python_source_set=python_source_set,
        maven_repos=maven_repos,
        pip=pip,
        static_proxy=static_proxy,
        extract_packages=extract_packages,
        extra_configs=extra_configs,
    )
    ulogging.info(
        tr(
            f"Start to generate the project '{project_name}' in '{os.path.normpath(os.path.abspath(output_dir))}'"
        )
    )
    try:
        cookiecutter(
            project_template,
            output_dir=output_dir,
            no_input=True,
            extra_context=user_configs,
        )
    except BaseException as e:
        ulogging.critical(tr(f"Failed to generate the project!"))
        upopup.critical(
            message=tr(f"An error occurred! Failed to generate the project!\n") + f"{e}"
        )
    else:
        ulogging.info(tr("The project has been generated!"))
        upopup.information(
            message=tr(
                f"The project has been generated. You can open it in Android Studio now."
            ),
            title=tr("Success"),
        )
