# -*- coding: utf-8 -*-
import io
import time
import json

from wand.image import Image
from wand.color import Color
from PyPDF2 import PdfFileReader, PdfFileWriter

#export DYLD_FALLBACK_LIBRARY_PATH=/usr/local/opt/imagemagick@6/lib

memo = {}

def get_name():
    with open('../data/exampleName.json', 'r') as f:
        data = json.load(f)
        names = data['names']
        for i in range(len(names)):
            names[i] = names[i].split('.')[0]
    return names

def getPdfReader(filename):
    reader = memo.get(filename, None)
    if reader is None:
        reader = PdfFileReader(filename, strict=False)
        memo[filename] = reader
    return reader


def _run_convert(filename, page, res=120):
    idx = page + 1
    temp_time = time.time() * 1000
    # 由于每次转换的时候都需要重新将整个PDF载入内存，所以这里使用内存缓存
    pdfile = getPdfReader(filename)
    pageObj = pdfile.getPage(page)
    dst_pdf = PdfFileWriter()
    dst_pdf.addPage(pageObj)

    pdf_bytes = io.BytesIO()
    dst_pdf.write(pdf_bytes)
    pdf_bytes.seek(0)

    img = Image(file=pdf_bytes, resolution=res)
    img.format = 'png'
    img.compression_quality = 90
    
    img.background_color = Color('white')
    img.alpha_channel = 'remove' 
    #img.channels = 'rgb_channels'
    # 保存图片
    #filename[:filename.rindex('.')]
    img_path = './image/%s.png' % (filename[filename.rindex('/pdf/')+5:filename.rindex('.pdf')])
            #)
    img.save(filename=img_path)
    img.destroy()
    img = None
    pdf_bytes = None
    dst_pdf = None
    #print('convert page %d cost time %d' % (idx, (time.time() * 1000 - temp_time)))


#if __name__ == '__main__':
#    _run_convert('demo.pdf', 0)

names = get_name()  
pdf_prefix = '../data/pdf/'
for name in ['wankel-motor']:
    #print(name)
    pdf = pdf_prefix + name + '.pdf'
    try:
        _run_convert(pdf, 0)
    except:
        print('#############error '+name)
        pass
    #print(names.index(name))
    
    
    
