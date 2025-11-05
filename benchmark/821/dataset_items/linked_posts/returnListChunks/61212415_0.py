def main():
  print(chunkify([1,2,3,4,5,6],2))

def chunkify(list, n):
  chunks = []
  for i in range(0, len(list), n):
    chunks.append(list[i:i+n])
  return chunks

main()
