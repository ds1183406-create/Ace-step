import runpod

def handler(event):
    print("Received event:", event)
    input_data = event.get("input", {})
    tags = input_data.get("tags", "test music")
    lyrics = input_data.get("lyrics", "")
    duration = input_data.get("duration", 30)
    
    # Return dummy output for testing
    return {
        "status": "success",
        "tags": tags,
        "lyrics": lyrics,
        "duration": duration,
        "message": "ACE-Step handler executed successfully!"
    }

runpod.serverless.start({"handler": handler})