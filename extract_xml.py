import zipfile
import xml.etree.ElementTree as ET

def get_xml_from_docx(docx_filename):
    with zipfile.ZipFile(docx_filename) as z:
        xml_content = z.read('word/document.xml')

    # with open('xml', 'wb') as xml_file:
    #     xml_file.write(xml_content)
    return xml_content


xml_content = get_xml_from_docx('test.doc')
tree = ET.fromstring(xml_content)
print(ET.tostring(tree, encoding='unicode'))
