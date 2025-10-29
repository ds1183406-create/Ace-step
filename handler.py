import runpod
import os
import torch
from ace_step import ACEStepPipeline

# Initialize pipeline globally
pipeline = None

def load_model():
    global pipeline
    if pipeline is None:
        checkpoint_path = os.environ.get('CHECKPOINT_PATH', '~/.cache/ace-step/checkpoints')
        pipeline = ACEStepPipeline.from_pretrained(
            checkpoint_path,
            torch_dtype=torch.bfloat16,
            device_map="auto"
        )
    return pipeline

def handler(job):
    job_input = job['input']
    
    # Load model
    pipe = load_model()
    
    # Extract parameters
    tags = job_input.get('tags', '')
    lyrics = job_input.get('lyrics', '')
    duration = job_input.get('duration', 60)
    inference_steps = int(os.environ.get('INFERENCE_STEPS', '27'))
    guidance_scale = float(os.environ.get('GUIDANCE_SCALE', '3.0'))
    
    # Generate music
    result = pipe(
        tags=tags,
        lyrics=lyrics,
        duration=duration,
        num_inference_steps=inference_steps,
        guidance_scale=guidance_scale
    )
    
    return {"audio_url": result.audio_url}

runpod.serverless.start({"handler": handler})