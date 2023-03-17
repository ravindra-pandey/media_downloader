"""
In this page we will use our scrapper module and gather 
all images after whic we will download all images from the webpage.
"""

import io
import time
import zipfile
import requests
import streamlit as st
from scrapper import Scrapper


def get_all_images(url):
    """
    this function gather all the images from in the webpage.
    """
    scrap = Scrapper(url)
    links = scrap.read_all_links()
    gathered_images = []
    for link in links:
        try:
            gathered_images.append(requests.get(link, timeout=0.5).content)
        except Exception as error:
            print(error)
    return gathered_images


IMAGES = None

st.header("Download media from any webpage")
with st.form("my form"):
    gather_url = st.text_input("Enter the link here")
    submitted = st.form_submit_button("fetch media")

    if submitted:
        IMAGES = get_all_images(gather_url)


def figs_to_zip(images) -> bytes:
    """THIS WILL BE RUN ON EVERY SCRIPT RUN"""
    zip_buf = io.BytesIO()
    with zipfile.ZipFile(file=zip_buf, mode='w', compression=zipfile.ZIP_DEFLATED) as z_f:
        for i, image in enumerate(images):
            filename = f'{i}.svg'
            z_f.writestr(zinfo_or_arcname=filename, data=image)
    buf = zip_buf.getvalue()
    zip_buf.close()
    return buf


placeholder = st.empty()
if IMAGES is not None:
    with placeholder:
        st.download_button(label='Download images', data=figs_to_zip(
            IMAGES), file_name=f'{time.time()}.zip')



