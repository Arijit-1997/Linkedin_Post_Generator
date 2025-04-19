import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Streamlit page config
st.set_page_config(page_title="LinkLens", page_icon="🔍")

# Dropdown options
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]
tone_options = ["Professional", "Casual", "Inspirational", "Storytelling"]

def main():
    st.markdown("## 🔍 LinkLens: Generate and Understand LinkedIn Content")
    st.markdown("Craft engaging posts based on topic, language, length, and tone in seconds!")

    # Optional: Let user input their GROQ API key
    # groq_key = st.text_input("🔐 Enter your GROQ API Key", type="password")
    # if groq_key:
    #     os.environ["GROQ_API_KEY"] = groq_key

    # Create three columns for input dropdowns
    col1, col2, col3, col4 = st.columns(4)
    fs = FewShotPosts()
    tags = fs.get_tags()

    with col1:
        selected_tag = st.selectbox("📌 Topic", options=tags)

    with col2:
        selected_length = st.selectbox("📝 Length", options=length_options)

    with col3:
        selected_language = st.selectbox("🌐 Language", options=language_options)

    with col4:
        selected_tone = st.selectbox("🎭 Tone", options=tone_options)

    st.markdown("---")

    # Generate button
    if st.button("🚀 Generate LinkedIn Post"):
        with st.spinner("Generating your post..."):
            post = generate_post(selected_length, selected_language, selected_tag, selected_tone)

        st.markdown("### ✨ Generated LinkedIn Post")
        st.code(post, language="markdown")

        st.download_button(
            label="📋 Download Post",
            data=post,
            file_name="linkedin_post.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
