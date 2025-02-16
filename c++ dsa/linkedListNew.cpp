#include<iostream>
using namespace std;

struct Node {
    int data;
    Node * next;

    Node(int d) {
        data = d;
        next = NULL;
    }
};

class LinkedList {
    Node *head, *tail;
    int size;

    public:
        LinkedList() {
            head = tail = NULL;
            size = 0;
        }

        void print() {
            Node *temp = head;

            if (head == NULL) {
                cout << "The Linked List is empty\n";
                return;
            }

            while (temp != NULL) {
                cout << temp -> data;

                if (temp -> next == NULL) 
                    cout << endl;
                else 
                    cout << " --> ";
                
                temp = temp -> next;
            }
        }

        void addAtBack(int val) {
            Node *temp = new Node(val);
            // temp -> data = val;
            // temp -> next = NULL;

            if (head == NULL) {
                head = tail = temp;
            } else {
                tail -> next = temp;
                tail = temp;
            }

            size++;
        }

        void addAtFront(int val) {
            Node *temp = new Node(val);
            // temp -> data = val;
            // temp -> next = NULL;

            if (head == NULL) {
                head = tail = temp;
            } else {
                temp -> next = head;
                head = temp;
            }

            size++;
        }

        void addAtIndex(int index, int val) {
            if (index > size) {
                cout << "Not possible to insert at this position\n";
                return;
            }

            if (index == 0) {
                addAtFront(val);
            } else if (index == size) {
                addAtBack(val);
            } else {
                Node *temp = head;
                for (int i = 0; i < index-1; ++i, temp = temp->next);

                Node *new_node = new Node(val);
                // new_node -> data = val;
                new_node -> next = temp -> next;
                temp -> next = new_node;
                size++;
            }
        }

        void printKthEle(int index) {
            if (index >= size || index < 0) {
                cout << "Index out of bouds\n";
                return;
            }

            Node *temp  = head;
            for (int i = 0; i < index; ++i, temp = temp->next);
            cout << temp -> data << endl;
        }

        void deleteKthEle(int index) {
            if (index >= size || index < 0) {
                cout << "Index out of bouds\n";
                return;
            }

            Node *prev, *curr = head;

            if (index == 0) {
                head = curr -> next;
                free(curr);
                size--;  
                return;
            }  

            for (int i = 0; i < index; ++i) {
                prev = curr;
                curr = curr -> next;
            }

            prev -> next = curr -> next;
            free(curr);

            if (index == size-1) {
                prev -> next == NULL;
                tail = prev;
            }
        
            size--;
        }

        void reverse() {
            Node *prev = NULL, *curr = head;

            if (curr == NULL) {
                cout << "The Linked List is empty\n";
                return;
            }
            // We will reverse the links while traversing
            while(curr != NULL) {
                Node *temp = curr -> next;
                curr -> next = prev;
                prev = curr;
                curr = temp;
            }

            swap(head, tail);

        }

        void middleEle() {
            Node *slow = head, *fast = head;

            while (fast != NULL && fast -> next != NULL) {
                slow = slow -> next;
                fast = fast -> next -> next;
            }

            cout << slow -> data << endl;
        }

        void nthFromEnd(int index) {
            int nthEle = size - index;

            Node *temp = head;
            for (int i = 0; i < nthEle; ++i, temp = temp->next);

            cout << temp -> data << endl;
        }

        void nthFromEndtwoPtr(int n) {
            Node *main_ptr = head, *ref_ptr = head;

            for (int i = 0; i < n; ++i, ref_ptr = ref_ptr -> next);

            while(ref_ptr != NULL) {
                main_ptr = main_ptr -> next;
                ref_ptr = ref_ptr -> next;
            }

            cout << main_ptr -> data << endl;
        }

        // Recursively reverse a Linked List
        void recReverse(Node *curr, Node *prev) {
            if (curr == NULL) {
                cout << "The Linked List is empty\n";
                return;
            }

            if (curr -> next == NULL) {
                head = curr;
                curr -> next = prev;
                return;
            }

            Node *temp = curr -> next;
            curr -> next = prev;
            recReverse(temp, curr);
        }

        void deleteEntireLinkedList() {
            Node *temp = NULL;

            while (head != NULL) {
                temp = head -> next;
                free(head);
                size--;
                head = temp;
            }

        }


        int getSize() {
            return size;
        }

        Node *getHead() {
            return head;
        }
   
};



int main() {
    LinkedList a;

    a.addAtBack(12);
    a.addAtBack(10);
    a.addAtBack(1);
    a.addAtBack(5);
    a.addAtFront(20);
    a.addAtFront(25);
    a.addAtFront(30);
    a.addAtIndex(1, 5);
    a.addAtIndex(5, 50);
    a.addAtIndex(3, 34);

    a.print();

    // a.deleteEntireLinkedList();
    // a.print();

    // a.nthFromEnd(1);
    // a.nthFromEndtwoPtr(1);
    // a.nthFromEnd(2);
    // a.nthFromEndtwoPtr(2);
    // a.nthFromEnd(3);
    // a.nthFromEndtwoPtr(3);
    // a.nthFromEnd(7);
    // a.nthFromEndtwoPtr(7);
    a.middleEle();
    // cout << a.getHead() << endl;
    // a.reverse();
    // a.print();

    // a.recReverse(a.getHead(), NULL);
    // a.print();
    // cout << a.getSize() << endl;

    // a.deleteKthEle(0);
    // a.print();
    // a.deleteKthEle(2);
    // a.print();
    // a.deleteKthEle(5);
    // a.print();
    // a.deleteKthEle(9);
    // a.print();
    // a.reverse();
    // a.print();

    // a.addAtIndex(12, 5);

    // a.printKthEle(5);
    // a.printKthEle(1);
    // a.printKthEle(0);
    // a.printKthEle(10);


    return 0;
}