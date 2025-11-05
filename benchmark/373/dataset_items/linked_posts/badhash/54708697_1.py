unsigned int Hash_UInt_M3(unsigned int key)
{
  key ^= (key << 13);
  key ^= (key >> 17);    
  key ^= (key << 5); 
  return key;
}
