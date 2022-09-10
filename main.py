import os
import cv2
import merge
from pascal_voc_writer import Writer

# img.shape[1] is the width, img.shape[0] is the height

path_of_the_directory= 'Pictures'
path_of_backgrounds= 'Backgrounds'
path_of_res = 'Res'
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):

        for background in os.listdir(path_of_backgrounds):
            bg = os.path.join(path_of_backgrounds,background)
            res = merge.merge(bg, f)
            res_path = os.path.join(path_of_res, f"{filename[:-4]}_{background}")
            cv2.imwrite(res_path, res[0])

            # Write Pascal VOC annotations: https://mlhive.com/2022/02/read-and-write-pascal-voc-xml-annotations-in-python
            # Create writer
            writer = Writer(res_path, res[1], res[2])

            # Create object
            writer.addObject(f'{filename[:-4]}', res[3], res[4], res[3]+res[1], res[4]+res[2])

            writer.save(f'{path_of_res}/{filename[:-4]}_{background[:-4]}.xml')

