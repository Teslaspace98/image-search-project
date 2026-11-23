import torchvision
import os
import glob

# Remove old blurry CIFAR images
for f in glob.glob("images/image_*_*.jpg"):
    os.remove(f)

os.makedirs("images", exist_ok=True)

dataset = torchvision.datasets.OxfordIIITPet(root="./pet_data", split="trainval", download=True)

for i in range(1000):
    img, label = dataset[i]
    img.save(f"images/pet_{i}_{label}.jpg")

print("Done preparing 1000 real pet photos!")