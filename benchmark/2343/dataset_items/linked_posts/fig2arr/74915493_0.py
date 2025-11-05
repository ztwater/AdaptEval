with io.BytesIO() as io_buf:
  fig.savefig(io_buf, format='raw', dpi=dpi)
  image = np.frombuffer(io_buf.getvalue(), np.uint8).reshape(
      int(fig.bbox.bounds[3]), int(fig.bbox.bounds[2]), -1)
