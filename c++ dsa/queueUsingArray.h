template<typename T>
class QueueUsingArray {
    T *data;
    int firstIndex, nextIndex, size, capacity;

    public:

    QueueUsingArray() {
        data = new T[5];
        firstIndex = -1;
        nextIndex = 0;
        size = 0;
        capacity = 5;
    }

    ~QueueUsingArray() {
        delete [] data;
    }

    int getSize() {
        return size;
    }

    bool isEmpty() {
        return size == 0;
    }

    void enqueue(T ele) {
        if (size == capacity) {
            T *newData = new T[2*capacity];

            int j = 0;
            for (int i = firstIndex; i < capacity; ++i) {
                newData[j++] = data[i];
            }
            for (int i = 0; i < firstIndex; ++i) {
                newData[j++] = data[i];
            }

            nextIndex = capacity;
            firstIndex = 0;
            delete [] data;
            data = newData;
            capacity *= 2;

        }
        data[nextIndex] = ele;
        nextIndex = (nextIndex + 1) % capacity;
        firstIndex == -1 ? firstIndex = 0: firstIndex;
        size++;
    }

    T front() {
        if (isEmpty()) {
            cout << "Queue Empty ! ";
            return 0;
        }
        return data[firstIndex];
    }

    T dequeue() {
        if (isEmpty()) {
            cout << "Queue Empty ! ";
            return 0;
        }
        T ans = data[firstIndex];
        firstIndex = (firstIndex + 1) % capacity;
        size--;
        if (size == 0) {
            firstIndex = -1;
            nextIndex = 0;
        }
        return ans;
    }

};