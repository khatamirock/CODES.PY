
lf,rt=2,2
st=[]
def mover(step,r,l):

    global st
    st.append(step)  ### appending ,,,,,,,,,,,,,,,,,,
    print(st, end=' \n')

    if r<rt:
        mover('right',r+1,l)

    if l<lf:
        mover('down',r,l+1)
        # st.pop()
        print('|',st[-1],'|\n')

    st.pop() ##### popping thats...... this is backTrack....
str=''
mover('',0,0)


##turtle graphics recursion...................  >>>>>>>>>
import turtle
my_turtle = turtle.Turtle()
my_win = turtle.Screen()
def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.left(90)
        draw_spiral(my_turtle, line_len - 5)
# call....
draw_spiral(my_turtle, 200)
my_win.exitonclick()