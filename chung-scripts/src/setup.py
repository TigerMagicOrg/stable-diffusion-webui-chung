import os 
from util import filePath

stable_diffusion_file_path = filePath('../../launch.py')
os.system(f'py {stable_diffusion_file_path} --opt-sdp-attention --api')