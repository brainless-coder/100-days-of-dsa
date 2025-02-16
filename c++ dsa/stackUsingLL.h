template<typename T>
struct Node {
    T data;
    Node<T> *next;

    Node(T data) {
        this->data = data;
        next = NULL;
    }
};

template<typename T>
class StackUsingLL {
    Node<T> *head;
    int totalSize;


    public:

    StackUsingLL() {
        head = NULL;
        totalSize = 0;
    }

    int size() {
        return totalSize;
    }

    bool isEmpty() {
        return totalSize == 0;
    }

    void push(T x) {
        Node<T> *temp = new Node<T>(x);

        temp->next = head;
        head = temp;
        totalSize++;
    }

    T pop() {
        if (head == NULL) {
            return -1;
        }

        T deletedEle = head->data;
        Node<T> *temp = head;
        head = head->next;
        delete temp;
        totalSize--;
        return deletedEle;
    }

    T top() {
        if (isEmpty()) {
            return -1;
        }
        return head->data;
    }

};