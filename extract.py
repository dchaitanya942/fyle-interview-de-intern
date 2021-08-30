# Your imports go here
import re
import logging
import json

logger = logging.getLogger(__name__)

'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''
def extract_amount(dirpath: str) -> float:
    logger.info('extract_amount called for dir %s', dirpath)
    with open(dirpath + "/ocr.json","r",encoding='utf-8') as file:
        data = file.read()
        js = json.loads(data)
    blocks = js['Blocks']
    names = {"total","total:","theater and dance","order total","paid","payment","credit","debit"}
    for x,_ in enumerate(blocks):
        try:
            if blocks[x]['Text'].lower() in names:
                a = 1
                while a<=2:
                    if any(i.isdigit() for i in blocks[x+a]['Text']) and blocks[x+a]['Text'].find('/')==-1 and blocks[x+a]['Text']!="1" and blocks[x+a]['Text'].find('-')==-1 :
                        amount = blocks[x+a]['Text']
                        return float(re.sub("[^0123456789.]","",amount))
                    else:
                        a+=1
        except KeyError:
            pass
    return float(re.sub("[^0123456789.]","",amount))
