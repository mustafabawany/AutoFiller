from pdf2image import convert_from_path
import os

path = os.getcwd() + '/ResumeDataSet/pdf/'

j = 1;
for filename in os.listdir(path):
    try:
        images = convert_from_path(path + filename)
        os.mkdir(os.getcwd() + '/ResumeDataSet/images/' + str(j))
        for i in range(len(images)):
            images[i].save(os.getcwd() + '/ResumeDataSet/images/' + str(j) + '/' + 'page' + str(i) + '.jpeg' , 'JPEG')
        j = j + 1
    except:
        Result = "pdf error"