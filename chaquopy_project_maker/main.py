from PyQt6.QtWidgets import QApplication
from pyguiadapter import GUIAdapter, DocumentFormat

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

    return adapter


def main():
    gui_adapter = setup(GUIAdapter())
    gui_adapter.add(
        make_project,
        display_document=APP_DOCUMENTATION,
        document_format=DocumentFormat.MARKDOWN,
        widget_configs=CONFIGS,
    )
    gui_adapter.run()


if __name__ == "__main__":
    main()
