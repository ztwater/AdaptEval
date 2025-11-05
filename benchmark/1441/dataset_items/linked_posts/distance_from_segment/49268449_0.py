// Return minimum distance between line segment: head--->tail and point
double MinimumDistance(Eigen::Vector3d head, Eigen::Vector3d tail,Eigen::Vector3d point)
{
    double l2 = std::pow((head - tail).norm(),2);
    if(l2 ==0.0) return (head - point).norm();// head == tail case

    // Consider the line extending the segment, parameterized as head + t (tail - point).
    // We find projection of point onto the line.
    // It falls where t = [(point-head) . (tail-head)] / |tail-head|^2
    // We clamp t from [0,1] to handle points outside the segment head--->tail.

    double t = max(0,min(1,(point-head).dot(tail-head)/l2));
    Eigen::Vector3d projection = head + t*(tail-head);

    return (point - projection).norm();
}
