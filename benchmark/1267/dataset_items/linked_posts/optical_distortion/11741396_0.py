IplImage* barrel_pincusion_dist(IplImage* img, double Cx,double Cy,double kx,double ky)
{
    IplImage* mapx = cvCreateImage( cvGetSize(img), IPL_DEPTH_32F, 1 );
    IplImage* mapy = cvCreateImage( cvGetSize(img), IPL_DEPTH_32F, 1 );

    int w= img->width;
    int h= img->height;

    float* pbuf = (float*)mapx->imageData;
    for (int y = 0; y < h; y++)
    {
        for (int x = 0; x < w; x++)
        {         
            float u= Cx+(x-Cx)*(1+kx*((x-Cx)*(x-Cx)+(y-Cy)*(y-Cy)));
            *pbuf = u;
            ++pbuf;
        }
    }

    pbuf = (float*)mapy->imageData;
    for (int y = 0;y < h; y++)
    {
        for (int x = 0; x < w; x++) 
        {
            *pbuf = Cy+(y-Cy)*(1+ky*((x-Cx)*(x-Cx)+(y-Cy)*(y-Cy)));
            ++pbuf;
        }
    }

    /*float* pbuf = (float*)mapx->imageData;
    for (int y = 0; y < h; y++)
    {
        int ty= y-Cy;
        for (int x = 0; x < w; x++)
        {
            int tx= x-Cx;
            int rt= tx*tx+ty*ty;

            *pbuf = (float)(tx*(1+kx*rt)+Cx);
            ++pbuf;
        }
    }

    pbuf = (float*)mapy->imageData;
    for (int y = 0;y < h; y++)
    {
        int ty= y-Cy;
        for (int x = 0; x < w; x++) 
        {
            int tx= x-Cx;
            int rt= tx*tx+ty*ty;

            *pbuf = (float)(ty*(1+ky*rt)+Cy);
            ++pbuf;
        }
    }*/

    IplImage* temp = cvCloneImage(img);
    cvRemap( temp, img, mapx, mapy ); 
    cvReleaseImage(&temp);
    cvReleaseImage(&mapx);
    cvReleaseImage(&mapy);

    return img;
}
