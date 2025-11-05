from pathvalidate import sanitize_filename

fname = "fi:l*e/p\"a?t>h|.t<xt"
print(f"{fname} -> {sanitize_filename(fname)}\n")
fname = "\0_a*b:c<d>e%f/(g)h+i_0.txt"
print(f"{fname} -> {sanitize_filename(fname)}\n")
