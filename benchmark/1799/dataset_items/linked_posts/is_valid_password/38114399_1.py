String pattern = "^(?=(.*\d){1})(.*\S)(?=.*[a-zA-Z\S])[0-9a-zA-Z\S]{8,}";
String password_string = "Type the password here"

private boolean isValidPassword(String password_string) {
    return password_string.matches(Constants.passwordPattern);
}
