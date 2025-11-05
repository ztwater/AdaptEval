   public static FileDataSet readFileDataset(File file) throws IOException{
        FileInputStream is = new FileInputStream(file);
        JsonReader reader = new JsonReader(new InputStreamReader(is, "UTF-8"));

        reader.beginObject();
        FileDataSet rs = new FileDataSet();
        while(reader.hasNext()){
            String name = reader.nextName();
            if(name.equals("downloadUrl")){
                rs.setPath(reader.nextString());
            } else if(name.equals("fileName")){
                rs.setName(reader.nextString());
            } else if(name.equals("sizeBytes")){
                rs.setSize(reader.nextLong());
            } else {
                reader.skipValue();
            }
        }
        reader.endObject();
        return rs;

    }
