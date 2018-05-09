"""gui init file"""

import sys
sys.path.append('./gui_files/')
from gui_files import gedcom_parser

if __name__ == '__main__':
    gedcom_parser.vp_start_gui()