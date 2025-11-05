private double shortestDistance(float x1,float y1,float x2,float y2,float x3,float y3)
    {
        float px=x2-x1;
        float py=y2-y1;
        float temp=(px*px)+(py*py);
        float u=((x3 - x1) * px + (y3 - y1) * py) / (temp);
        if(u>1){
            u=1;
        }
        else if(u<0){
            u=0;
        }
        float x = x1 + u * px;
        float y = y1 + u * py;

        float dx = x - x3;
        float dy = y - y3;
        double dist = Math.sqrt(dx*dx + dy*dy);
        return dist;

    }
