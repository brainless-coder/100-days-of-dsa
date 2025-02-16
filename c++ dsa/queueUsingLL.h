template<typename T>
class Node {
    public:

    T data;
    Node<T> *next;

    Node(T data) {
        this->data = data;
        next = NULL;
    }
};

template<typename T>
class QueueUsingLL {
    Node<T> *head, *tail;
    int size;

    public:

    QueueUsingLL() {
        head = tail = NULL;
        size = 0;
    }

    int getSize() {
        return size;
    }

    bool isEmpty() {
        return size == 0;
    }

    void enqueue(T ele) {
        Node<T> *temp = new Node<T>(ele);

        if (head == NULL) {
            head = tail = temp;
        } else {
            tail->next = temp;
            tail = temp;
        }
        size++;
    }

    T front() {
        if (head == NULL) {
            cout << "Queue Empty !";
            return 0;
        }
        return head->data;
    }

    T dequeue() {
        if (head == NULL) {
            cout << "Queue Empty !";
            return 0;
        }
        T ans = head->data;
        Node<T> *temp = head;
        head = head->next;
        delete temp;
        size--;
        return ans;
    }

};