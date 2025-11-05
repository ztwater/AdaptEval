function myFunction() {
    var str = "c1TTTTaTTT@";
    var patt = new RegExp("^.*(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])[a-zA-Z0-9@#$%^&+=]*$");
    var res = patt.test(str);
    console.log("Is regular matches:", res);
}
