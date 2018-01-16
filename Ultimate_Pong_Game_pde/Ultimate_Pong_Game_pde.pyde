z=60
w=30
velocityY=-9
velocityX=-9
x=200
y=200

def setup():
    size(900,700)
    background(0)
   
def nettoyer():
    
    background(0)
def dessiner():
    
    rect(w,z,25,85)
    smooth()
    ellipse(x,y,20,20)
    line(200,0,200,400)
def bouger():
    global z
    global x
    global y
    global velocityX
    global velocityY
    x = x + velocityX
    y = y + velocityY
    z = mouseY
def rebondir():
    global z
    global x
    global y
    global velocityX
    global velocityY
    if x > width-10 :
        velocityX = -velocityX
    if y > height-10:
        velocityY = -velocityY 
    
    if x < -10 :
        velocityX = -velocityX
    if y < +10 :
        velocityY = -velocityY
        
    if x<w+35 and y>z and y<z+85:
        velocityX= -velocityX
    
    if x< 10:
        noLoop()
        print ("Game Over")
        
def draw():
    nettoyer()
    dessiner()
    bouger()
    rebondir()