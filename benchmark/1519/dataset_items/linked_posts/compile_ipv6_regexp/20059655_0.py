$is_ip4address = (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4) !== FALSE);
$is_ip6address = (filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6) !== FALSE);
