parser = argparse.ArgumentParser(formatter_class=CustomArgumentFormatter)

parser.add_argument(
    '--ethernet_config', type=str, required=False, default=None,
    help='Path to a text file that specifies Ethernet network IP settings \
      to use on the board. For example: \
      \n\t ip=192.0.2.100 \
      \n\t subnet_mask=255.255.255.0 \
      \n\t gateway=192.0.2.1')
