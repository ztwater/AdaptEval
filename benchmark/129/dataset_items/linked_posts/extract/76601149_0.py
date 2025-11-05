#! /usr/bin/env python3

import lxml.etree
import io



def parse_xml_stream(xml_stream, ignore_default_ns=True):
    """
    ignore_default_ns:
    ignore the default namespace of the root node.

    by default, lxml.etree.iterparse
    returns the namespace in every element.tag.

    with ignore_default_ns=True,
    element.tag returns only the element's localname,
    without the namespace.

    example:
    xml_string:
        <html xmlns="http://www.w3.org/1999/xhtml">
            <div>hello</div>
        </html>
    with ignore_default_ns=False:
        element.tag = "{http://www.w3.org/1999/xhtml}div"
    with ignore_default_ns=True:
        element.tag = "div"

    see also:
    Python ElementTree module: How to ignore the namespace of XML files
    https://stackoverflow.com/a/76601149/10440128
    """

    # save the original read method
    xml_stream_read = xml_stream.read

    if ignore_default_ns:
        def xml_stream_read_track(_size):
            # ignore size, always return 1 byte
            # so we can track node positions
            return xml_stream_read(1)
        xml_stream.read = xml_stream_read_track

    def get_parser(stream):
        return lxml.etree.iterparse(
            stream,
            events=('start', 'end'),
            remove_blank_text=True,
            huge_tree=True,
        )

    if ignore_default_ns:
        # parser 1
        parser = get_parser(xml_stream)

        # parse start of root node
        event, element = next(parser)
        #print(xml_stream.tell(), event, element)
        # get name of root node
        root_name = element.tag.split("}")[-1]
        #print("root name", root_name)
        #print("root pos", xml_stream.tell()) # end of start-tag
        # attributes with namespaces
        #print("root attrib", element.attrib)

        # patched document header without namespaces
        xml_stream_nons = io.BytesIO(b"\n".join([
            #b"""<?xml version="1.0" encoding="utf-8"?>""",
            b"<" + root_name.encode("utf8") + b"><dummy/>",
        ]))
        xml_stream.read = xml_stream_nons.read

    # parser 2
    parser = get_parser(xml_stream)

    # parse start of root node
    # note: if you only need "end" events,
    # then wait for end of dummy node
    event, element = next(parser)
    print(event, element.tag)
    assert event == "start"

    if ignore_default_ns:
        assert element.tag == root_name

        # parse start of dummy node
        event, element = next(parser)
        #print(event, element.tag)
        assert event == "start"
        assert element.tag == "dummy"

        # parse end of dummy node
        event, element = next(parser)
        #print(event, element.tag)
        assert event == "end"
        assert element.tag == "dummy"

        # restore the original read method
        xml_stream.read = xml_stream_read

        # now all elements come without namespace
        # so element.tag is the element's localname
        #print("---")

    # TODO handle events

    #for i in range(5):
    #    event, element = next(parser)
    #    print(event, element)

    for event, element in parser:
        print(event, element.tag)



# xml with namespace in root node
xml_bytes = b"""\
<?xml version="1.0" encoding="utf-8"?>
<doc version="1" xmlns="http://www.test.com">
    <node/>
    <!--
        limitation: this breaks the parser.
        lxml.etree.XMLSyntaxError:
        Namespace prefix some-ns on some-name is not defined
        <some-ns:some-name/>
    -->
</doc>
"""

print("# keep default namespace")
parse_xml_stream(io.BytesIO(xml_bytes), False)

print()

print("# ignore default namespace")
parse_xml_stream(io.BytesIO(xml_bytes))
