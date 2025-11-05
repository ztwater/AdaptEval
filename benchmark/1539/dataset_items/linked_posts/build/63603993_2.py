import torch
import torch.nn as nn

def compare1DAdaptivity(ind,outd,inputpattern):
    c = 1
    padding = 0

    input = torch.Tensor(inputpattern).view(1,c,ind)

    stride = ind // outd
    kernel_size = (ind - (outd-1)*stride)
    avg_pool = nn.AvgPool1d(stride=stride,kernel_size=kernel_size,padding=padding)
    avg_out = avg_pool(input)

    adap_avg_pool = torch.nn.AdaptiveAvgPool1d(outd)
    adap_avg_out = adap_avg_pool(input)
    
    try:
        equal_output = torch.allclose(avg_out,adap_avg_out)
    except:
        equal_output = False

    print("input.shape: {}".format(input.shape))
    print("in_dims: {}".format(ind))
    print("out_dims: {}".format(outd))
    print("")
    print("AAL strides: {}".format(stride))
    print("AAL kernel_sizes: {}".format(kernel_size))
    print("AAL pad: {}".format(padding))
    print("")
    print("outputs equal: {}".format(equal_output))
    print("")
    print("AAL input -> output: {} -> {}".format(input,avg_out))
    print("adap input -> output: {} -> {}".format(input,adap_avg_out))
    return equal_output
