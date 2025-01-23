//{ Driver Code Starts
import java.util.*;

class Node {
    int data;
    Node next, random;

    Node(int d) {
        data = d;
        next = random = null;
    }
}

class Cloning {

    public static Node addToTheLast(Node head, Node node) {
        if (head == null) {
            return node;
        } else {
            Node temp = head;
            while (temp.next != null) temp = temp.next;
            temp.next = node;
            return head;
        }
    }

    public static boolean validation(Node head, Node res) {
        Node temp1 = head;
        Node temp2 = res;

        int len1 = 0, len2 = 0;
        while (temp1 != null) {
            len1++;
            temp1 = temp1.next;
        }
        while (temp2 != null) {
            len2++;
            temp2 = temp2.next;
        }

        if (len1 != len2) return false;

        HashMap<Node, Node> nodeMap = new HashMap<>();

        temp1 = head;
        temp2 = res;
        while (temp1 != null) {
            if (temp1 == temp2) return false;
            if (temp1.data != temp2.data) return false;

            if ((temp1.random == null && temp2.random != null) ||
                (temp1.random != null && temp2.random == null)) {
                return false;
            }
            if (temp1.random != null && temp2.random != null &&
                temp1.random.data != temp2.random.data) {
                return false;
            }
            nodeMap.put(temp1, temp2);
            temp1 = temp1.next;
            temp2 = temp2.next;
        }

        temp1 = head;
        temp2 = res;
        while (temp1 != null) {
            if (temp1.random != null && nodeMap.get(temp1.random) != temp2.random) {
                return false;
            }
            temp1 = temp1.next;
            temp2 = temp2.next;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine(); // Consume the newline after the integer input

        while (t-- > 0) {
            Node head = null, head2 = null;
            String line = sc.nextLine().trim();
            String[] numsStr = line.split(" ");
            int[] nums = Arrays.stream(numsStr).mapToInt(Integer::parseInt).toArray();

            int n = nums.length;
            head = addToTheLast(head, new Node(nums[0]));
            head2 = addToTheLast(head2, new Node(nums[0]));

            for (int i = 1; i < n; i++) {
                head = addToTheLast(head, new Node(nums[i]));
                head2 = addToTheLast(head2, new Node(nums[i]));
            }

            String line2 = sc.nextLine().trim();
            String[] numsStr2 = line2.split(" ");
            int[] nums2 = Arrays.stream(numsStr2).mapToInt(Integer::parseInt).toArray();
            int q = nums2.length / 2;

            for (int i = 0; i < q; i++) {
                int a = nums2[2 * i];
                int b = nums2[2 * i + 1];

                Node tempA = head;
                Node temp2A = head2;
                for (int j = 0; j < a - 1 && tempA != null; j++) {
                    tempA = tempA.next;
                    temp2A = temp2A.next;
                }
                Node tempB = head;
                Node temp2B = head2;
                for (int j = 0; j < b - 1 && tempB != null; j++) {
                    tempB = tempB.next;
                    temp2B = temp2B.next;
                }

                if (a <= n) {
                    tempA.random = tempB;
                    temp2A.random = temp2B;
                }
            }

            Solution g = new Solution();
            Node res = g.cloneLinkedList(head);
            if (res == null || res == head) {
                System.out.println("false");
                continue;
            }
            if (validation(head, res) && validation(head2, res))
                System.out.println("true");
            else
                System.out.println("false");
            System.out.println("~");
        }
        sc.close();
    }
}

// } Driver Code Ends


/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

/*
class Node {
    int data;
    Node next, random;

    Node(int d)
    {
        data = d;
        next = random = null;

    }
}*/

class Solution {
    // Function to clone a linked list with next and random pointer.
    Node cloneLinkedList(Node head)
    {
        Node currnode=head;
        while(currnode!=null)
        {
            Node nextnode=currnode.next;
            Node newnode=new Node(currnode.data);
            currnode.next=newnode;
            currnode=currnode.next;
            currnode.next=nextnode;
            currnode=currnode.next;
        }
        Node newhead=head.next;
        currnode=head;
        Node currnode1=newhead;
        while(currnode1!=null)
        {
            if(currnode.random!=null)
            {
                currnode1.random=currnode.random.next;
            }
            currnode=currnode.next.next;
            if(currnode==null)
            {
                break;
            }
            currnode1=currnode1.next.next;
        }
        currnode=head;
        currnode1=newhead;
        while(currnode!=null)
        {
            currnode.next=currnode.next.next;
            currnode1.next=currnode1.next.next;
            currnode=currnode.next;
            currnode1=currnode1.next;
            if(currnode1.next==null)
            {
                currnode.next=null;
                break;
            }
        }
        return newhead;
    }
}
