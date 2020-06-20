import PIL
import matplotlib.pyplot as plt

# aspect ratio: width / height

def img_width_height(img):
    width, height = img.size
    return width, height

def open_image(path):
    return PIL.Image.open(path)
    
def normal_to_grayscale(img):
    return PIL.ImageOps.grayscale(img)
    
def grayscale_to_normal(img):
    return PIL.ImageOps.colorize(img)
    
def img_to_numpy(img):
    # result shape: (height, width, 3)
    return np.asarray(img)
    
def numpy_to_img(np_img):
    return PIL.Image.fromarray(np_img.astype(np.uint8))
    
def img_to_proper_numpy(img):
    # shape: (height, width, 3)
    return np.asarray(img).astype('float32') / 255
    
def proper_numpy_to_img(np_img):
    # shape: (height, width, 3)
    return PIL.Image.fromarray((255 * np_img).astype(np.uint8))

def rotate(img, rotate_degrees):
    return img.rotate(rotate_degrees)

''' Image co-ordinates
(0, 0) (0, 1) ...
(1, 0) (1, 1) ...
...
'''

def img_paste_text(img, text, x, y, opacity=255, centre=True, colour=(0, 0, 0)):
    txt = PIL.Image.new('RGBA', img.size, (0, 0, 0, 0,))
    fnt = PIL.ImageFont.load_default()
    d = PIL.ImageDraw.Draw(txt)
    if centre:
        text_width, text_height = fnt.getsize(text)
        x -= int(text_width / 2)
        y -= int(text_height / 2)
    d.text((x,y), text, font=fnt, fill=colour + (opacity,))
    return PIL.Image.alpha_composite(img, txt)
    
def img_paste_circle(img, radius, x, y, opacity=255, colour=(0, 0, 0)):
    circle = PIL.Image.new('RGBA', img.size, (0, 0, 0, 0,))
    d = PIL.ImageDraw.Draw(circle)
    d.ellipse((x - radius, y - radius, x + radius, y + radius), fill=colour + (opacity,))
    return PIL.Image.alpha_composite(img, circle)

def img_paste_circle(img, radius, x, y, opacity=255, colour=(0, 0, 0)):
    circle = PIL.Image.new('RGBA', img.size, (0, 0, 0, 0,))
    d = PIL.ImageDraw.Draw(circle)
    d.ellipse((x - radius, y - radius, x + radius, y + radius), fill=colour + (opacity,))
    return PIL.Image.alpha_composite(img, circle)
    
def img_paste_line(img, x1, y1, x2, y2, opacity=255, colour=(0, 0, 0), width=0):
    line = PIL.Image.new('RGBA', img.size, (0, 0, 0, 0,))
    d = PIL.ImageDraw.Draw(line)
    d.line((x1, y1, x2, y2), fill=colour + (opacity,), width=width)
    return PIL.Image.alpha_composite(img, line)
    
def img_paste_resized_text(img, text, x, y, opacity=255, centre=True, colour=(0, 0, 0)):
    txt = PIL.Image.new('RGBA', img.size, (0, 0, 0, 0,))
    fnt = PIL.ImageFont.load_default()
    d = PIL.ImageDraw.Draw(txt)
    if centre:
        text_width, text_height = fnt.getsize(text)
        x -= int(text_width / 2)
        y -= int(text_height / 2)
    d.text((x,y), text, font=fnt, fill=colour + (opacity,))
    return PIL.Image.alpha_composite(img, txt)
    
def fill_image(img, colour):
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0,0),img.size], fill=colour)
    
def show_img(img):
    # img.show() is unreliable
    # scipy imshow is deprecated
    plt.imshow(img)
    
def save_img(img, path):
    raise NotImplementedError()
    
def crop(img, new_x1, new_y1, new_x2, new_y2):
    return img.crop((new_x1, new_y1, new_x2, new_y2))
    
def horizontal_flip(img):
    return PIL.ImageOps.mirror(img)
    
def vertical_flip(img):
    return PIL.ImageOps.flip(img)
    
def resize(img, size, preserve_aspect_ratio=True):
    width, height = size
    old_width, old_height = img.size
    if preserve_aspect_ratio:
        if width / old_width > height / old_height:
            # scale based on height
            scaled_width = int(old_width * height / old_height)
            scaled_height = height
        else:
            # scale based on width
            scaled_width = width
            scaled_height = int(old_height * width / old_width)
    else:
        scaled_width, scaled_height = width, height
    img = img.resize((scaled_width, scaled_height))
    result = PIL.Image.new('RGB', (width, height), color=0)
    result.paste(img, box=(int((width - scaled_width) / 2), 
                 int((height - scaled_height) / 2)))
    return result
        
def resize_v2(img, size, preserve_aspect_ratio=True):
    width, height = size
    old_width, old_height = img.size
    if preserve_aspect_ratio:
        img.thumbnail((width, height))
        scaled_width, scaled_height = img.size
        result = PIL.Image.new('RGB', (width, height), color=0)
        result.paste(img, box=(int((width - scaled_width) / 2), 
                     int((height - scaled_height) / 2)))
        
    else:
        img = img.resize((width, height))
    return result

def binary_np_to_img(data):
    # fail: return PIL.Image.fromarray(data * 255, mode='L').convert('1')
    return PIL.Image.fromarray(np.uint8(a * 255) , 'L')
    


# keypoint operations

def keypoint_crop(keypoints, new_x1, new_y1):
    # keypoints: iterable of (x, y) tuples
    return [(x - new_x1, y - new_y1) for x, y in keypoints]
    
def keypoint_resize(keypoints, old_size, new_size, preserve_aspect_ratio=True):
    # keypoints: list of (x, y) tuples
    width, height = new_size
    old_width, old_height = old_size
    if preserve_aspect_ratio:
        if width / old_width > height / old_height:
            # scale based on height
            scaled_width = int(old_width * height / old_height)
            scaled_height = height
        else:
            # scale based on width
            scaled_width = width
            scaled_height = int(old_height * width / old_width)
    else:
        scaled_width, scaled_height = width, height
    
    x_offset = int((width - scaled_width) / 2)
    y_offset = int((height - scaled_height) / 2)
    
    return [(x * scaled_width / old_width + x_offset, y * scaled_height / old_height + y_offset) 
            for x, y in keypoints]
            
def keypoint_horizontal_flip(keypoints, size):
    width, height = size
    return [(width - x, y) for x, y in keypoints]



