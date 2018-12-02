
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.Scanner;

public class solution {

    public static void main(String[] args) {
        HashMap<Character,Character> map = new HashMap<>();
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');
        
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        for(int i=0; i<num ; i++){
             String expression = scan.next();
             System.out.println(isBalanced(expression, map) ? "YES" : "NO" );
        }
        scan.close();
        

    }
    public static boolean isBalanced(String expression, HashMap<Character,Character> map){
        
        if(expression.length()%2!=0){
            return false;
        }
        ArrayDeque<Character> deque = new ArrayDeque();
        for (int i=0; i<expression.length(); i++){
            Character ch = expression.charAt(i);
            if(map.containsKey(ch))
                deque.push(ch);
            else if(deque.isEmpty() || ch != map.get(deque.pop())){
                return false;
            }    
    }
 return deque.isEmpty();
}
}
