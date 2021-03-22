# 处理返回的所有基金字符串
class FundStack:
    def __init__(self):
        self.items = []

    # push 压栈
    def push(self, item):
        self.items.append(item)

    # pop 弹出栈
    def pop(self):
        self.items.pop()

    # 获取栈顶元素
    def peek(self):
        if self.size() > 0:
            return self.items[len(self.items) - 1]
        return -1

    # 栈的大小
    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack = FundStack()
    stack.push("[")
    stack.push("[")
    stack.push("start")
