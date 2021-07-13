from typing import MappingView
from module import *

main = GameController
itemlist = main.initialize_items(2)
entitylist = main.initialize_entities(3)

mapw=10
maph=10


map = MapRender(mapw, maph, itemlist, entitylist)
map.update()
main.generate_items(itemlist, len(itemlist), 3)
main.generate_entities(entitylist, len(entitylist), mapw*maph)
g_map = map.generate_map()
map.print_items("Items")
map.print_entities("Entities")
map.draw_map(g_map)