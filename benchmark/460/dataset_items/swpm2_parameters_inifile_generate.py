from ansible.module_utils.basic import missing_required_lib

LXML_LIBRARY_IMPORT_ERROR = None
try:
    from lxml import etree
except ImportError:
    LXML_LIBRARY_IMPORT_ERROR = traceback.format_exc()
    HAS_LXML_LIBRARY = False
else:
    HAS_LXML_LIBRARY = True


def set_has_lxml_library(b):
    global HAS_LXML_LIBRARY
    HAS_LXML_LIBRARY = b


# SWPM2 control.xml conversion to utf8
def control_xml_utf8(filepath, module):
    if not HAS_LXML_LIBRARY:
        module.fail_json(msg=missing_required_lib(
            "lxml"), exception=LXML_LIBRARY_IMPORT_ERROR)
    source = filepath + "/control.xml"
    # source = "input.xml"  # without file_path concat

    # Convert control.xml from iso-8859-1 to UTF-8, so it can be used with Beautiful Soup lxml-xml parser
    # https://stackoverflow.com/questions/64629600/how-can-you-convert-a-xml-iso-8859-1-to-utf-8-using-python-3-7-7/64634454#64634454
    with open(source, 'rb') as source:
        parser = etree.XMLParser(encoding="iso-8859-1", strip_cdata=False)
        # parser = etree.XMLParser(encoding="iso-8859-1")
        root = etree.parse(source, parser)

    string = etree.tostring(root, xml_declaration=True, encoding="UTF-8",
                            pretty_print=True).decode('utf8').encode('iso-8859-1')

#    string1 = etree.tostring(root, xml_declaration=True, encoding="UTF-8",
#                            pretty_print=True).decode('utf8').encode('utf-8').strip()

    # with open('output.xml', 'wb') as target:
    with open('control_utf8.xml', 'wb') as target:
        target.write(string)

