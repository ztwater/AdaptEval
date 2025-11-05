        try {
            IPAddressString str = new IPAddressString("::1");
            IPAddress addr = str.toAddress();
            if(addr.isIPv6() || addr.isIPv6Convertible()) {
                IPv6Address ipv6Addr = addr.toIPv6();
            }
            //use address
        } catch(AddressStringException e) {
            //e.getMessage has validation error
        }
