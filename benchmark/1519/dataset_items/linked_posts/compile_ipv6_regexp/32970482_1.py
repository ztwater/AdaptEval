"The `ip` validator" should {
  "return false if the IPv4 is invalid" in {
    ip("123") must beFalse
    ip("255.255.255.256") must beFalse
    ip("127.1") must beFalse
    ip("30.168.1.255.1") must beFalse
    ip("-1.2.3.4") must beFalse
  }

  "return true if the IPv4 is valid" in {
    ip("255.255.255.255") must beTrue
    ip("127.0.0.1") must beTrue
    ip("0.0.0.0") must beTrue
  }

  //IPv6
  //@see: http://www.ronnutter.com/ipv6-cheatsheet-on-identifying-valid-ipv6-addresses/
  "return false if the IPv6 is invalid" in {
    ip("1200::AB00:1234::2552:7777:1313") must beFalse
  }

  "return true if the IPv6 is valid" in {
    ip("1200:0000:AB00:1234:0000:2552:7777:1313") must beTrue
    ip("21DA:D3:0:2F3B:2AA:FF:FE28:9C5A") must beTrue
  }
}
