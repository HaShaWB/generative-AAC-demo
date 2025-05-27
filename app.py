# app.py

import os

import streamlit as st

from gAAC import keyword_to_prompt, prompt_to_image
from typing import Any
from io import BytesIO


def generate_prompt(keyword):
    """
    Generate a prompt based on the input keyword.
    """
    return keyword_to_prompt(keyword)


def generate_image(prompt: Any) -> list[BytesIO]:
    """
    Generate a list of images based on the input prompt.

    Args:
        prompt (Any): 입력 프롬프트

    Returns:
        list[BytesIO]: 생성된 이미지 리스트
    """
    return prompt_to_image(prompt)


st.title("gAAC: Generative AAC Demo")

st.header("Demo Page")
st.text("생성할 Keyword를 입력하세요.")


# Input for keyword
keyword = st.text_input("Enter a keyword to generate an image:")

# Button to generate image
generate_button = st.button("Generate Image")

prompt_placeholder = st.container(height=100)
image_placeholder = st.container(height=300)

if generate_button and keyword:
    print(f"DEBUG: Generating image for keyword: {keyword}")
    

    with st.spinner("Generating Prompt..."):
        prompt = generate_prompt(keyword)
        prompt_placeholder.write(prompt)

    with st.spinner("Generating Image..."):
        images = generate_image(prompt)
        with image_placeholder.container():
            n_of_img = len(images)
            
            cols = st.columns(n_of_img)
            for i, img in enumerate(images):
                cols[i].image(img, width=200)


st.header("Settings")


anthropic_api_key = st.text_input("Anthropic API Key", type="password", key="anthropic_api_key")
genai_api_key = st.text_input("GenAI API Key", type="password", key="genai_api_key")


if anthropic_api_key:
    if anthropic_api_key == os.environ["DEBUG_KEY"]:
        os.environ["ANTHROPIC_API_KEY"] = os.environ["D_ANTHROPIC_API_KEY"]
        os.environ["GENAI_API_KEY"] = os.environ["D_GENAI_API_KEY"]
    else:
        os.environ["ANTHROPIC_API_KEY"] = anthropic_api_key

if genai_api_key:
    if genai_api_key == os.environ["DEBUG_KEY"]:
        os.environ["ANTHROPIC_API_KEY"] = os.environ["D_ANTHROPIC_API_KEY"]
        os.environ["GENAI_API_KEY"] = os.environ["D_GENAI_API_KEY"]
    else:
        os.environ["GENAI_API_KEY"] = genai_api_key