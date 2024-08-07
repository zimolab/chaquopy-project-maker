from PyQt6.QtWidgets import QApplication

from function2widgets import (
    CheckBox,
    ComboBoxEdit,
    ComboBoxEditArgs,
    ComboBox,
    ComboBoxArgs,
    ListEditor,
    ListEditorArgs,
    DictEditor,
    DictEditorArgs,
)
from function2widgets import CheckBoxArgs
from function2widgets import DirPathEdit
from function2widgets import DirPathEditArgs
from function2widgets import IntLineEdit
from function2widgets import IntLineEditArgs
from function2widgets import LineEdit
from function2widgets import LineEditArgs
from function2widgets import FilePathEdit, FilePathEditArgs

tr = QApplication.tr


DEFAULT_PROJECT_NAME = "Hello Chaquopy"
DEFAULT_PACKAGE_NAME = (
    f"com.example.{DEFAULT_PROJECT_NAME.replace(' ', '').lower()}".strip()
)
DEFAULT_MIN_SDK = 24
DEFAULT_COMPILE_SDK = 34
DEFAULT_TARGET_SDK = 34
DEFAULT_AGP_VERSION = "8.3.1"
DEFAULT_KGP_VERSION = "1.9.23"
DEFAULT_CHAQUOPY_VERSION = "15.0.1"
DEFAULT_ADD_ALIYUN_REPOSITORIES = False


GRADLE_WRAPPER_URLS = [
    "https://services.gradle.org/distributions/gradle-8.4-all.zip",
    "https://mirrors.cloud.tencent.com/gradle/gradle-8.4-all.zip",
]

JAVA_VERSIONS = [
    "VERSION_1_8",
    "VERSION_1_9",
    "VERSION_1_10",
    "VERSION_11",
    "VERSION_12",
    "VERSION_13",
    "VERSION_14",
    "VERSION_15",
    "VERSION_16",
    "VERSION_17",
    "VERSION_18",
    "VERSION_19",
    "VERSION_20",
    "VERSION_21",
    "VERSION_22",
    "VERSION_23",
    "VERSION_24",
    "VERSION_25",
]

JVM_TARGETS = [v.replace("VERSION_", "").replace("_", ".") for v in JAVA_VERSIONS]

DEFAULT_JVM_TARGET_VERSION = JAVA_VERSIONS[0].replace("VERSION_", "").replace("_", ".")
DEFAULT_PYTHON_VERSION = "3.8"

PYC_OPTIONS = [
    "Auto",
    "False",
    "True",
]

CONFIGS = {
    "project_template": {
        "widget_class": DirPathEdit.__name__,
        "widget_args": DirPathEditArgs(
            parameter_name="AS-IS",
            label=tr("Project Template Path"),
            description=tr(
                "Select project template directory or you can input the path of a template (for example, a git repo,"
                "a zip file, and so on). If you want to use the "
                "<a href='https://github.com/zimolab/HelloChaquopy'>default template</a>, you can leave it blank."
            ),
            default="",
            default_value_description=tr("Use the default template"),
            hide_default_value_widget=False,
        ),
    },
    "output_dir": {
        "widget_class": DirPathEdit.__name__,
        "widget_args": DirPathEditArgs(
            parameter_name="AS-IS",
            label=tr("Output Directory"),
            description=tr(
                "Select the output directory. "
                "If you leave it blank, the project will be created in the current directory."
            ),
            default="",
            hide_default_value_widget=False,
            default_value_description=tr("Use the current directory"),
        ),
    },
    "project_name": {
        "widget_class": LineEdit.__name__,
        "widget_args": LineEditArgs(
            parameter_name="AS-IS",
            label=tr("Project Name"),
            default=DEFAULT_PROJECT_NAME,
        ),
    },
    "package_name": {
        "widget_class": LineEdit.__name__,
        "widget_args": LineEditArgs(
            parameter_name="AS-IS",
            label=tr("Package Name"),
            default=DEFAULT_PACKAGE_NAME,
        ),
    },
    "min_sdk": {
        "widget_class": IntLineEdit.__name__,
        "widget_args": IntLineEditArgs(
            parameter_name="AS-IS",
            label=tr("Min Sdk Version"),
            default=DEFAULT_MIN_SDK,
        ),
    },
    "compile_sdk": {
        "widget_class": IntLineEdit.__name__,
        "widget_args": IntLineEditArgs(
            parameter_name="AS-IS",
            label=tr("Compile Sdk Version"),
            default=DEFAULT_COMPILE_SDK,
        ),
    },
    "target_sdk": {
        "widget_class": IntLineEdit.__name__,
        "widget_args": IntLineEditArgs(
            parameter_name="AS-IS",
            label=tr("Target Sdk Version"),
            default=DEFAULT_COMPILE_SDK,
        ),
    },
    "abi_arm64_v8a": {
        "widget_class": CheckBox.__name__,
        "widget_args": CheckBoxArgs(
            parameter_name="AS-IS",
            label="Add arm64-v8a ABI",
            description="Add arm64-v8a ABI filter",
            default=True,
            text=tr("Enabled"),
        ),
    },
    "abi_armeabi_v7a": {
        "widget_class": CheckBox.__name__,
        "widget_args": CheckBoxArgs(
            parameter_name="AS-IS",
            label="Add armeabi-v7a ABI",
            description="Add armeabi-v7a ABI filter",
            default=True,
            text=tr("Enabled"),
        ),
    },
    "abi_x86": {
        "widget_class": CheckBox.__name__,
        "widget_args": CheckBoxArgs(
            parameter_name="AS-IS",
            label="Add x86 ABI",
            description="Add x86 ABI filter",
            default=True,
            text=tr("Enabled"),
        ),
    },
    "abi_x86_64": {
        "widget_class": CheckBox.__name__,
        "widget_args": CheckBoxArgs(
            parameter_name="AS-IS",
            label="Add x86_64 ABI",
            description="Add x86_64 ABI filter",
            default=True,
            text=tr("Enabled"),
        ),
    },
    "agp_version": {
        "widget_class": LineEdit.__name__,
        "widget_args": LineEditArgs(
            parameter_name="AS-IS",
            label=tr("Android Gradle Plugin (AGP)"),
            default=DEFAULT_AGP_VERSION,
        ),
    },
    "kgp_version": {
        "widget_class": LineEdit.__name__,
        "widget_args": LineEditArgs(
            parameter_name="AS-IS",
            label=tr("Kotlin Gradle Plugin (KGP)"),
            default=DEFAULT_KGP_VERSION,
        ),
    },
    "chaquopy_version": {
        "widget_class": LineEdit.__name__,
        "widget_args": LineEditArgs(
            parameter_name="AS-IS",
            label=tr("Chaquopy Version"),
            default=DEFAULT_CHAQUOPY_VERSION,
        ),
    },
    "gradle_wrapper_url": {
        "widget_class": ComboBoxEdit.__name__,
        "widget_args": ComboBoxEditArgs(
            parameter_name="AS-IS",
            label=tr("Gradle Wrapper URL"),
            items=GRADLE_WRAPPER_URLS,
            default=GRADLE_WRAPPER_URLS[0],
        ),
    },
    "java_source_compatibility": {
        "widget_class": ComboBoxEdit.__name__,
        "widget_args": ComboBoxEditArgs(
            parameter_name="AS-IS",
            label=tr("Java Source Compatibility"),
            items=JAVA_VERSIONS,
            default=JAVA_VERSIONS[0],
        ),
    },
    "java_target_compatibility": {
        "widget_class": ComboBoxEdit.__name__,
        "widget_args": ComboBoxEditArgs(
            parameter_name="AS-IS",
            label=tr("Java Target Compatibility"),
            items=JAVA_VERSIONS,
            default=JAVA_VERSIONS[0],
        ),
    },
    "jvm_target": {
        "widget_class": ComboBoxEdit.__name__,
        "widget_args": ComboBoxEditArgs(
            parameter_name="AS-IS",
            label=tr("JVM Target"),
            items=JVM_TARGETS,
            default=JVM_TARGETS[0],
        ),
    },
    "python_version": {
        "widget_class": LineEdit.__name__,
        "widget_args": LineEditArgs(
            parameter_name="AS-IS",
            label=tr("Python Version"),
            default=DEFAULT_PYTHON_VERSION,
        ),
    },
    "python_command": {
        "widget_class": FilePathEdit.__name__,
        "widget_args": FilePathEditArgs(
            parameter_name="AS-IS",
            label=tr("Python Command"),
            description=tr(
                "Input the python command or select the python executable which will be used by Chaquopy plugin to "
                "compile your python code into bytecode (*.pyc) during the build time."
            ),
            default="",
        ),
    },
    "pyc_src": {
        "widget_class": ComboBox.__name__,
        "widget_args": ComboBoxArgs(
            parameter_name="AS-IS",
            label=tr("Compile src (pyc)"),
            items=PYC_OPTIONS,
            default=PYC_OPTIONS[0],
        ),
    },
    "pyc_pip": {
        "widget_class": ComboBox.__name__,
        "widget_args": ComboBoxArgs(
            parameter_name="AS-IS",
            label=tr("Compile pip (pyc)"),
            items=PYC_OPTIONS,
            default=PYC_OPTIONS[0],
        ),
    },
    "pyc_stdlib": {
        "widget_class": ComboBox.__name__,
        "widget_args": ComboBoxArgs(
            parameter_name="AS-IS",
            label=tr("Compile stdlib (pyc)"),
            items=PYC_OPTIONS,
            default=PYC_OPTIONS[0],
        ),
    },
    "python_source_set_name": {
        "widget_class": LineEdit.__name__,
        "widget_args": LineEditArgs(
            parameter_name="AS-IS",
            label=tr("Extra Python Source Set"),
            default_value_description=tr("No extra python source set"),
            default=None,
        ),
    },
    "python_source_set_dir": {
        "widget_class": LineEdit.__name__,
        "widget_args": LineEditArgs(
            parameter_name="AS-IS",
            label=tr("Extra Python Source Set Directory"),
            description=tr("Input the extra python source set directory"),
            default_value_description=tr("No extra python source set"),
            default=None,
        ),
    },
    "pip_index_url": {
        "widget_class": LineEdit.__name__,
        "widget_args": LineEditArgs(
            parameter_name="AS-IS",
            label=tr("Pip Index URL"),
            description=tr("Set the pip index url"),
            default_value_description=tr("Use default pip index url"),
            default="",
            hide_default_value_widget=False,
        ),
    },
    "pip_extra_index_urls": {
        "widget_class": ListEditor.__name__,
        "widget_args": ListEditorArgs(
            parameter_name="AS-IS",
            label=tr("Extra Pip Index URLS"),
            description=tr("Add extra pip index urls"),
            display_current_value=False,
            default_value_description=tr("No extra pip index urls"),
            default=[],
            hide_default_value_widget=False,
            window_title=tr("Extra pip Index URLS"),
        ),
    },
    "pip_requirements": {
        "widget_class": ListEditor.__name__,
        "widget_args": ListEditorArgs(
            parameter_name="AS-IS",
            label=tr("Pip Requirements"),
            description=tr("Add pip requirements"),
            display_current_value=False,
            default_value_description=tr("No python dependencies"),
            default=[],
            hide_default_value_widget=False,
            window_title=tr("Python Dependencies"),
        ),
    },
    "static_proxy_classes": {
        "widget_class": ListEditor.__name__,
        "widget_args": ListEditorArgs(
            parameter_name="AS-IS",
            label=tr("Static Proxy"),
            description=tr("Add python static proxy classes."),
            display_current_value=False,
            default_value_description=tr("No python static proxy classes"),
            default=None,
            window_title=tr("Python Static Proxy Classes"),
        ),
    },
    "extract_packages": {
        "widget_class": ListEditor.__name__,
        "widget_args": ListEditorArgs(
            parameter_name="AS-IS",
            label=tr("Extract Packages"),
            description=tr("Add python packages will be extracted as separate files."),
            display_current_value=False,
            default_value_description=tr("No extract packages"),
            default=None,
            hide_default_value_widget=False,
            window_title=tr("Extract Packages"),
        ),
    },
    "plugin_maven_repos": {
        "widget_class": ListEditor.__name__,
        "widget_args": ListEditorArgs(
            parameter_name="AS-IS",
            label=tr("Extra Plugin Maven Repositories"),
            description=tr("Add extra plugin maven repository urls"),
            display_current_value=False,
            default_value_description=tr("No extra plugin maven repositories"),
            default=[],
            hide_default_value_widget=False,
            window_title=tr("Extra Plugin Maven Repositories"),
        ),
    },
    "dependency_maven_repos": {
        "widget_class": ListEditor.__name__,
        "widget_args": ListEditorArgs(
            parameter_name="AS-IS",
            label=tr("Extra Dependency Maven Repositories"),
            description=tr("Add extra dependency maven repositories"),
            display_current_value=False,
            default_value_description=tr("No extra dependency maven repositories"),
            default=[],
            hide_default_value_widget=False,
            window_title=tr("Extra Dependency Maven Repositories"),
        ),
    },
    "extra_configs": {
        "widget_class": DictEditor.__name__,
        "widget_args": DictEditorArgs(
            parameter_name="AS-IS",
            label=tr("Extra Configs"),
            description=tr(
                "Add extra configs can be accessed in cookiecutter template"
            ),
            display_current_value=False,
            default_value_description=tr("No extra configs"),
            default=None,
            hide_default_value_widget=False,
            window_title=tr("Extra Configs"),
        ),
    },
}
