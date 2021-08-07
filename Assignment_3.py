from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76



def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def get_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image
def get_colors(image, number_of_colors, show_chart):
    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    clf = KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_image)
    counts = Counter(labels)

    center_colors = clf.cluster_centers_

    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    h = image.shape[0]
    w = image.shape[1]
    r = w//h

    clr1 = np.ones((300,200,3), np.uint8)
    clr2 = np.ones((300,200,3), np.uint8)
    clr3 = np.ones((300,200,3), np.uint8)
    clr4 = np.ones((300,200,3), np.uint8)
    clr5 = np.ones((300,200,3), np.uint8)


    #colour rectangles
    clr1[:] = rgb_colors[0]
    clr2[:] = rgb_colors[1]
    clr3[:] = rgb_colors[2]
    clr4[:] = rgb_colors[3]
    clr5[:] = rgb_colors[4]

    clr1 = cv2.copyMakeBorder(clr1,2,1,2,2,cv2.BORDER_CONSTANT,value=[255,255,255])
    clr2 = cv2.copyMakeBorder(clr2,1,1,2,2,cv2.BORDER_CONSTANT,value=[255,255,255])
    clr3 = cv2.copyMakeBorder(clr3,1,1,2,2,cv2.BORDER_CONSTANT,value=[255,255,255])
    clr4 = cv2.copyMakeBorder(clr4,1,1,2,2,cv2.BORDER_CONSTANT,value=[255,255,255])
    clr5 = cv2.copyMakeBorder(clr5,1,2,2,2,cv2.BORDER_CONSTANT,value=[255,255,255])
    image = cv2.copyMakeBorder(image,2,2,2,2,cv2.BORDER_CONSTANT,value=[255,255,255])
    image = cv2.resize(image, (400*r,400))

    array = np.vstack([clr1,clr2,clr3,clr4,clr5])
    array = cv2.resize(array, (200,400))
    array = cv2.cvtColor(array, cv2.COLOR_RGB2BGR)
    cv2.imshow("output",np.hstack([image,array]))
    


    if (show_chart):
        plt.figure(figsize = (8, 6))
        plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
        plt.show()
        cv2.waitKey(0)


    return rgb_colors

print(get_colors(get_image(r"C:\Users\lance\Desktop\KRATOS\hello.png"),5,True))