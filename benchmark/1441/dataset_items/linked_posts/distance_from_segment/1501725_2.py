float dist_to_segment_squared(float px, float py, float pz, float lx1, float ly1, float lz1, float lx2, float ly2, float lz2) {
  float line_dist = dist_sq(lx1, ly1, lz1, lx2, ly2, lz2);
  if (line_dist == 0) return dist_sq(px, py, pz, lx1, ly1, lz1);
  float t = ((px - lx1) * (lx2 - lx1) + (py - ly1) * (ly2 - ly1) + (pz - lz1) * (lz2 - lz1)) / line_dist;
  t = constrain(t, 0, 1);
  return dist_sq(px, py, pz, lx1 + t * (lx2 - lx1), ly1 + t * (ly2 - ly1), lz1 + t * (lz2 - lz1));
}
