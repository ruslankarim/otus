import torch

t_celsius = torch.tensor([0.5, 14.0, 15.0, 28.0, 11.0, 8.0, 3.0, -4.0, 6.0, 13.0, 21.0])
t_unknown = torch.tensor([35.7, 55.9, 58.2, 81.9, 56.3, 48.9, 33.9, 21.8, 48.4, 60.4, 68.4])
t_unknown_normalize = t_unknown * 0.1


def model(t_u, w, b):
    return t_u * w + b


check = model(t_unknown_normalize[0] * 0.1, 5.3671, -17.3012)
print(check)
