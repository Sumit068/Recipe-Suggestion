import streamlit as st
import io
from PIL import Image
import recipe_suggestion as recipe

def main():
    st.title('Recipe Suggestion',False)
    with st.sidebar:
        # Settings
        st.title('Menu')
        app_mode = st.selectbox('Choose the App mode', ['Recipe Sugesstion', 'About'])
    if app_mode == 'Recipe Sugesstion':
        img_data = None
        with st.sidebar:
            st.markdown('---')
            # read drag/selected file
            data = st.file_uploader("Upload a Image", type=[".png", '.jpg', '.jpeg'])
            if data is not None:
                img_data = data.getvalue()
        if img_data is not None:
            # predict vegetables and generate recipe
            result = recipe.suggestion(Image.open(io.BytesIO(img_data)))
            # print image on screen
            st.image(img_data)
            # print recipe
            st.write(result)
    elif app_mode == 'About':
        st.header('About App',False)
        st.markdown('This is Recipe Suggestion Application where user can upload images of Vegetables and it wiil suggestion recipe based on identify vegetables on given image.')
        st.markdown('''I am Sumit Pal Singh, a Machine Learning Enthuiast. you can follow me.  
                    Linkedin : https://www.linkedin.com/in/sumit-pal-singh-233639217/
                    ''')
if __name__ == '__main__' :
    try :
        main()
    except SystemExit :
        pass