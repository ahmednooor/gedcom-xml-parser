# gedcom-xml-parser
GEDCOM -> XML Parser/Convertor

- Aconex GEDCOM Parser Challange
- Made in Python
- Tkinter used for GUI

# How to Run

> You will need to have `python 3.5+` and `tkinter` installed on your system before running.

### GUI Version

1. Open Terminal/Cmd in this directory
2. Type `python gui.py`

### Console Version

1. Open Terminal/Cmd in this directory
2. Type `python cli.py`
3. Enter the path to GEDCOM `.ged` file to parse. Like this, `folder/input.ged`
4. Enter the path to XML `.xml` file to save xml. Like this, `folder/output.xml`
> Use `.ged` files from `data_files` directory for testing.

# How to use it on your own

* Copy `gedcom_xml_parser` directory in to the directory where your python file is.
* Below is the code example of usage,
``` python
from gedcom_xml_parser.gedcom_xml_parser import GedcomXMLParser

def main():
    '''GedcomXMLParser usage'''
    gedcom_text = r'''0 @I1@ INDI
    1 NAME Jamis Gordon /Buck/
    2 SURN Buck
    2 GIVN Jamis Gordon
    1 SEX M'''

    parser = GedcomXMLParser(gedcom_text)
    xml_text_pretty = parser.get_parsed_data()
    xml_text_minified = parser.get_parsed_data_minified()
    
    print('# --- Parsed XML (Pretty):')
    print(xml_text_pretty)
    # --- OUTPUT:
    # <?xml version="1.0" ?>
    # <GEDCOM>
    #         <INDI id="@I1@">
    #                 <NAME value="Jamis Gordon /Buck/">
    #                         <SURN>Buck</SURN>
    #                         <GIVN>Jamis Gordon</GIVN>
    #                 </NAME>
    #                 <SEX>M</SEX>
    #         </INDI>
    # </GEDCOM>
    
    print()
    print('# --- Parsed XML (Minified):')
    print(xml_text_minified)
    # --- OUTPUT:
    # <?xml version="1.0" ?><GEDCOM><INDI id="@I1@"><NAME ...

if __name__ == '__main__':
    main()
```

# Build Executable

1. You will need to have `cx_freeze` installed first
2. Build only tested on `Windows`
3. Replace `<path/to/your/python_directory>` in `setup.py` with your own python directory path.
4. Open Terminal/Cmd
5. Run `python setup.py build` to build the executable.

---
