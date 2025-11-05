class RawText(minidom.Text):
    def writexml(self, writer, indent='', addindent='', newl=''):
        '''
        patching minidom.Text.writexml:1087
        the original calls minidom._write_data:302
        below is a combined version of both, but without the '&' replacements and so on..
        '''
        if self.data:
            writer.write('{}{}{}'.format(indent, self.data, newl))
