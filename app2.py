import streamlit as st
from PIL import Image
import IPython.display as ipd

def main():        
        st.title("SightSync Harmony")
        disclaimer_message = """This is an object detector model so preferably use images containing different objects, tools... for best results 🙂."""

        st.write("")
        with st.expander("Disclaimer ⚠️", expanded=False):
            st.markdown(disclaimer_message)

        uploaded_image = st.file_uploader("Choose an image ...", type=["jpg", "jpeg", "png"])

        if uploaded_image is not None:
            st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)

            image = Image.open(uploaded_image)
            width, height = image.size
            st.write("Image Dimensions:", f"{width}x{height}")

if __name__ == "__main__":
    main()
    