import java.util.HashMap;
import java.util.Map;

public class LRUCache{
    static class Node{
        int key , val;
        Node prev, next;
        Node(int k , int v){
            key =  k;
            val = v;
        }
    }
    //最近最少使用
    private Map<Integer, Node> map;
    private Node head, tail;
    private int capicity;
    
    public LRUCache(int capicity){
        map = new HashMap<>();
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head.next = tail;
        tail.prev = head;
        this.capicity = capicity;
    }
   
   public int get(int key){
       //移除节点
       if(!map.containsKey(key)){
           return -1;
       }
       // 添加节点到头部
       Node node = map.get(key);
       removeNode(node);
       addFirst(node);
       return node.val;
   }
   
   
   public void put(int key , int value){
      // 包含  —— 移除  、 追加
      if(map.containsKey(key)){
          Node node = map.get(key);
          node.val = value;
          removeNode(node);
          addFirst(node);
          return;
      }
      // 容量 
       if(map.size()>= capicity){
           Node del = tail.prev;
           removeNode(del);
           map.remove(del.key);
           
       }
       Node newNode = new Node(key,value); 
       map.put(key, newNode);
       addFirst(newNode);
   }
    
     //移除节点
    private void removeNode(Node node){
         node.prev.next = node.next;
         node.next.prev = node.prev;
    
    }   
       // 添加节点到头部
     private void addFirst(Node node){
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
        node.prev = head;
        
     }  
    
     public static void main(String[] args) {
        LRUCache cache = new LRUCache(2);
        cache.put(1, 1);
        cache.put(2, 2);
        System.out.println(cache.get(1)); // 返回 1
        cache.put(3, 3); // 该操作会使得密钥 2 作废
        System.out.println(cache.get(2)); // 返回 -1 (未找到)
        cache.put(4, 4); // 该操作会使得密钥 3 作废
        System.out.println(cache.get(3)); // 返回 -1 (未找到)
        System.out.println(cache.get(4)); // 返回 4
     }
       
}