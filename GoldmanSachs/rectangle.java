import java.io.*;
import java.util.*;

public class rectangle {
   public
    static void main(String[] args) throws Exception{
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t= Integer.parseInt(read.readLine());
        while(t-- >0)
        {
            String[] S = read.readLine().split(" ");
            int p[] = new int[2];
            int q[] = new int[2];
            int r[] = new int[2] ;
            int s[] = new int[2];

            p[0]=Integer.parseInt(S[0]);
            p[0]=Integer.parseInt(S[1]);
            p[0]=Integer.parseInt(S[2]);
            p[0]=Integer.parseInt(S[3]);
            p[0]=Integer.parseInt(S[4]);
            p[0]=Integer.parseInt(S[5]);
            p[0]=Integer.parseInt(S[6]);
            p[0]=Integer.parseInt(S[7]);
            Solution ob = new Solution();
            int ans = ob.doOverlap(p,q,r,s);
            System.out.println(ans);
      
        }
    } 
}        
 // logic for overlapping rectangle
 class Solution{
    int doOverlap(int L1[], int R1[], int L2[], int R2[]) {
        // code here if(L1[0]>R2[0] || L2[0]>R1[0])
        if(L1[0]>R2[0] || L2[0]>R1[0])
            return 0;
        if(R1[1]>L2[1]|| R2[1]>L1[1])
            return 0;
        return 1;
    
}
 }

