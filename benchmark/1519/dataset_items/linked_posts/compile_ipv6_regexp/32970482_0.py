libraryDependencies += "commons-validator" % "commons-validator" % "1.4.1"


import org.apache.commons.validator.routines._

/**
 * Validates if the passed ip is a valid IPv4 or IPv6 address.
 *
 * @param ip The IP address to validate.
 * @return True if the passed IP address is valid, false otherwise.
 */  
 def ip(ip: String) = InetAddressValidator.getInstance().isValid(ip)
