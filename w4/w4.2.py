class ReverseIter:
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        self.next_item = len(self.collection)
        return self

    def __next__(self):
        if self.next_item > 0:
            current_item = self.next_item
            self.next_item -= 1
            return current_item
        else:
            raise StopIteration
