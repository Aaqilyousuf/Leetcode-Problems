/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head==null){
            return null;
        }
        head = connectBw(head);
        connectRandom(head);
        return deepCopy(head);
    }
    public Node connectBw(Node head){
        Node temp = head;
        while(temp!=null){
            Node copyNode = new Node(temp.val);
            copyNode.next = temp.next;
            temp.next = copyNode;
            temp = temp.next.next;
        }
        return head;
    }
    public void connectRandom(Node head){
        Node temp = head;
        while(temp!=null){
            Node copyNode = temp.next;
            if(temp.random!=null){
                copyNode.random = temp.random.next;
            }else{
                copyNode.random = null;
            }
            temp = temp.next.next;

        }
    }
    public Node deepCopy(Node head){
        //in this function we connect our copied LL 
        Node dummyNode = new Node(-1);
        Node res = dummyNode;
        Node temp = head;
        while (temp!=null){
            //connecting our copied ll to dummy node
            res.next = temp.next;
            temp.next = temp.next.next;
            //moving to next connection
            res = res.next;
            temp = temp.next;
        }
        return dummyNode.next;
    }
}