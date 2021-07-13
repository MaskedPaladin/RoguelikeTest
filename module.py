import random, sys

class Item:
    def __init__(self, name, position):
        self.name = name
        self.position = position
class Entity:
    def __init__(self, name, position, entity_type, icon):
        self.name = name
        self.position = position
        self.entity_type = entity_type
        self.icon = icon
class DataMap:
    def __init__(self, w, h, items, entities):
        self.w = w
        self.h = h
        self.items = items
        self.entities = entities
    def generate_map(self):
        arraymap=[]
        for i in range(self.h):
            arraymap.extend("\n")
            for j in range(self.w):
                if i == 0:
                    arraymap.extend("#")
                elif i == self.h-1:
                    arraymap.extend("#")
                elif j !=0 and j != self.w-1:
                    arraymap.extend("·")
                else:
                    arraymap.extend("#")
        for i in range(len(self.entities)):
            if self.entities[i].position in range(self.w*self.h):
                arraymap[self.entities[i].position]=self.entities[i].icon
        print(self.w, self.h)
        return arraymap
    def update(self):
        pass
class GameController:
    def __init__(self):
        pass
    def initialize_items(n):
        items = []
        for i in range(n):
            items.append(Item(None, None))
        return items
    def generate_items(itemlist, n, size):
        charlist = "abcdefghijklmnñopqrstuvwxyz"
        for i in range(n):
            name = ""
            position = random.randint(0,size)
            length = random.randint(4,12)
            for j in range(length):
                value = random.choice(charlist)
                name=name+value
            itemlist[i].name=name
            itemlist[i].position=position
    def initialize_entities(n):
        entities = []
        for i in range(n):
            entities.append(Entity(None, None, None, None))
        return entities
    def generate_entities(entitylist, n, size):
        charlist = "abcdefghijklmnñopqrstuvwxyz"
        entity_type = "Player"
        for i in range(n):
            if i > 0:
                entity_type="Other"
            name = ""
            position = random.randint(0,size)
            length = random.randint(4,12)
            for j in range(length):
                value = random.choice(charlist)
                name=name+value
            entitylist[i].name=name
            entitylist[i].position=position
            entitylist[i].entity_type=entity_type
            if entity_type=="Player":
                entitylist[i].icon="@"
            else:
                entitylist[i].icon="m"
class MapRender(DataMap):
    def __init__(self, w, h, items, entities):
        super().__init__(w, h, items, entities)
    def print_items(self, separator=""):
        for i in range(len(self.items)):
            print(str(separator)+" "+str(self.items[i].__dict__))
    def print_entities(self, separator=""):
        for i in range(len(self.entities)):
            print(str(separator)+" "+str(self.entities[i].__dict__))
    def draw_map(self, g_map):
        for i in range(len(g_map)):
            if i=="\n":
                print()
            sys.stdout.write(str(g_map[i]))
            
if __name__=="__main__":
    pass