#define hash32(x) ((x)*2654435761)
#define H_BITS 24 // Hashtable size
#define H_SHIFT (32-H_BITS)
unsigned hashtab[1<<H_BITS]  
.... 
unsigned slot = hash32(x) >> H_SHIFT
