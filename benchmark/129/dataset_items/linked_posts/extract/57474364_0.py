def parse_xml(xml_path: Path) -> Tuple[ET.Element, Dict[str, str]]:
    xml_iter = ET.iterparse(xml_path, events=["start-ns"])
    xml_namespaces = dict(prefix_namespace_pair for _, prefix_namespace_pair in xml_iter)
    return xml_iter.root, xml_namespaces
