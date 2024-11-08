import turtle
import time

# IMAGES
ball_location = "./images/Ball_50"
groundskwish = [f"{ball_location}/ball_chubb_0.gif", f"{ball_location}/ball_chubb_1.gif", f"{ball_location}/ball_chubb_2.gif"]

dust         = "./images/dust.gif"

bgpic_out      = "./images/PIT/PIT_OUTSIDE.gif"
pit_out_block  = "./images/PIT/PIT_OUTSIDE_BLOCK.gif"

bgpic_in      = "./images/PIT/PIT_INSIDE.gif"
pit_in_block  = "./images/PIT/PIT_INSIDE_BLOCK.gif"

airdust      = f"{ball_location}/takeoff_small_00.gif"


max_ball_frames = 90
ballFrames = [None] * max_ball_frames
for i in range (0,max_ball_frames):
    ballFrames[i] = f"{ball_location}/ball_" + str(i) + ".gif"

# Motion paramet ers
def get_gravity(pg):
    print((pg/moon_grav)*g_factor)
    return (pg/moon_grav)*g_factor

g_factor = -0.09
moon_grav = 1.62
earth_grav = 9.807
mars_grav = 3.71
y_velocity   = 2  # pixels/(time of iteration)
x_velocity   = 1  # pixels/(time of iteration)
energy_loss  = 0.75
slow_animation = 0.05

gravity      = get_gravity(moon_grav)  # pixels/(time of iteration)^2
#gravity      = get_gravity(earth_grav)  # pixels/(time of iteration)^2
#gravity      = get_gravity(mars_grav)  # pixels/(time of iteration)^2

# Window Size
width  = 1024
height = 768
forward = True

# Ball rotation
ball_idx = len(ballFrames)-1

def ball_turn():
    global ball_idx
    if forward == False:
        ball_idx -= 1
        if ball_idx == -1:
            ball_idx = len(ballFrames)-1
        ball.shape(ballFrames[ball_idx])
    else:
        ball_idx += 1
        if ball_idx == len(ballFrames):
            ball_idx = 0
        ball.shape(ballFrames[ball_idx])

def ground_dust():
    pass
#    liftoff.goto(ball.xcor(), ball.ycor()-20)
#    liftoff.st()
#    window.update()
#    liftoff.ht()
#    window.update()

# Liftoff
def liftoff_animate(y_vel, top=height/4, show_ground_dust=True):
    y_velocity = y_vel
    
    if show_ground_dust:
        ground_dust()

    ball.sety(ball.ycor() + y_velocity)
    ball.setx(ball.xcor() + x_velocity)
    window.update()

    # y_velocity = 8
    while ball.ycor() <= top :
        airlift.goto(ball.xcor(), ball.ycor()-20)
        airlift.st()
        window.update()
        ball.sety(ball.ycor() + y_velocity)
        ball.setx(ball.xcor() + x_velocity)
        y_velocity -= gravity
        time.sleep(0.1)
        window.update()

    airlift.ht()
    window.update()

# Liftoff
def liftoff_sideays_animate(y_vel, x_vel=2, top=height/4, show_ground_dust=True):
    y_velocity = y_vel
    x_velocity = x_vel
    
    if show_ground_dust:
        ground_dust()

    ball.sety(ball.ycor() + y_velocity)
    ball.setx(ball.xcor() + x_velocity)
    window.update()

    # y_velocity = 8
    while ball.ycor() <= top :
        airlift.goto(ball.xcor(), ball.ycor()-20)
        airlift.st()
        window.update()
        ball.sety(ball.ycor() + y_velocity)
        ball.setx(ball.xcor() + x_velocity)
        y_velocity -= gravity
        time.sleep(0.1)
        window.update()

    airlift.ht()
    window.update()

def set_ball_chubb():
    for img in groundskwish[0::]:
        ball.shape(img)
        window.update()

    time.sleep(slow_animation)

    for img in groundskwish[::-1]:
        ball.shape(img)
        window.update()


def jump_animate(hops, y_vel=y_velocity):
    global shapetime
    global shapetime_max

    y_velocity = y_vel
    while hops:
        ball_turn()
        #print(f"{ball.xcor()}, {ball.ycor()}")
        ball.sety(ball.ycor() + y_velocity)
        ball.setx(ball.xcor() + x_velocity)
        time.sleep(0.05)                            ## CHANGE SPEED HERE
        y_velocity += gravity

        if ball.ycor() < ground:
            y_velocity = -y_velocity * energy_loss
            ball.sety(ground)
            set_ball_chubb()
            hops -= 1
            window.update()
            #time.sleep(0.05)

        window.update()

    ball_turn()
    window.update()
#    print(y_velocity)
#    return y_velocity


def bounce_up(y_vel=y_velocity):
    global shapetime
    global shapetime_max
    y_velocity = y_vel

    while ball.ycor() < ground:
        ball_turn()
        ball.sety(ball.ycor() + y_velocity)
        ball.setx(ball.xcor() + x_velocity)
        time.sleep(0.05)                            ## CHANGE SPEED HERE

        if ball.ycor() >= ground:
            set_ball_chubb()
            window.update()
            time.sleep(0.05)

        y_velocity += gravity
        #print(y_velocity)
        window.update()

def drag_animate(xstop=0):
    y_velocity = 0
    airlift.goto(ball.xcor()-10, ball.ycor())
    airlift.st()
    window.update()
    x_velocity = 10

    instance = 0
    while ball.xcor() < xstop :
        if(x_velocity == 2):
            airlift.goto(ball.xcor()-10, ball.ycor())
            airlift.st()
            window.update()
            x_velocity = 10
        ball.setx(ball.xcor() + x_velocity)
        x_velocity -= 1
        window.update()
        time.sleep(0.1)
        if instance == 2:
            instance = 0
            airlift.ht()
            window.update()
        else:
            instance += 1
    airlift.ht()
    window.update()

if __name__ == "__main__":
    window = turtle.Screen()
    window.setup(width, height)
    window.tracer(0,0)

    for i in range (0, len(groundskwish)):
        window.addshape(groundskwish[i])

    for i in range(0, max_ball_frames):
        window.addshape(ballFrames[i])

    window.addshape(dust)
    window.addshape(airdust)
    window.addshape(pit_out_block)
    window.addshape(pit_in_block)

    window.bgpic(bgpic_out)

    liftoff = turtle.Turtle()
    liftoff.penup()
    liftoff.shape(dust)
    liftoff.ht()

    airlift = turtle.Turtle()
    airlift.penup()
    airlift.shape(airdust)
    airlift.ht()

    ball = turtle.Turtle()
    ball.penup()
    ball.shape(ballFrames[ball_idx])
    ball.st()
    ball.resizemode("user")

    out_block = turtle.Turtle()
    out_block.shape(pit_out_block)
    out_block.st()

    in_block = turtle.Turtle()
    in_block.shape(pit_in_block)
    in_block.ht()
    time.sleep(20)
    while(1):
        ball.goto(-width/2+10, 4)
        ground       = 4
        y_velocity   = 4
        x_velocity   = 1.5
        energy_loss  = 0.5
        jump_animate(hops = 4, y_vel=y_velocity)

        time.sleep(0.5)

        liftoff_animate(10)

        # BIG HOP
        y_velocity   = 4
        x_velocity   = 4
        energy_loss  = 0.5
        jump_animate(hops = 1, y_vel=y_velocity)

        y_velocity   = 4
        x_velocity   = 1
        energy_loss  = 0.5
        jump_animate(hops = 2, y_vel=y_velocity)

        time.sleep(0.5)

        # Turn around
        forward = False
        y_velocity   = 4
        x_velocity   = -1
        energy_loss  = 0.5
        liftoff_animate(10, top=height/20)
        jump_animate(hops = 2, y_vel=y_velocity)

        liftoff_animate(10, top=height/12)

        ground = -height/4

        y_velocity   = 4
        x_velocity   = -1.5
        jump_animate(hops = 1, y_vel=y_velocity)

        ##
        ## Move the stage to inside the pit
        ##        
        window.bgpic(bgpic_in)
        in_block.st()
        out_block.ht()
        ball.goto(250, 150)
        window.update()

        y_velocity   = -2
        x_velocity   = 0
        ground       = -80
        jump_animate(hops = 1, y_vel=y_velocity)

        # Touch Top
        in_block.ht()
        window.update()
        y_velocity   = 7
        x_velocity   = 0.5
        ground       = 180
        bounce_up(y_velocity)

        y_velocity   = -2 
        x_velocity   = -0.5
        ground       = -120
        jump_animate(hops = 1, y_vel=y_velocity)
        in_block.st()

        y_velocity   = 4
        x_velocity   = -2
        ground       = -200
        jump_animate(hops = 3, y_vel=y_velocity)

        time.sleep(3)

        ## Start to come out of pit
        x_velocity = 1.5
        liftoff_sideays_animate(10, 10, top=150)
#        liftoff_animate(10, top=0)
#        drag_animate(xstop=ball.xcor()+400)
#        liftoff_animate(10, top=150, show_ground_dust=False)

        ##
        ## Move the stage to outside the pit again
        ##
        forward = True        
        window.bgpic(bgpic_out)
        in_block.ht()
        out_block.st()
        ball.goto(40, -100)
        window.update()
        x_velocity = 2
        ground = 4
        liftoff_animate(20)

        jump_animate(hops = 4)
