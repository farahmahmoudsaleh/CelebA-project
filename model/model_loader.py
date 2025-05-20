import torch

def load_model():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    with open("resnet_model.pkl", "rb") as f:
        model = torch.load(f)
        model.eval()
    return device, model
