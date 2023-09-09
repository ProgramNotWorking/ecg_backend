import io
import json

import requests
from PIL import Image

name = "Aleksey"
pulse = 5201233
graph_x = '12, 9, 871, 4'
graph_y = '59, -1, 78, 1000'

data = {
    'patient_name': name,
    'graph_x': graph_x,
    'graph_y': graph_y,
    'pulse': pulse
}

resp = requests.post(
    'http://localhost:8000/new-ecg',
    data=json.dumps(data),
    stream=True
)

print(resp.content)

image = Image.open(io.BytesIO(resp.content))
image.show()
