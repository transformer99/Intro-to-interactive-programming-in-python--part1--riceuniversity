# template for "Stopwatch: The Game"
import simplegui
 
# define global variables
interval = 100
width = 300
height = 200
 
time = 0
count = 0
success = 0
message= ''
isStart = False
 
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global message
    minute = t // 600
    tensecond = (t - minute * 600) // 100
    second = (t - minute * 600 - tensecond * 100) // 10
    minisecond = t % 10
 
    message = str(minute)+":"+str(tensecond)+str(second)+":"+str(minisecond)
    return message
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global isStart 
    isStart = True
    timer.start()
 
def stop():
    timer.stop()
    global isStart, count, success
    if isStart:
        isStart = False
        count += 1
        if time % 10 == 0:
            success +=1   
        
def reset():
    global time, count, success, isStart
    timer.stop()
    time = 0
    count = 0
    success = 0
    isStart = False
    
# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time = time +1
 
# define draw handler
def draw(c):
    global message
    c.draw_text(format(time), (width//2 - width//6, height//2+height // 10), 36, "white")  
    score = str(success)+"/"+str(count)
    c.draw_text(score, (width - width // 5, height // 5), 24, "Green")
    
    
# create frame
frame = simplegui.create_frame("Stopwatch", width, height)
timer = simplegui.create_timer(interval, tick)
 
# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
 
# start frame
frame.start()
 
# Please remember to review the grading rubric
