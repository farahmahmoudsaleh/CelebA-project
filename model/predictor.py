# model/predictor.py

import torch


def predict_on_image(model, image_tensor, device):
    model.eval()
    image_tensor = image_tensor.unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image_tensor)
        preds = (output > 0.5).int().cpu().numpy()[0]
        print (preds)
    # Interpreted results
    return {
        "Smiling": "Smiling" if preds[0] == 1 else "Not Smiling",
        "Gender": "Male" if preds[1] == 1 else "Female",
        "Hat": "Wearing Hat" if preds[2] == 1 else "Not Wearing Hat"
    }

