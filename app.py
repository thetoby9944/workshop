from pathlib import Path

import streamlit as st
import numpy as np
import PIL
from PIL import Image
import plotly.express as px
from pydantic import BaseModel


"# Image Processing Workshop"

st.image("image.jpg")

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




