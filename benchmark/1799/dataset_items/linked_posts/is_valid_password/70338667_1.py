const regex = /^(?=[^A-Z\n]*[A-Z])(?=[^a-z\n]*[a-z])(?=[^0-9\n]*[0-9])(?=[^#?!@$%^&*\n-]*[#?!@$%^&*-]).{8,}$/;
[
  "abcA1#!A",
  "#!asdfSFD1;",
  "# a f F1 ;",
  "1111111111",
  "aaaaaaaa",
  "11111111",
  "AAAAAAAA",
  "########",
  "aA1#"
].forEach(s =>
  console.log(regex.test(s) ? `Match --> ${s}` : `No match --> ${s}`)
);