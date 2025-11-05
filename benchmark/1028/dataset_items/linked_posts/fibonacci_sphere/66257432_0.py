// golden angle in radians
static float Phi = Mathf.PI * ( 3f - Mathf.Sqrt( 5f ) );
static float Pi2 = Mathf.PI * 2;

public static Vector3 Point( float radius , int index , int total , float min = 0f, float max = 1f , float angleStartDeg = 0f, float angleRangeDeg = 360 )
{
    // y goes from min (-) to max (+)
    var y = ( ( index / ( total - 1f ) ) * ( max - min ) + min ) * 2f - 1f;

    // golden angle increment
    var theta = Phi * index ; 
        
    if( angleStartDeg != 0 || angleRangeDeg != 360 )
    {
        theta = ( theta % ( Pi2 ) ) ;
        theta = theta < 0 ? theta + Pi2 : theta ;
            
        var a1 = angleStartDeg * Mathf.Deg2Rad;
        var a2 = angleRangeDeg * Mathf.Deg2Rad;
            
        theta = theta * a2 / Pi2 + a1;
    }

    // https://stackoverflow.com/a/26127012/2496170
    
    // radius at y
    var rY = Mathf.Sqrt( 1 - y * y ); 
    
    var x = Mathf.Cos( theta ) * rY;
    var z = Mathf.Sin( theta ) * rY;

    return  new Vector3( x, y, z ) * radius;
}
