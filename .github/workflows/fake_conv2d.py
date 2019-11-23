# *_*coding:utf-8 *_*
import numpy as np
from PIL import Image
import struct
np.set_printoptions(threshold=np.inf)


def float_bin(s): # s是对应每个数，decimal是10
    den = 0
    if s >= pow(2, 7):
        s = pow(2, 7) - 1
    if s < -pow(2, 7):
        s = -pow(2, 7)
    if s < 0:
        den = (s + pow(2, int(8))) #% pow(2, int(8))
    else:
        den = s
    return int(den)

def take_image(image_path, image_shape):
    out = []
    zeros = np.zeros((image_shape[1],image_shape[2], 1))
    for i in range(4):
        img = Image.open(image_path + 'test' + str(i) + '.jpg')
        img = img.resize((image_shape[1],image_shape[2]), Image.ANTIALIAS)
        image = np.array(img)
        image = image[:, :, 0:3]
        print('iamge.shape', image.shape)
        image = np.append(image, zeros, axis=2)
        print('iamge.shape', image.shape)
        out.append(image)
    print('np.array(out)', np.array(out).shape)
    out = np.array(out)
    print('out.shape', out.shape)


    return out

def take_feature(image_shape):
    size = 1
    for i in range(len(image_shape)):
        size = size * image_shape[i]
    input = np.random.randint(0,size,image_shape)
    print('input.shape is', input.shape)
    return  input

def im2con(input, k_size, padding, stride):
    inter = stride - 1
    out_size = (input.shape[2] - k_size + 2 * padding) // stride + 1
    out = []
    for i in range(input.shape[0]):
        for ii in range(out_size):
            for iii in range(out_size):
                a = input[i:i+1, ii*inter:k_size+(ii*inter), iii*inter:k_size+(iii*inter), :]
                a = a.reshape(input.shape[3] * k_size *k_size)
                out.append(a)
    return out

def Conv2d(input, weight, padding, stride):
    image = im2con(input, weight.shape[2], padding, stride)
    image = np.array(image)
    weight = np.reshape(weight, (-1, weight.shape[3]))
    result = np.dot(image, weight)
    result = np.reshape(result, (input.shape[0], 104, 104, -1))
    return result

def write_input(image):
    n, h, w, c = image.shape
    out = []
    image = np.int8(image)
    print('max is', np.max(image))
    print('image shape is',image.shape)
    with open('image.coe', 'w') as fp:
        for i in range(h):
            for ii in range(w):
                for iii in range(c):
                    for iiii in range(n):
                        out.append(image[iiii][i][ii][iii])
                        if len(out) == 16:
                            out.reverse()
                            for m in out:
                                m = int(float_bin(m) & 0xFFFFFFFF)
                                fp.write('%04x'%m)
                                #fp.write('%02x'%(&0x80000000))
                            fp.write(',\n')
                            out = []

def main():
    image_path = '/home/dapang/workspace/'
    image_shape = (4,208,208,4)
    weight_shape = [4,3,3,16]
    input =  take_feature(image_shape)
    #input =  take_image(image_path, image_shape)
    write_input(input)
    weight  = np.random.randint(0,576,weight_shape)
    padding = 1
    stride = 2
    result = Conv2d(input, weight, padding, stride)
    return result

if __name__ == '__main__':
    result = main()
