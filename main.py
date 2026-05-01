import streamlit as st
import random
import time
#Logo
st.logo("Logo.png",size="large")
#Header
st.header("Rock-Paper-Scissor",text_alignment="center")

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
    if st.button('**Rock**',key=1, width=600, icon='🪨'):
            user_choice=1
    if st.button('**Paper**',key=2, width=600, icon='📄'):
            user_choice=2
    if st.button('**Scissor**',key=3,width=600, icon='✂️'):
            user_choice=3
    if st.button('**Restart**',key=4,width=600, icon='🔄'):
            st.session_state.clear()
            st.rerun()

#Delay effect
if user_choice in [1,2,3]:
    winner.subheader("Deciding...")
    time.sleep(2)

#User & computer score
if 'user_score' not in st.session_state:
    st.session_state.user_score=0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score=0

#fuction for priview user and computer choice
def user_and_computer_choice():
        user_choice_priview.markdown(f':blue-background[**Your Choice**] {dict_for_choice[user_choice]}',text_alignment="center")
        computer_choice_priview.markdown(f':blue-background[**Computer Choice**] {dict_for_choice[computer_choice]}',text_alignment="center")
#Game logic
if user_choice:
    if user_choice==computer_choice:
        winner.subheader('Match Draw! 🙃',text_alignment="center")
        user_and_computer_choice()

    elif user_choice==1 and computer_choice==2:
        winner.subheader(':red[Sorry! Computer Win ☹️]',text_alignment="center")
        st.session_state.computer_score+=1
        user_and_computer_choice()
        
    elif  user_choice==1 and computer_choice==3:
        winner.subheader(':green[Hurreh! You Win] 😍',text_alignment="center")
        st.session_state.user_score+=1
        user_and_computer_choice()
        st.balloons()

    elif user_choice==2 and computer_choice==3:
        winner.subheader(':red[Sorry! Computer Win ☹️]',text_alignment="center")
        st.session_state.computer_score+=1
        user_and_computer_choice()

    elif user_choice==2 and computer_choice==1:
        winner.subheader(':green[Hurreh! You Win] 😍',text_alignment="center")
        st.session_state.user_score+=1
        user_and_computer_choice()
        st.balloons()

    elif user_choice==3 and computer_choice==1:
        winner.subheader(':red[Sorry! Computer Win ☹️]',text_alignment="center")
        st.session_state.computer_score+=1
        user_and_computer_choice()

    elif user_choice==3 and computer_choice==2:
        winner.subheader(':green[Hurreh! You Win] 😍',text_alignment="center")
        st.session_state.user_score+=1
        user_and_computer_choice()
        st.balloons()
else:
    winner.markdown(":yellow[**Tap the buttons to begin your fun 🤩**]")

#Scoreboard
st.table(
    {
        "**You**":[st.session_state.user_score],
        "**Computer**":[st.session_state.computer_score],
    },
    hide_index=True
)

#Footer
st.markdown("Built with ❤️ and fueled by ☕️",text_alignment="center")