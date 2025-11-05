var pwdList = [
    '@@V4-\3Z`zTzM{>k',
    '12qw!"QW12',
    '123qweASD!"#',
    '1qA!"#$%&',
    'Günther32',
    '123456789',
    'qweASD123',
    'qweqQWEQWEqw',
    '12qwAS!'
  ],
  re = /^(?=\S*[a-z])(?=\S*[A-Z])(?=\S*\d)(?=\S*[^\w\s])\S{8,}$/;
  
  pwdList.forEach(function (pw) {
    document.write('<span style="color:'+ (re.test(pw) ? 'green':'red') + '">' + pw + '</span><br/>');
  });