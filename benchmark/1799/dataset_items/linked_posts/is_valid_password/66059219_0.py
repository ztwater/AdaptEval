     var value=$("#password").val();
     $.validator.addMethod("strongePassword",function(value) 
     {
         return /^[A-Za-z0-9!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]*$/.test(value) && /[a-z]/.test(value) && /\d/.test(value) && /[A-Z]/.test(value)&& /[A-Z]/.test(value);`enter code here`
     },'Password must have minimum 9 characters and contain at least 1 UPPERCASE, 1 lower case, 1 number, 1 special character.');
