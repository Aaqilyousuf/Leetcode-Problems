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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head==null){
            return null;
        }
        ListNode cur = head;
        int tot = 0;
        while (cur!=null){
            tot += 1;
            cur = cur.next;
        }
        if(tot == 1 && n==1){
            return null;
        }
        int curPos = tot-n;
        if (curPos == 0) {
            return head.next;
        }
        ListNode cur1 = head;
        for (int i=0;i<curPos-1; i++){
            cur1 = cur1.next;
        }
        cur1.next = cur1.next.next;
        return head;
    }
}