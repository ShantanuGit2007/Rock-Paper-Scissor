import streamlit as st
import random
import time

#Header
st.markdown(
    '''
    <center><h4 style="font-family: 'Source Sans', sans-serif; color: red;"><b>Rock-Paper-Scissor</b></h4></center>
    ''',
    unsafe_allow_html=True
)

#variable to pick computer choice
computer_choice=random.randint(1,3)

#Dictonary with value and crossponding Item
dict_for_choice={
    1:'🪨',
    2:'📄',
    3:'✂️'
}

#Variable to detact winner
st.divider()
winner=st.empty()
colll1,colll2=st.columns([1,1])
with colll1:
    user_choice_priview=st.empty()
with colll2:
     computer_choice_priview=st.empty()
st.divider()

#Set deafult user value
user_choice=None

#All buttons
col1,col2,col3=st.columns([1,2,1])
with col2:
    if st.button('Rock   ',key=1, width=600, icon='🪨'):
            user_choice=1
    if st.button('Paper  ',key=2, width=600, icon='📄'):
            user_choice=2
    if st.button('Scissor',key=3,width=600, icon='✂️'):
            user_choice=3
    if st.button('Rematch',key=4,width=600, icon='🔄'):
            st.session_state.clear()
            st.rerun()

#Delay effect
if user_choice in [1,2,3]:
    winner.title("Deciding...")
    time.sleep(2)

#User & computer score
if 'user_score' not in st.session_state:
    st.session_state.user_score=0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score=0

#fuction for priview user and computer choice
def user_and_computer_choice():
        user_choice_priview.write(f'Your Choice: {dict_for_choice[user_choice]}')
        computer_choice_priview.write(f'Computer choice: {dict_for_choice[computer_choice]}')
#Game logic
if user_choice:
    if user_choice==computer_choice:
        winner.title('Match Draw!')
        user_and_computer_choice()

    elif user_choice==1 and computer_choice==2:
        winner.title('Sorry! Computer Won')
        st.session_state.computer_score+=1
        user_and_computer_choice()
        
    elif  user_choice==1 and computer_choice==3:
        winner.title("Hurreh! You Win")
        st.session_state.user_score+=1
        user_and_computer_choice()
        st.balloons()

    elif user_choice==2 and computer_choice==3:
        winner.title('Sorry! Computer Won')
        st.session_state.computer_score+=1
        user_and_computer_choice()

    elif user_choice==2 and computer_choice==1:
        winner.title("Hurreh! You Win")
        st.session_state.user_score+=1
        user_and_computer_choice()
        st.balloons()

    elif user_choice==3 and computer_choice==1:
        winner.title('Sorry! Computer Won')
        st.session_state.computer_score+=1
        user_and_computer_choice()

    elif user_choice==3 and computer_choice==2:
        winner.title("Hurreh! You Win")
        st.session_state.user_score+=1
        user_and_computer_choice()
        st.balloons()

#Scoreboard
with st.container(border=True):
    coll1,coll2=st.columns([1,1])
    with coll1:
        st.markdown(
            '''
            <h3><u>Your score</u></h3>
            ''',
            unsafe_allow_html=True
        )
        st.subheader(st.session_state.user_score)

    with coll2:
        st.markdown(
            '''
            <h3><u>Computer Score</u></h3>
            ''',
            unsafe_allow_html=True
        )
        st.subheader(st.session_state.computer_score)

#Footer
st.markdown('''
<center><p> "Built With ❤️ and fueled by ☕️" </p></center>
''',
unsafe_allow_html=True)