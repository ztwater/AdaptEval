function calcArea(poly) {
    if(!poly || poly.length < 3) return null;
    let end = poly.length - 1;
    let sum = poly[end][0]*poly[0][1] - poly[0][0]*poly[end][1];
    for(let i=0; i<end; ++i) {
        const n=i+1;
        sum += poly[i][0]*poly[n][1] - poly[n][0]*poly[i][1];
    }
    return sum;
}

function isClockwise(poly) {
    return calcArea(poly) > 0;
}

let poly = [[352,168],[305,208],[312,256],[366,287],[434,248],[416,186]];

console.log(isClockwise(poly));

let poly2 = [[618,186],[650,170],[701,179],[716,207],[708,247],[666,259],[637,246],[615,219]];

console.log(isClockwise(poly2));