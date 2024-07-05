from PyQt6.QtWidgets import QApplication
from pyguiadapter import GUIAdapter, DocumentFormat
from pyguiadapter.ui import ActionItem, ExecutionContext
from pyguiadapter.interact import upopup


from chaquopy_project_maker.core import make_project
from chaquopy_project_maker.configs import CONFIGS

tr = QApplication.tr

APP_NAME = tr("Chaquopy Project Maker")
APP_DOCUMENTATION = """This tool can help you quickly create a new Chaquopy-based Android Studio project.

Chaquopy is a powerful library which provides everything you need to include Python components in an Android app, 
including:
    
1.Full integration with Android Studio’s standard Gradle build system.

2.Simple APIs for calling Python code from Java/Kotlin, and vice versa.

3.A wide range of third-party Python packages, including SciPy, OpenCV, TensorFlow and many more.

----

Check [Chaquopy website](https://chaquo.com/chaquopy/) and [documentation](https://chaquo.com/chaquopy/doc/current/)
for more information.

"""

EXTRA_PLUGIN_MAVEN_REPOS_ALIYUN = [
    "https://maven.aliyun.com/repository/google",
    "https://maven.aliyun.com/repository/central",
    "https://maven.aliyun.com/repository/gradle-plugin",
]

EXTRA_DEP_MAVEN_REPOS_ALIYUN = [
    "https://maven.aliyun.com/repository/google",
    "https://maven.aliyun.com/repository/central",
]


def on_add_aliyun_repositories(ctx: ExecutionContext):
    try:
        # add aliyun's repos to extra_plugin_maven_repositories and extra_dependency_maven_repositories
        extra_plugin_maven_repositories = (
            ctx.get_param_value("extra_plugin_maven_repositories") or []
        )
        extra_dependency_maven_repositories = (
            ctx.get_param_value("extra_dependency_maven_repositories") or []
        )
        for repo in EXTRA_PLUGIN_MAVEN_REPOS_ALIYUN:
            if repo not in extra_plugin_maven_repositories:
                extra_plugin_maven_repositories.append(repo)
        for repo in EXTRA_DEP_MAVEN_REPOS_ALIYUN:
            if repo not in extra_dependency_maven_repositories:
                extra_dependency_maven_repositories.append(repo)
        ctx.set_param_value(
            "extra_plugin_maven_repositories", extra_plugin_maven_repositories
        )
        ctx.set_param_value(
            "extra_dependency_maven_repositories", extra_dependency_maven_repositories
        )
    except BaseException as e:
        print(e)
        ctx.logging_fatal(tr(f"Failed to add aliyun repositories!"))
        ctx.logging_fatal(f"{e}")
        upopup.critical(tr("Failed to add aliyun repositories!\n"), title=tr("Error"))
        return
    else:
        msg = tr(
            "Aliyun repositories has been added to extra_plugin_maven_repositories and "
            "extra_dependency_maven_repositories!"
        )
        ctx.logging_info(msg)
        upopup.information(msg, title=tr("Success"))


MENUS = {
    tr("File"): {
        "add_aliyun_repositories": ActionItem(
            text=tr("Add Aliyun Repositories"),
            callback=on_add_aliyun_repositories,
        ),
        "about": ActionItem(
            text=tr("About"),
            callback=lambda ctx: upopup.show_about_popup(
                app_name=APP_NAME,
                app_description=tr(
                    "Chaquopy Project Maker is a GUI tool to help you create a Chaquopy-integrated Android app project"
                    "easily. It can save you a lot of time from the repeating and tedious work."
                ),
                app_copyright=tr("copyright © zimolab. All right reserved"),
                app_fields={
                    tr("License"): "GPL",
                    tr("Version"): "0.0.1",
                    tr("Author"): "zimolab",
                    tr(
                        "GitHub"
                    ): "<a href='https://github.com/zimolab/chaquopy-project-maker'>chaquopy-project-maker</a>",
                },
            ),
        ),
    },
}


def setup(adapter: GUIAdapter) -> GUIAdapter:
    adapter.execution_window_config.title = APP_NAME
    adapter.execution_window_config.execute_button_text = tr("Make Project")
    adapter.execution_window_config.print_func_start_msg = False
    adapter.execution_window_config.print_func_finish_msg = False
    adapter.execution_window_config.print_func_result = False
    adapter.execution_window_config.show_func_error_dialog = True
    adapter.execution_window_config.show_func_result_dialog = False
    adapter.execution_window_config.func_error_msg = "{}"
    adapter.execution_window_config.func_error_dialog_title = tr("Error")
    adapter.execution_window_config.enable_menubar_actions = True

    return adapter


def main():
    gui_adapter = setup(GUIAdapter())
    gui_adapter.add(
        make_project,
        display_document=APP_DOCUMENTATION,
        document_format=DocumentFormat.MARKDOWN,
        widget_configs=CONFIGS,
        menus=MENUS,
    )
    gui_adapter.run()


if __name__ == "__main__":
    main()
