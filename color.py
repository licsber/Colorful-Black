import os
import cv2
import numpy as np


def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def get_color_img(width, height):
    w = np.logspace(0, 255, height, base=1.01, dtype=np.uint8)
    w = np.reshape(w, (-1, 1))
    h = np.linspace(0, 255, width, dtype=np.uint8)
    h = np.reshape(h, (1, -1))
    shu = w * h
    shu = np.reshape(shu, (height, -1))
    shu = cv2.cvtColor(shu, cv2.COLOR_GRAY2BGR)
    shu = cv2.applyColorMap(shu, cv2.COLORMAP_HSV)

    w = np.linspace(0, 255, height, dtype=np.uint8)
    w = np.reshape(w, (-1, 1))
    h = np.logspace(0, 255, width, base=1.01, dtype=np.uint8)
    h = np.reshape(h, (1, -1))
    heng = w * h
    heng = np.reshape(heng, (height, -1))
    heng = cv2.cvtColor(heng, cv2.COLOR_GRAY2BGR)
    heng = cv2.applyColorMap(heng, cv2.COLORMAP_HSV)

    img = heng + shu

    img = cv2.medianBlur(img, 101)
    return img


def mix_img(file_dir, filename, count):
    path = os.path.join(file_dir, filename)
    for i in range(1, count):
        img = cv2.imread(path + str(i) + '.jpg')
        color = get_color_img(img.shape[1], img.shape[0])
        mask = (img == (0, 0, 0))[:, :, 0]
        img[mask] = color[mask]
        mix = img
        cv2.imwrite(path + str(i) + '.jpg', mix)


if __name__ == '__main__':
    img = get_color_img(100, 100)
    cv2.imwrite('tmp/1.jpg', img)
