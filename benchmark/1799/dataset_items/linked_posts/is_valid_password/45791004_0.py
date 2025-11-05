def validatePassword(password: String): Boolean = {
  if (password.length < 8)
    return false

  var lower = false
  var upper = false
  var numbers = false
  var special = false

  password.foreach { c =>
    if (c.isDigit)       numbers = true
    else if (c.isLower)  lower = true
    else if (c.isUpper)  upper = true
    else                 special = true
  }

  lower && upper && numbers && special
}
