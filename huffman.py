import heapq

class BinaryTreeNode:
    def __init__(self, value, freq) -> None:
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

class HuffmanCoding:
    def __init__(self, path) -> None:
        self.path = path
        self.__heap = []

    def __makeFreqDict(self, text):
        freqDict = {}
        for char in text:
            freqDict[char] = freqDict.get(char, 0) + 1
        return freqDict

    def __buildHeap(self, freqDict):
        for key in freqDict:
            pass

    def compress(self):
        # get the file from path
        # read text from file
        text = "asdlkfjslrijwensdsldkfjslkfj"

        # make frequency dictionary using the text
        freqDict = self.__makeFreqDict(text)

        # construct heap from the freq dictionary
        self.__buildHealp(freqDict)
        # make tree from the heap

        # construct the codes from binary tree

        # create the encoded text using the codes
    
        # put this encoded text into the binary file
    
        # return this binary file as output

        pass