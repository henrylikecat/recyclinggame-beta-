import pgzrun,random
WIDTH=1100
HEIGHT=800
CENTER_X=WIDTH/2
CENTER_Y=HEIGHT/2
CENTER=(CENTER_X,CENTER_Y)
FINAL_LEVEL=10
SPEED=10
game_over=False
game_complete=False
current_level=1
ITEMS=["battery","bottle","chips","plasticbags"]
def draw():
    screen.blit("background",(0,0))
def update():
    pass
def random_items(number_of_extra_items):
    items_to_create=["paper"]
    for i in range(0,number_of_extra_items):
        random_item=random.choice(ITEMS)
        items_to_create.append(random_item)
    return items_to_create
def create_items(items_to_create):
    new_items=[]
    for i in items_to_create:
        item=Actor(i)
        new_items.append(item)
    return new_items
def layout_items(items_to_layout):
    number_of_gaps=len(items_to_layout)+1
    gap_size=WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index,item in enumerate(items_to_layout):
        new_x_pos = (index + 1) *gap_size
        item.x = new_x_pos
pgzrun.go()