function sphere ( N:float,k:int):Vector3 {
    var inc =  Mathf.PI  * (3 - Mathf.Sqrt(5));
    var off = 2 / N;
    var y = k * off - 1 + (off / 2);
    var r = Mathf.Sqrt(1 - y*y);
    var phi = k * inc;
    return Vector3((Mathf.Cos(phi)*r), y, Mathf.Sin(phi)*r); 
};
