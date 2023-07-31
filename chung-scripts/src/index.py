from util.common import generate_next_index
from util.stable_diffusion import generate_image

next_index = generate_next_index()

prompt = 'perfume on table'
negative_prompt = "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime), text, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, BadDream, UnrealisticDream"
sampler = "DPM++ SDE Karras"
check_point_name = "realisticVisionV50_v50VAE"
cfg_scale = 7
steps = 20
seed = -1
clip_skip = 2
generate_image(prompt=prompt, negative_prompt=negative_prompt, sampler=sampler, check_point_name=check_point_name, cfg_scale=cfg_scale,steps=steps, seed=seed,clip_skip=2,temp_file_index=next_index)

