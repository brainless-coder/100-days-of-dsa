#include<iostream>
using namespace std;

struct node {
    int data;
    node * next;
};

class LinkedList {
    private:
        node *head, *tail;
        int size;

    public:
        LinkedList() {
            head = NULL;
            tail = NULL;
            size = 0;
        }

        void print() {
            node * temp = head;

            while (temp != NULL) {
                cout << temp -> data;
                if (temp->next == NULL) {
                    cout << endl;
                } else {
                    cout << " --> ";
                }

                temp = temp -> next;
            }
        }

        void addAtBack(int val) {
            node *temp = new node;
            temp->data = val;
            temp->next = NULL;

            if (head == NULL) {
                head = tail = temp;
            } else {
                tail->next = temp;
                tail = temp;
            }

            size++;
        }  

        void addAtFront(int val) {
            node *temp = new node;
            temp->data = val;
            temp->next = NULL;

            if (head == NULL) {
                head = tail = temp;
            } else {
                temp->next = head;
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
                node *temp = head;
                for (int i = 0; i < index-1; ++i, temp = temp->next);

                node *new_node = new node;
                new_node->data = val;
                new_node->next = temp->next;
                temp->next = new_node;
                size++;
            }
        }

        void printKthElement(int index) {
            if (index > size || index < 0) {
                cout << "Index out of bounds\n";
                return;
            }

            node *temp = head;
            for (int i = 0; i < index; ++i, temp = temp->next);
            cout << temp->data << endl;
        }

        void deleteKthElement(int index) {
            if (index > size || index < 0) {
                cout << "Index out of bounds\n";
                return;
            }

            node *prev, *curr = head;

            if (index == 0) {
                head = curr->next;
                free(curr);
                size--;
                return;
            }

            for (int i = 0; i < index; ++i) {
                prev = curr;
                curr = curr -> next;
            }

            prev->next = curr->next;
            free(curr);
            size--;

            if (index == size) {
                tail = prev;
            }
        }

        void reverse() {
            node *prev = NULL, *curr = head;

            while (curr != NULL) {
                node *temp = curr -> next;
                curr -> next = prev;
                prev = curr;
                curr = temp;
            }

            swap(head, tail);
        }

        node * getHead() {
            return head;
        }

        void merge(node *b_head) {
            if (head == NULL) {
                head = b_head;
                return;
            }

            if (b_head == NULL) {
                return;
            }

            node *temp_head, *temp_tail;

            if (head -> data <= b_head -> data) {
                temp_head = head;
                temp_tail = head;
                head = head -> next;
            } else {
                temp_head = b_head;
                temp_tail = b_head;
                b_head = b_head -> next;
            }

            while (head != NULL && b_head != NULL) {

                if (head->data <= b_head->data) {
                    temp_tail -> next = head;
                    head = head -> next;
                } else {
                    temp_tail -> next = b_head;
                    b_head = b_head -> next;
                }

                temp_tail = temp_tail -> next;
            }

            if (head == NULL) {
                temp_tail -> next = b_head;
            } else {
                temp_tail -> next = head;
            }

            head = temp_head;
        }

        int getSize() {
            return size;
        }
};

int main() {
    LinkedList a;
    LinkedList b;

    // a.addAtBack(5);
    // a.addAtBack(3);
    // a.addAtBack(8);
    // a.addAtBack(2);
    // a.addAtFront(10);
    // a.addAtFront(12);
    // a.addAtFront(1);
    // a.addAtIndex(2, 100);
    // a.addAtIndex(5, -1);
    // a.addAtIndex(1, 34);

    a.addAtBack(2);
    a.addAtBack(9);
    a.addAtBack(20);
    a.print();

    b.addAtBack(3);
    b.addAtBack(200);
    b.addAtBack(300);
    b.print();

    a.merge(b.getHead());
    b.print();
    a.print();
    cout << endl;
    b.merge(a.getHead());
    b.print();
    a.print();

    return 0;
}