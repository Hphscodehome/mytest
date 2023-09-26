import torch
print(torch.__version__)
print(torch.version.cuda)
print(torch.backends.cudnn.version())
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0))
print(torch.cuda.current_device())
from torch.backends import cudnn
print(cudnn.is_available())
print(torch.device("cuda:0"))
print(torch.cuda.empty_cache())
