use Net::IPv6Addr;

if( defined Net::IPv6Addr::is_ipv6($ip_address) ){
  print "Looks like an ipv6 address\n";
}
