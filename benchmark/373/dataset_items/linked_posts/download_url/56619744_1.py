with open(out_path, "wb") as f:
    response = urlopen(filepath)
    data_read = chunk_read(response, report_hook=chunk_report)

    f.write(data_read)
