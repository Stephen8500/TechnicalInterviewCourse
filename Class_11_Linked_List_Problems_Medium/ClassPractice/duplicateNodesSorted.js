// Write a program to remove duplicates from a sorted list
// (Add a function to your Linked List class code)

class Node {
    constructor(val) {
        this.data = val
        this.next = null
    }
}

class LinkedList {
    constructor() {
        this.head = null
    }

    insert(val) {
        const newNode = new Node(val)
        if (this.head) {
            let current = this.head
            while (current.next) {
                current = current.next
            }
            current.next = newNode
        } else {
            this.head = newNode
        }
    }

    remove(val) {
        let current = this.head
        let prev = null

        // if head exists, and it matches the value
        if (current !== null && current.data === val) {
            this.head = current.next
            return
        }

        while (current !== null && current.data !== val) {
            prev = current
            current = current.next
        }

        if (current === null) return

        // else, we've found the right node
        prev.next = current.next
    }

    reverse() {
        // iterate through each node
        // redirect .next to the previous node
        // head.next becomes null
        // tail becomes head

        let prev = null
        let current = this.head

        while (current !== null) {
            // reverse .next connection
            let temp = current.next
            current.next = prev

            // update pointers
            prev = current
            current = temp
        }

        this.head = prev
    }

    /** NEW STUFF HERE **/
    removeDuplicatesSorted() {
        // taken from geeksforgeeks.com
        
        /*Another reference to head*/
        let curr = this.head;
  
        /* Traverse list till the last node */
        while (curr != null) {
             let temp = curr;
            /*Compare current node with the next node and
            keep on deleting them until it matches the current
            node data */
            while(temp!=null && temp.data==curr.data) {
                temp = temp.next;
            }
            /*Set current node next to the next different
            element denoted by temp*/
            curr.next = temp;
            curr = curr.next;
        }
    }
}

let ll = new LinkedList()
ll.insert(1)
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
console.log(ll)
ll.removeDuplicatesSorted()
console.log(ll)