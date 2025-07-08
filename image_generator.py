from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt, output_path="output.png", resolution=512):
    # Modeli yükle
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        torch_dtype=torch.float16
    )

    # Cihaz kontrolü (Mac için mps)
    device = "cuda" if torch.cuda.is_available() else "mps"
    pipe = pipe.to(device)

    # Görsel üret
    image = pipe(prompt, height=resolution, width=resolution).images[0]
    image.save(output_path)
    return output_path
