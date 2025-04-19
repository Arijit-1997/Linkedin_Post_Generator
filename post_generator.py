from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()


def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"


def generate_post(length, language, tag, tone):
    prompt = get_prompt(length, language, tag, tone)

    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"❌ Error generating post: {str(e)}"


def get_prompt(length, language, tag, tone):
    length_str = get_length_str(length)

    prompt = f"""
Your task is to write a compelling LinkedIn post using the following criteria:
- Topic: {tag}
- Length: {length_str}
- Language: {language}
- Tone: {tone}
- The post should start with a hook, contain valuable insight or a personal experience, and end with a call-to-action or a thought-provoking question.

If the language is Hinglish, use a mix of Hindi and English—but always use English script (no Devanagari).
Match the tone to "{tone}"—e.g., a Professional tone is formal and insightful, Storytelling uses personal experiences, Casual is friendly, and Inspirational is motivational.".
"""

    examples = few_shot.get_filtered_posts(length, language, tag, tone)

    if len(examples) > 0:
        prompt += "\n\nHere are a few example posts with similar style:\n"
        for i, post in enumerate(examples[:2]):
            post_text = post['text']
            prompt += f"\nExample {i + 1}:\n{post_text.strip()}\n"

    else:
        prompt += "\n\nUse a conversational, real LinkedIn user tone with practical insights."

    return prompt


# Testing (for development/debugging)
if __name__ == "__main__":
    print(generate_post("Medium", "English", "Mental Health", "Professional"))
