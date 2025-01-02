/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        ArrayList<Integer> list = new ArrayList<>();
        ListNode cur = head;
        while(cur!=null){
            list.add(cur.val);
            cur = cur.next;
        }
        Collections.sort(list);
        ListNode res = insert(list);
        return res;

    }
    public ListNode insert(ArrayList<Integer> list){
         if (list == null || list.size() == 0) {
            return null;
        }
        ListNode head = new ListNode(list.get(0));
        ListNode cur = head;
        for (int i=1;i<list.size();i++){
            ListNode newNode = new ListNode(list.get(i));
            cur.next = newNode;
            cur = newNode; 
        }
        return head;
    }
}