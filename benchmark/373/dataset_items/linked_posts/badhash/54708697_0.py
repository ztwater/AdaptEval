#define MCR_HashTableSize 2^10

unsigned int
Hash_UInt_GRPrimeNumber(unsigned int key)
{
  key = key*2654435761 & (MCR_HashTableSize - 1)
  return key;
}
