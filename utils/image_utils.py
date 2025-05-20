# utils/image_utils.py

from torchvision import transforms
from PIL import Image

def create_transforms():
    train_transform = transforms.Compose([
        transforms.Resize((178, 178)),
        transforms.RandomCrop((160, 160)),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.ColorJitter(brightness=0.1, contrast=0.1),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    val_test_transform = transforms.Compose([
        transforms.Resize((178, 178)),
        transforms.CenterCrop((160, 160)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    return train_transform, val_test_transform


def load_image(image_file) -> Image.Image:
    """Loads image from FastAPI UploadFile"""
    image = Image.open(image_file.file)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image
