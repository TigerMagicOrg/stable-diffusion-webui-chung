from util.common import generate_next_index
from util.stable_diffusion import generate_image

next_index = generate_next_index()

prompt = 'photo of the warrior Aragorn from Lord of the Rings, film grain'
negative_prompt = "BadDream, (UnrealisticDream:1.2)"
sampler = "DPM++ SDE Karras"
model = "absolutereality_v16.safetensors [be1d90c4ab]"
cfg_scale = 4
steps = 20
seed = 1988487711
clip_skip = 2
generate_image(prompt=prompt, negative_prompt=negative_prompt, sampler=sampler, model=model, cfg_scale=cfg_scale,steps=steps, seed=seed,clip_skip=2,temp_file_index=next_index)

