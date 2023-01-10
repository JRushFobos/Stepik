class Graph:
    def set_data(self, data):
        self.data = data

    def draw(self):
        self.LIMIT_Y = [0, 10]
        num = ''
        for i in self.data:
            if i >= self.LIMIT_Y[0] and i <= self.LIMIT_Y[1]:
                num += str(i) + ' '
        print(num)


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
