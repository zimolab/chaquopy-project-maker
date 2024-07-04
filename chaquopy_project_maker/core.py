from typing import Literal, List

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
    extra_plugin_maven_repositories: List[str],
    extra_dependency_maven_repositories: List[str],
    python_version: str,
    python_command: str,
    pyc_src: Literal["None", "False", "True"],
    pyc_pip: Literal["None", "False", "True"],
    pyc_stdlib: Literal["None", "False", "True"],
    python_source_set_name: str,
    python_source_set_dir: str,
    python_dependencies: List[str],
    pip_extra_index_urls: List[str],
    python_static_proxies: List[str],
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
    extra_plugin_maven_repositories = extra_plugin_maven_repositories or None
    extra_dependency_maven_repositories = extra_dependency_maven_repositories or None

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
        _extra_plugin_maven_repositories=extra_plugin_maven_repositories,
        _extra_dependency_maven_repositories=extra_dependency_maven_repositories,
        python_version=python_version,
        python_command=python_command,
        pyc_src=pyc_src,
        pyc_pip=pyc_pip,
        pyc_stdlib=pyc_stdlib,
        python_source_set=python_source_set,
        _python_dependencies=python_dependencies,
        _pip_extra_index_urls=pip_extra_index_urls,
        _python_static_proxies=python_static_proxies,
    )
    print(user_configs)

    cookiecutter(
        project_template,
        no_input=True,
        output_dir=output_dir,
        extra_context=user_configs,
    )
