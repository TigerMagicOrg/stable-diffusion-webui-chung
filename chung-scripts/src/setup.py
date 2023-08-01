import os 
from util import filePath

stable_diffusion_file_path = filePath('../../launch.py')
os.system(f'py {stable_diffusion_file_path} --opt-sdp-attention --api')

# Run with CPU: python launch.py --use-cpu all --precision full --no-half --skip-torch-cuda-test --api
# Run with GPU: python launch.py --xformers --api --lowvram --no-half
# Run with GPU: python launch.py --xformers --api --no-half
# Run python .\chung-scripts\src\index.py