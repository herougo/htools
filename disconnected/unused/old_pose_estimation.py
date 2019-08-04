
"""
Example 1:
input: tensor of shape (x, y)
output: tensor of shape (x, a, y)
Ouput must have 2 new dimensions st input is duplicated over those dimensions
(For all i,j,k output[i,j,k] = input[i,k]

a = np.expand_dims(a, axis=1)
a = np.tile(a, (1, 2, 1))



Other
Keras logical_and 
    indices = K.all(K.stack([x, y], axis=0), axis=0)

"""



text_paste = (int(img_width / 2 - text_width / 2), int(img_height / 2 - text_height / 2))
#text_paste = (0, 0)
    

    
multiplier = desired_text_height / text_height
d_text.text(text_paste, text, font=fnt, fill=text_fill)
#if i >= 10:
#  plt.imshow(text_img); return
new_img_width =  int(multiplier * img_width)
new_img_height = int(multiplier * img_height)
text_img = text_img.resize((new_img_width, new_img_height))
x2 = int(new_img_width / 2 - x)
y2 = int(new_img_height / 2 - y)
text_img = text_img.crop((x2, y2, x2 + img_width, y2 + img_height))
print(x2, y2, x, y, text_width, text_height)
#if i >= 8:
pose = PIL.Image.alpha_composite(text_img, pose)
#plt.imshow(pose); return

def debug_compute_keypoints(score):
  axes_stream = plot_stream(4, 4)
  for k in range(N_KEYPOINTS):
    s = score[k]
    s = s / (np.max(s) + 0.0000001)
    heatmap_image = s.repeat(3).reshape((RESOLUTION, RESOLUTION, 3))
    
    axes = next(axes_stream)
    axes.set_title('{} - {}'.format(k, KEYPOINT_NAMES[k]))
    axes.axis('off')
    axes.imshow(heatmap_image)
  
  plt.show()

