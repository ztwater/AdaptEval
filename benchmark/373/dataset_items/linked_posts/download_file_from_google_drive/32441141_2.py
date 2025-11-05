gdrive download --stdout 0B7_OwkDsUIgFWXA1B2FPQfV5S8H | \
    pv -br -L 90k | cat > file.ext
