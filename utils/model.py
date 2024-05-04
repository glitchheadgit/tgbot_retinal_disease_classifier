import torch
from torchvision import transforms
import numpy as np
from PIL import Image


def prediction_wrapper(model, image, device=torch.device("cpu")):
    diagnosis = {0: "No DR", 1: "Mild", 2: "Moderate", 3: "Severe", 4: "Proliferative"}
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
    return diagnosis[name_class], prob


def choose_random_image(int):
    pass
