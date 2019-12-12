with open('day08_input.txt') as f:
    raw_photo = [int(bit) for bit in f.read().rstrip('\n')]

def unlayer(data,pixel_width = 25, pixel_height = 6):
    val_per_layer = pixel_width * pixel_height

    data = [data[i:i + val_per_layer] for i in range(0, len(data), val_per_layer)]
    zeros_count = val_per_layer
    return data


def corrupt_check(photo, pixel_width = 25, pixel_height = 6):

    val_per_layer = pixel_width * pixel_height
    zeros_count = val_per_layer

    for layer in photo:
        num_of_zeros = layer.count(0)

        if num_of_zeros < zeros_count:
            zeros_count = num_of_zeros
            max_layer = layer

    return max_layer.count(1)*max_layer.count(2)


def check_pixel(photo,layer,x,y):
    val = photo[layer][x][y]
    if val == 2:
        val = check_pixel(photo, layer+1, x, y)
    return val

def decode_im(photo,pixel_width = 25, pixel_height = 6):
    decoded_im = ''
    image = []
    for val in range(len(photo)):

        layer = photo[val]
        layer = [layer[i:i + pixel_width] for i in range(0, len(layer), pixel_width)]
        image.append(layer)

    layer_num = 0
    for y in range(pixel_height):
        for x in range(pixel_width):
            val= check_pixel(image, layer_num, y, x)
            if val == 1:
                color = '\u2588'
            else:
                color = ' '
            decoded_im+=color
        decoded_im += '\n'


    print('---------PART 2----------\n-------------------------')
    print(decoded_im)

photo = unlayer(raw_photo)
print('---------PART 1----------\n-------------------------')
print(corrupt_check(photo))
decode_im(photo)