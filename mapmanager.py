# напиши здесь код создания и управления картой
class Mapmanager():
    def init(self):
        self.startNew()
        self.model = 'block' # модель кубика лежит в файле block.egg
        self.texture = 'block.png'         
        self.colors = [
            (0.2, 0.2, 0.35, 1),
            (0.2, 0.5, 0.2, 1),
            (0.7, 0.2, 0.2, 1),
            (0.5, 0.3, 0.0, 1)
        ] #rgba
        # создаём основной узел карты:



    def startNew(self):
        self.land = render.attachNewNode("Land") # узел, к которому привязаны все блоки карты


    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]

    def addBlock(self, position):
        # создаём строительные блоки
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getColor(int(position[2]))
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

        self.block.setTag('at', str(position))

        self.block.reparentTo(self.land)

    def clear(self):
        self.land.removeNode
        self.startNew()


    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1
        return x,y



        def findBlocks(self, pos):
            return self.land.findeAllMatches('=at', str(pos))



        def isEmpty(self, pos):
            blocks = self.findBlocks(pos)
            if block:
                return False
            return True


        def findHighestEmpty(self, pos):
            x, y, z = pos
            z = 1
            while not self.isEmpty((x, y, z)):
                z += 1
            return(x, y, z)

        def delBlock(self, position):
            blocks = self.findBlocks(position)
            for block in blocks:
                block.removeNode


        def buildBlock(self, pos):
            x, y, z = pos
            new = self.findHighestEmpty(pos)
            if new [2] <= z + 1:
                self.addBlock(new)


        def delBlockFrom(self, position):
            x, y, z = pos
            pos = x, y, z - 1
            blocks = self.findBlocks(pos)
            for block in blocks:
                block.removeNode()