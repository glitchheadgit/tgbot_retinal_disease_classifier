import torch
import random

from pathlib import Path
from torchvision import transforms
import numpy as np
from PIL import Image

DIAGNOSIS = {0: "No retinopathy", 1: "Mild", 2: "Moderate", 3: "Severe", 4: "Proliferative"}

def prediction_wrapper(model, image, device=torch.device("cpu")):
    image = Image.open(image)
    with torch.no_grad():
        transform = transforms.Compose(
            [
                transforms.Resize(size=(224, 224)),
                transforms.ToTensor(),
                transforms.Normalize(
                    [0.4064, 0.2169, 0.0722], [0.2786, 0.1515, 0.0811]
                ),
            ]
        )
        image_tensor = transform(image)
        image_sample = image_tensor.unsqueeze(0)
        image_sample = image_sample.to(device)
        model.eval()
        logit = model(image_sample).cpu()
        probs = torch.nn.functional.softmax(logit, dim=-1).numpy()
        prob = np.max(probs)
        name_class = np.argmax(probs)
    return f'{DIAGNOSIS[name_class]}', prob


def choose_image_by_stage(stage):
    if stage == 5:
        n = len(DIAGNOSIS)
        stage = random.randint(1, n)
    p = Path('data/images')
    images = list(p.glob(f'{stage}*'))
    idx = random.choice(range(len(images)-1))
    return str(images[idx].absolute())

