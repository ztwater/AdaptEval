    int[] a = {1,3,2,4,5,4,6,7};
    StringBuilder s1 = new StringBuilder();
    for(int i : a){
     s1.append(i);
    }       
    StringBuilder s2 = new StringBuilder();
    int count = findSubstring(s1.toString(), s2);       
    System.out.println(s2.reverse());

public static int findSubstring(String str1, StringBuilder s2){     
    StringBuilder s1 = new StringBuilder(str1);
    if(s1.length() == 0){
        return 0;
    }
    if(s2.length() == 0){
        s2.append(s1.charAt(s1.length()-1));
        findSubstring(s1.deleteCharAt(s1.length()-1).toString(), s2);           
    } else if(s1.charAt(s1.length()-1) < s2.charAt(s2.length()-1)){ 
        char c = s1.charAt(s1.length()-1);
        return 1 + findSubstring(s1.deleteCharAt(s1.length()-1).toString(), s2.append(c));
    }
    else{
        char c = s1.charAt(s1.length()-1);
        StringBuilder s3 = new StringBuilder();
        for(int i=0; i < s2.length(); i++){
            if(s2.charAt(i) > c){
                s3.append(s2.charAt(i));
            }
        }
        s3.append(c);
        return Math.max(findSubstring(s1.deleteCharAt(s1.length()-1).toString(), s2), 
                findSubstring(s1.deleteCharAt(s1.length()-1).toString(), s3));
    }       
    return 0;
}
