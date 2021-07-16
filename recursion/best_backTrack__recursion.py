
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

    ''' after all we need to retreat to the previous step...... '''
    st.pop() ##### popping thats...... this is backTrack....
str=''


mover('',0,0)
