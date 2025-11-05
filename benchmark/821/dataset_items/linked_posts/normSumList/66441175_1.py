norm = (lambda the_max, the_min: [(float(i)-the_min)/(the_max-the_min) for i in raw])(max(raw),min(raw))
