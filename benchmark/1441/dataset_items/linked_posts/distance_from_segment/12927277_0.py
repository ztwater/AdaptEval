create function fn_sqr (@NumberToSquare decimal(18,10)) 
returns decimal(18,10)
as 
begin
    declare @Result decimal(18,10)
    set @Result = @NumberToSquare * @NumberToSquare
    return @Result
end
go

create function fn_Distance(@ax decimal (18,10) , @ay decimal (18,10), @bx decimal(18,10),  @by decimal(18,10)) 
returns decimal(18,10)
as
begin
    declare @Result decimal(18,10)
    set @Result = (select dbo.fn_sqr(@ax - @bx) + dbo.fn_sqr(@ay - @by) )
    return @Result
end
go

create function fn_DistanceToSegmentSquared(@px decimal(18,10), @py decimal(18,10), @ax decimal(18,10), @ay decimal(18,10), @bx decimal(18,10), @by decimal(18,10)) 
returns decimal(18,10)
as 
begin
    declare @l2 decimal(18,10)
    set @l2 = (select dbo.fn_Distance(@ax, @ay, @bx, @by))
    if @l2 = 0
        return dbo.fn_Distance(@px, @py, @ax, @ay)
    declare @t decimal(18,10)
    set @t = ((@px - @ax) * (@bx - @ax) + (@py - @ay) * (@by - @ay)) / @l2
    if (@t < 0) 
        return dbo.fn_Distance(@px, @py, @ax, @ay);
    if (@t > 1) 
        return dbo.fn_Distance(@px, @py, @bx, @by);
    return dbo.fn_Distance(@px, @py,  @ax + @t * (@bx - @ax),  @ay + @t * (@by - @ay))
end
go

create function fn_DistanceToSegment(@px decimal(18,10), @py decimal(18,10), @ax decimal(18,10), @ay decimal(18,10), @bx decimal(18,10), @by decimal(18,10)) 
returns decimal(18,10)
as 
begin
    return sqrt(dbo.fn_DistanceToSegmentSquared(@px, @py , @ax , @ay , @bx , @by ))
end
go

--example execution for distance from a point at (6,1) to line segment that runs from (4,2) to (2,1)
select dbo.fn_DistanceToSegment(6, 1, 4, 2, 2, 1) 
--result = 2.2360679775

--example execution for distance from a point at (-3,-2) to line segment that runs from (0,-2) to (-2,1)
select dbo.fn_DistanceToSegment(-3, -2, 0, -2, -2, 1) 
--result = 2.4961508830

--example execution for distance from a point at (0,-2) to line segment that runs from (0,-2) to (-2,1)
select dbo.fn_DistanceToSegment(0,-2, 0, -2, -2, 1) 
--result = 0.0000000000
