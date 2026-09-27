import streamlit as st
from google import genai


if "page" not in st.session_state:
    st.session_state.page = 1


if st.session_state.page == 1:
    st.title("Manifest")
    st.write("당신이 원하는 현실은 무엇인가요?")

    dream = st.text_area("원하는 현실을 자유롭게 적어보세요" , placeholder='나는 내가 좋아하는 일을 하면서 돈을 벌고싶어..')

    if st.button("시작하기"):
        st.session_state.dream = dream
        st.session_state.page = 2

elif st.session_state.page == 2:
    st.title('당신의 이야기를 조금 더 알아볼게요')
    st.write('그 현실이 이루어진다면' , 
             '당신의 하루는 어떻게 달라져 있을까요?')

    day = st.text_area('미래를 상상해보세요' , placeholder='당신의 달라진 하루를 상상해보세요')

    if st.button('다음'):
        st.session_state.day = day
        st.session_state.page = 3

elif st.session_state.page ==3:
    st.title("당신이 원하는 Manifest 입니다")
    manifest = f"""
    내가 원하는 현실: 
    {st.session_state.dream}

    내가 원하는 하루 : 
    {st.session_state.day}
    """

    st.write(manifest)

    action = st.text_area("그 현실을 만들기 위해 할 수 있는 작은 행동은 뭐가 있을까요?" ,
                          placeholder='예: 그 분야에 대해서 30분 정도 조사해본다' , key = 'action'
                          )

    if st.button("다음"):
        st.session_state.page = 4

elif st.session_state.page == 4 :
    prompt = f"""
    내가 원하는 현실
    {st.session_state.dream}

    내가 원하는 하루
    {st.session_state.day}

    오늘의 작은 행동
    {st.session_state.action}

    이 내용들을 바탕으로 사용자에게 맞춤형 목표를 만들어줘 
    """

    client  = genai.Client(api_key = st.secrets['GEMINI_API_KEY'])
    response = client.models.generate_content(model = 'gemini-3.5-flash-lite' , contents = prompt)

    st.write("🎯 AI가 만든 나의 목표")
    st.write(response.text)

