function absAngle(a) {
  // this yields correct counter-clock-wise numbers, like 350deg for -370
  return (360 + (a % 360)) % 360;
}

function angleDelta(a, b) {
  // https://gamedev.stackexchange.com/a/4472
  let delta = Math.abs(absAngle(a) - absAngle(b));
  let sign = absAngle(a) > absAngle(b) || delta >= 180 ? -1 : 1;
  return (180 - Math.abs(delta - 180)) * sign;
}

// sample output
for (let angle = -370; angle <= 370; angle+=20) {
  let testAngle = 10;
  console.log(testAngle, "->", angle, "=", angleDelta(testAngle, angle));
}