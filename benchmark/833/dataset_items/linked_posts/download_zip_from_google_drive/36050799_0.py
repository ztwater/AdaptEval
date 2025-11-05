private InputStream gConnect(String remoteFile) throws IOException{
    URL  url = new URL(remoteFile);
    URLConnection connection = url.openConnection();
    if(connection instanceof HttpURLConnection){
        HttpURLConnection httpConnection = (HttpURLConnection) connection;
        connection.setAllowUserInteraction(false);
        httpConnection.setInstanceFollowRedirects(true);
        httpConnection.setRequestProperty("User-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows 2000)");
        httpConnection.setDoOutput(true);          
        httpConnection.setRequestMethod("GET");
        httpConnection.connect();

        int reqCode = httpConnection.getResponseCode();


        if(reqCode == HttpURLConnection.HTTP_OK){
            InputStream is = httpConnection.getInputStream();
            Map<String, List<String>> map = httpConnection.getHeaderFields();
            List<String> values = map.get("content-type");
            if(values != null && !values.isEmpty()){
                String type = values.get(0);

                if(type.contains("text/html")){
                    String cookie = httpConnection.getHeaderField("Set-Cookie");
                    String temp = Constants.getPath(mContext, Constants.PATH_TEMP) + "/temp.html";
                    if(saveGHtmlFile(is, temp)){
                        String href = getRealUrl(temp);
                        if(href != null){
                            return parseUrl(href, cookie);
                        }
                    }


                } else if(type.contains("application/json")){
                    String temp = Constants.getPath(mContext, Constants.PATH_TEMP) + "/temp.txt";
                    if(saveGJsonFile(is, temp)){
                        FileDataSet data = JsonReaderHelper.readFileDataset(new File(temp));
                        if(data.getPath() != null){
                            return parseUrl(data.getPath());
                        }
                    }
                }
            }
            return is;
        }
    }
    return null;
}
