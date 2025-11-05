namespace = get_namespace(tree.getroot())
print tree.find('./{0}parent/{0}version'.format(namespace)).text
