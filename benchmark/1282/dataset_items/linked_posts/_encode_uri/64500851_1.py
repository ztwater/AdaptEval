text = "Lorem ipsum dolor sit amet"
intermediates = [text := text.replace(i, "") for i in "aeiou" if i in text]

['Lorem ipsum dolor sit met',
 'Lorm ipsum dolor sit mt',
 'Lorm psum dolor st mt',
 'Lrm psum dlr st mt',
 'Lrm psm dlr st mt']
