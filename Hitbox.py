
class Hitbox:    
    def __init__(
        useless,
        hitbox_x,
        hitbox_x2,
        hitbox_y,
        hitbox_y2,
        mousex,
        mousey
    ):
        Hitbox.oof(
            hitbox_x,
        hitbox_x2,
        hitbox_y,
        hitbox_y2,
        mousex,
        mousey)

    def isCollide(
        hitbox_x,
        hitbox_x2,
        hitbox_y,
        hitbox_y2,
        mouseX,
        mouseY,
        
    ):
        #print(mouseX,hitbox_x,mouseX,hitbox_x2,mouseY,hitbox_y,mouseY,hitbox_y2,"      <--")
        #605 420 605 800                                 288 538 288 730       <--
        if (mouseX > hitbox_x and mouseX < hitbox_x2 and mouseY> hitbox_y and mouseY<hitbox_y2):
            
            return (True)
        else:
            return(False)













    
    