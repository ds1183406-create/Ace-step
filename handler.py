import runpod
import os
import base64
from ace_step.inference import ACEStepInference

# Initialize inference globally
inference = None

def load_model():
    global inference
    if inference is None:
        checkpoint_path = os.environ.get('CHECKPOINT_PATH', '~/.cache/ace-step/checkpoints')
        inference = ACEStepInference(
            checkpoint_path=checkpoint_path,
            device_id=0,
            bf16=True
        )
    return inference

def handler(job):
    job_input = job['input']
    
    # Load model
    inf = load_model()
    
    # Extract parameters
    tags = job_input.get('tags', '')
    lyrics = job_input.get('lyrics', '')
    duration = job_input.get('duration', 60)
    inference_steps = int(os.environ.get('INFERENCE_STEPS', '27'))
    guidance_scale = float(os.environ.get('GUIDANCE_SCALE', '3.0'))
    
    # Generate music
    audio_data = inf.text2music(
        tags=tags,
        lyrics=lyrics,
        audio_duration=duration,
        inference_steps=inference_steps,
        guidance_scale=guidance_scale
    )
    
    # Convert to base64
    audio_b64 = base64.b64encode(audio_data).decode('utf-8')
    
    return {"audio_base64": audio_b64}

runpod.serverless.start({"handler": handler})