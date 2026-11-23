import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import numpy as np

# Load pretrained model
model = models.resnet18(pretrained=True)
model = torch.nn.Sequential(*list(model.children())[:-1])
model.eval()

# Transform image
transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
])

def extract_features(image_path):
    img = Image.open(image_path).convert('RGB')
    img = transform(img).unsqueeze(0)

    with torch.no_grad():
        features = model(img)

    emb = features.squeeze().numpy()
    emb = emb / np.linalg.norm(emb)

    return emb