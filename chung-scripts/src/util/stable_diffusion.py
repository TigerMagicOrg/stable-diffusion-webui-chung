import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
from .common import absoluteFilePath

check_points = {
    "absolutereality_v16": "absolutereality_v16.safetensors [e948ca5dc4]",
    "realisticVisionV50_v40VAE":"realisticVisionV50_v40VAE.ckpt [035430afae]",
    "v1-5-pruned-emaonly":"v1-5-pruned-emaonly.safetensors [6ce0161689]",
}
sd_default_config = {
    "check_point": "absolutereality_v16.safetensors [e948ca5dc4]",
    "negative_prompt": "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime), text, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, UnrealisticDream",
    "sampler": "Euler",
    "cfg_scale": 6.5,
    "seed": -1,
    "width": 512,
    "height": 512,
    "denoising_strength": 0.35,
    "eta": 31337,
    "restore_faces": False,
}
url = "http://127.0.0.1:7860"

def generate_image(prompt, negative_prompt, sampler, model, cfg_scale, steps, seed, clip_skip, temp_file_index):
    api_url = f'{url}/sdapi/v1/txt2img'
    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "sampler_index": sampler,
        "sd_model_checkpoint": model,
        "cfg_scale": cfg_scale,
        "steps": steps,
        "seed": seed,
        "width": 512,
        "height": 512,
        "clip_skip":clip_skip,
        "denoising_strength": 0.35,
        "eta": 31337,
        "restore_faces": False,
        # "settings/Do not make DPM++ SDE deterministic across different batch sizes./visible": True,
    }

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
        image_path = absoluteFilePath(f'../../images/output_{temp_file_index}.png')
        image.save(image_path, pnginfo=pnginfo)
        print(f'Generated image: {image_path}')




