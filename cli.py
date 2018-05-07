"""gedcom parser"""

from gedcom_xml_parser.gedcom_xml_parser import GedcomXMLParser

def main():
    '''GedcomXMLParser usage'''
    gedcom_text = None
    input_file_path = input('Enter the path to .ged file (e.g. "folder/file.ged" without quotes): \n> ')
    with open(input_file_path, 'r') as input_file:
        gedcom_text = input_file.read()

    parser = GedcomXMLParser(gedcom_text)
    xml_text_pretty = parser.get_parsed_data()

    out_file_path = input('Enter the path to .xml file (e.g. "folder/file.xml" without quotes): \n> ')
    with open(out_file_path, 'w') as output_file:
        output_file.write(xml_text_pretty)

if __name__ == '__main__':
    main()
