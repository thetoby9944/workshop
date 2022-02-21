from pathlib import Path

import streamlit as st
import numpy as np
import PIL
from PIL import Image
import plotly.express as px
from pydantic import BaseModel


"# Image Processing Workshop"

st.image("image.jpg")


"## Path Processing"

path = Path("image.jpg")
path

path = path.resolve()
path

path = path.parent
path

path = path / "image.jpg"
path

path_list = list(path.parent.rglob("*.jpg"))
path_list



"## Image Processing"

img = Image.open(path)
st.image(img)

img = img.convert("L")
st.image(img)


patch_size = int(st.number_input("path size", 0, 100, 100))


img = np.asarray(img)
orig_img = img
img[0:patch_size, 0:patch_size] = 0

img = Image.fromarray(img)

img_stack = np.stack([img, orig_img])

fig = px.imshow(img_stack, facet_col=0)
st.plotly_chart(fig)

st.image(img)



