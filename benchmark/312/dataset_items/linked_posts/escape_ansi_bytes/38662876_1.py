def test_remove_ansi_escape_sequence(self):
    line = '\t\u001b[0;35mBlabla\u001b[0m                                  \u001b[0;36m172.18.0.2\u001b[0m'

    escaped_line = escape_ansi(line)

    self.assertEqual(escaped_line, '\tBlabla                                  172.18.0.2')
