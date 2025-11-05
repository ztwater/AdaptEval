use Validate::IP qw'is_ipv6';

if( is_ipv6($ip_address) ){
  print "Looks like an ipv6 address\n";
}
