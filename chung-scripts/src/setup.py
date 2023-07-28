import os 
from util import filePath

stable_diffusion_file_path = filePath('../../launch.py')
os.system(f'py {stable_diffusion_file_path} --opt-sdp-attention --api')

# Run with CPU: --use-cpu all --precision full --no-half --skip-torch-cuda-test --share=True