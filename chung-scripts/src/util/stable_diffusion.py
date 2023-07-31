import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
from .common import absoluteFilePath

check_points = [
  {
    "title": "v1-5-pruned-emaonly.safetensors [6ce0161689]",
    "model_name": "v1-5-pruned-emaonly",
    "hash": "6ce0161689",
    "sha256": "6ce0161689b3853acaa03779ec93eafe75a02f4ced659bee03f50797806fa2fa",
    "filename": "D:\\Dev\\Projects\\stable-diffusion-webui-chung\\models\\Stable-diffusion\\v1-5-pruned-emaonly.safetensors",
    "config": "D:\\Dev\\Projects\\stable-diffusion-webui-chung\\models\\Stable-diffusion\\v1-5-pruned-emaonly.yaml"
  },
  {
    "title": "v2-1_768-ema-pruned.ckpt [ad2a33c361]",
    "model_name": "v2-1_768-ema-pruned",
    "hash": "ad2a33c361",
    "sha256": "ad2a33c361c1f593c4a1fb32ea81afce2b5bb7d1983c6b94793a26a3b54b08a0",
    "filename": "D:\\Dev\\Projects\\stable-diffusion-webui-chung\\models\\Stable-diffusion\\v2-1_768-ema-pruned.ckpt",
    "config": "D:\\Dev\\Projects\\stable-diffusion-webui-chung\\models\\Stable-diffusion\\v2-1_768-ema-pruned.yaml"
  },
  {
    "title": "absolutereality_v16.safetensors [be1d90c4ab]",
    "model_name": "absolutereality_v16",
    "hash": "be1d90c4ab",
    "sha256": "be1d90c4abb7bb0183f267f899f38b44112ad6ef9a757a6723514ea4e9be15dc",
    "filename": "D:\\Dev\\Projects\\stable-diffusion-webui-chung\\models\\Stable-diffusion\\absolutereality_v16.safetensors",
    "config": "D:\\Dev\\Projects\\stable-diffusion-webui-chung\\models\\Stable-diffusion\\absolutereality_v16.yaml"
  },
  {
    "title": "realisticVisionV50_v40VAE.ckpt [035430afae]",
    "model_name": "realisticVisionV50_v50VAE",
    "hash": "035430afae",
    "sha256": "035430afae9634d904fdd57a2a23bb4f8162688c48dd7258ce885831b84df198",
    "filename": "D:\\Dev\\Projects\\stable-diffusion-webui-chung\\models\\Stable-diffusion\\realisticVisionV50_v40VAE.ckpt",
    "config": "D:\\Dev\\Projects\\stable-diffusion-webui-chung\\models\\Stable-diffusion\\realisticVisionV50_v40VAE.yaml"
  }
]

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

def load_check_point(ck_name):
    api_url = f'{url}/sdapi/v1/options'
    payload = {
        "sd_model_checkpoint": ck_name
    }
    response = requests.post(url=api_url, json=payload)

def generate_image(prompt, negative_prompt, sampler, check_point_name, cfg_scale, steps, seed, clip_skip, temp_file_index):
    load_check_point(check_point_name)
    api_url = f'{url}/sdapi/v1/txt2img'
    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "sampler_index": sampler,
        "cfg_scale": cfg_scale,
        "steps": steps,
        "seed": seed,
        "width": 640,
        "height": 960,
        "clip_skip":clip_skip,
        "denoising_strength": 0.35,
        # "enable_hr": True,
        # "hr_scale": 2,
        # "hr_upscaler": "4x-UltraSharp",
        # "eta": 31337,
        # "restore_faces": False,
        # "settings/Do not make DPM++ SDE deterministic across different batch sizes./visible": True,
    }

    response = requests.post(url=api_url, json=payload)

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




