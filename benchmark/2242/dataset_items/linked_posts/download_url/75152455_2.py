class ProgressBar:

  def __init__(self):
      self.progress_bar = None

  def __call__(self, current_bytes, total_bytes, width):
      current_mb = round(current_bytes / 1024 ** 2, 1)
      total_mb = round(total_bytes / 1024 ** 2, 1)
      if self.progress_bar is None:
          self.progress_bar = tqdm(total=total_mb, desc="MB")
      delta_mb = current_mb - self.progress_bar.n
      self.progress_bar.update(delta_mb)
