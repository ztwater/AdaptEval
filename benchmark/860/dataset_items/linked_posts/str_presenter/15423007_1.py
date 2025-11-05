{multiline: 'Line1

    Line2

    Line3

    ', multiline-unicode: "L\xEAne1\nL\xEAne2\nL\xEAne3\n", short: Hello}

{multiline: 'Line1

    Line2

    Line3

    ', multiline-unicode: 'Lêne1

    Lêne2

    Lêne3

    ', short: Hello}

After override

multiline: |
  Line1
  Line2
  Line3
multiline-unicode: "L\xEAne1\nL\xEAne2\nL\xEAne3\n"
short: Hello

multiline: |
  Line1
  Line2
  Line3
multiline-unicode: |
  Lêne1
  Lêne2
  Lêne3
short: Hello
