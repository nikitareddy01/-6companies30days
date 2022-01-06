import java.io.*;
import java.util.*;

/**
 * DecodeSring
 */
public class DecodeSring {
    public static void main(String[] args)throws IOException {

        BufferedReader in= new BufferedReader(new InputStreamReader(System.in));
        String s =in.readLine();
        Solution ob = new Solution();
        System.out.println(ob.decodedString(s));
        

    }

}

class Solution{
    int i=0;
    public String decodedString(String s){
        // code here
        StringBuilder result = new StringBuilder();
        while(i<s.length() && s.charAt(i)!=']'){
            if(Character.isDigit(s.charAt(i))){
                int k=0;
                while(i< s.length() && Character.isDigit(s.charAt(i)))
                    k=k*10+s.charAt(i++)-'0';
            i++;
            String r= decodedString(s);
            while(k-- >0)
                result.append(r);
            i++;
            
            }
            else 
                result.append(s.charAt(i++));
        }
        return result.toString();
        
    }
}



