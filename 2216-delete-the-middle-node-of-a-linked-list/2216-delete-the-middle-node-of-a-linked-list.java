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
    public ListNode deleteMiddle(ListNode head) {
        if(head==null){
            return null;
        }
        int tot = 0;
        ListNode cur = head;
        while (cur!=null){
            tot++;
            cur = cur.next;
        }
        if (tot == 1){
            return null;
        }
        int mid = tot / 2;
        
        ListNode temp = head;
        for(int i=0;i<mid-1; i++){
            temp = temp.next;
        }
        temp.next = temp.next.next;
        return head;
        // }else{
        //     ListNode temp = head;
        //     for(int i=0;i<mid-1; i++){
        //         temp = temp.next;
        //     }
        //     temp.next = temp.next.next;
        //     return head;
        // }
        
    }
}