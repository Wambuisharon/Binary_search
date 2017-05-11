class BinarySearch(list):
    length = 0

    def __init__(self, a, b):
        current = b
        self.append(current)
        for n in range(1, a):
            current += b
            self.append(current)
        self.length = len(self)

    def search(self, value):
        result = {"count": 0, "index": 0}
        temp = self
        index = 0

        while len(temp) > 1:
            if temp[len(temp) - 1] == value:
                if len(temp) == len(self):
                    index = len(temp) - 1
                else:
                    index += len(temp) - 1
                break
            elif temp[0] == value:
                index += 0
                break
            result.update({"count": result.get("count") + 1})
            middle = int(len(temp) / 2)
            if temp[middle] <= value:
                index += - int(middle / 2)
                temp = temp[middle:]
            else:
                index += middle
                temp = temp[:middle]

        result.update({"index": index})
        return result