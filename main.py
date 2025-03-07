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
ITEMS=["battery","bottle","chips","plasticbag"]
I=[]
ANIMATIONS=[]
def draw():
    screen.blit("background",(0,0))
    if game_over:
        pass
    elif game_complete:
        pass
    else:
        for i in I:
            i.draw()
def update():
    global I,current_level
    if len(I)==0:
        I=make_items(current_level)
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
def animate_items(items_to_animate):
    for item in items_to_animate:
        duration=SPEED-current_level
        item.anchor=("center","bottom")
        animation=animate(item,duration=duration,on_finished=handle_gameover,y=HEIGHT)
        ANIMATIONS.append(animation)
def handle_gameover():
    global game_over
    game_over=True
def on_mouse_down(pos):
    for item in I:
        if item.collidepoint(pos):
            if "paper" in item:
                handle_game_complete()
            else:
                handle_gameover()
def handle_game_complete():
    global current_level,FINAL_LEVEL,game_complete,ANIMATIONS,I
    stop_animation(ANIMATIONS)
    if current_level==FINAL_LEVEL:
        game_complete=True
    else:
        current_level+=1
        I=[]
        ANIMATIONS=[]
def stop_animation(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()
def make_items(number_of_extra_items):
    items_to_create=random_items(number_of_extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items
pgzrun.go()