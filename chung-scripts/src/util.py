import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
import os

cache_index_file = '../cache/index.txt'
url = "http://127.0.0.1:7860"

def filePath(relativePath):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, relativePath)
    return abs_file_path

def generate_next_index():
    f = open(filePath(cache_index_file), "r")
    index_text = f.read()
    next_index = int(index_text) + 1
    f = open(filePath(cache_index_file), "w")
    f.write(str(next_index))
    f.close()
    return next_index

def generate_image(prompt, index):
    api_url = f'{url}/sdapi/v1/txt2img'
    payload = {
        "seed": -1,
        "negative_prompt": "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime), text, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, UnrealisticDream",
        "sd_model_checkpoint": "realisticVisionV50_v40VAE.ckpt [035430afae]",
        "cfg_scale": 6.5,
        "width": 512,
        "height": 512,
        "denoising_strength": 0.35,
    }

    payload["prompt"] = prompt

    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

    r = response.json()

    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image_path = filePath(f'../images/output_{index}.png')
        image.save(image_path, pnginfo=pnginfo)
        print(f'Generated image: {image_path}')




