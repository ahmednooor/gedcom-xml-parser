"""
# GEDCOM to XML Parser/Convertor
# ~ Author: Ahmed Noor ('https://github.com/ahmednooor')

# Usage:
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
    print()
    print('# --- Parsed XML (Minified):')
    print(xml_text_minified)

if __name__ == '__main__':
    main()
"""


class GedcomXMLParser:
    """GEDCOM to XML Parser Class
    
    Usage:
        gedcom_text = r'''0 @I1@ INDI
        1 NAME Jamis Gordon /Buck/
        2 SURN Buck
        2 GIVN Jamis Gordon
        1 SEX M'''

        parser = GedcomXMLParser(gedcom_text)
        xml_text_pretty = parser.get_parsed_data()
        xml_text_minified = parser.get_parsed_data_minified()
    """

    def __init__(self, unparsed_data):
        """initialize object"""
        self._raw_data = unparsed_data
        if isinstance(unparsed_data, str) is False:
            raise TypeError(
                '"GedcomXMLParser" can only receive argument of type "str". "{}" was given.'
                .format(type(unparsed_data)),
                unparsed_data
            )

        self._tokenized_data = self._tokenize()
        self._parsed_data = self._parse_to_xml()

    def _tokenize(self):
        """tokenize data
        ~ tokenize the string into list of dicts,
        containing (level, tag, id, data)"""
        data = self._raw_data
        data = data.split('\n')
        data = [item for item in data if item != '']
        data = [
            ' '.join([elem for elem in item.split(' ') if elem != ''])
            for item in data
        ]
        data = [
            {
                'level': int(item.split(' ')[0]),
                'id' \
                    if item.split(' ')[1][0] == '@' \
                    and item.split(' ')[1][-1] == '@' \
                    else 'tag': item.split(' ')[1],
                'tag' \
                    if item.split(' ')[1][0] == '@' \
                    and item.split(' ')[1][-1] == '@' \
                    else 'data': ' '.join(item.split(' ')[2::])
                                 .strip()
                                 .replace('&', '&amp;')
                                 .replace('<', '&lt;')
                                 .replace('>', '&gt;')
                                 .replace('"', '&quot;')
                                 .replace('\'', '&apos;')
            }
            for item in data
        ]
        return data

    def _parse_to_xml(self):
        """parse data
        ~ parse the tokenized data into xml
        according to (level, tag, id, data) rules"""
        data = self._tokenized_data
        if data is None:
            return None

        data_len = len(data)
        parsed_tree = ['<?xml version="1.0" ?>', '<GEDCOM>']
        prev_level = 0

        def add_tabs(parsed_tree, level):
            """add tabs to pretify"""
            tabs = ''
            for _k in range(0, level):
                tabs = tabs + '\t'

            parsed_tree[-1] = tabs + parsed_tree[-1]

        for i in range(0, data_len):
            if data[i]['level'] < prev_level:
                j = i
                while j >= 0:
                    if data[j-1]['level'] < data[j]['level'] \
                            and data[j-1]['level'] < prev_level:
                        parsed_tree.append(
                            '</' + data[j-1]['tag'] + '>'
                        )
                        add_tabs(parsed_tree, data[j-1]['level'] + 1)

                        prev_level = data[j-1]['level']
                    if data[j-1]['level'] == data[i]['level']:
                        break
                    j -= 1

            string = '<' + data[i]['tag']
            if 'id' in data[i]:
                if i < data_len - 1 and data[i+1]['level'] == data[i]['level']:
                    string = string + '></' + data[i]['tag'] + '>'
                else:
                    string = string + ' id="' + data[i]['id'] + '">'
            if 'data' in data[i]:
                if i < data_len - 1 and data[i+1]['level'] > data[i]['level']:
                    string = (string + ' value="' + data[i]['data'] + '">') \
                                if data[i]['data'] != '' \
                                else (string + '>')
                else:
                    string = string + '>' + data[i]['data'] + '</' \
                        + data[i]['tag'] + '>'

            parsed_tree.append(string)
            add_tabs(parsed_tree, data[i]['level'] + 1)
            prev_level = data[i]['level']

            if i == data_len - 1 and data[i]['level'] > 0:
                j = i
                while j >= 0:
                    if data[j-1]['level'] < data[j]['level'] \
                            and data[j-1]['level'] < prev_level:
                        parsed_tree.append(
                            '</' + data[j-1]['tag'] + '>'
                        )
                        add_tabs(parsed_tree, data[j-1]['level'] + 1)

                        prev_level = data[j-1]['level']
                    if data[j-1]['level'] == 0:
                        break
                    j -= 1

        parsed_tree.append('</GEDCOM>')
        return '\n'.join(parsed_tree)

    def get_parsed_data(self):
        """get parsed data"""
        return self._parsed_data

    def get_parsed_data_minified(self):
        """get parsed data minified"""
        return self._parsed_data.replace('\t', '').replace('\n', '')

    def __str__(self):
        """str representation"""
        return self._parsed_data
