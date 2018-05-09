import sys, os
from cx_Freeze import setup, Executable

os.environ["TCL_LIBRARY"] = "<path/to/your/python_directory>/tcl/tcl8.6"
os.environ["TK_LIBRARY"] = "<path/to/your/python_directory>/tcl/tk8.6"

base = None
include_files = [
    "./gedcom_xml_parser",
    "./gui_files",
    "<path/to/your/python_directory>/DLLs/tcl86t.dll",
    "<path/to/your/python_directory>/DLLs/tk86t.dll"
]

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="GedcomToXMLParser",
    version="1.0",
    description="GEDCOM To XML Parser",
    options={
        "build_exe": {
            "include_files": include_files
            }
    },
    executables=[
        Executable(
            "gui.py",
            base=base,
            targetName="GedcomToXML.exe",
            icon="./gui_files/assets/icon.ico"
        )
    ]
)
