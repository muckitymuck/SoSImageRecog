# OCR.SPACE API KEY 7528f1b76188957

import ocrspace
import requests

# Or if you have an API key or desired language, pass those:
# api = ocrspace.API('Insert key here', ocrspace.Language.Croatian)

api = ocrspace.API('7528f1b76188957')

# Local File
# api.ocr_file('receipt2.jpg')

# URL
# api.ocr_url('https://ocr.space/Content/Images/receipt-ocr-original.jpg')

urlReq: object = (api.ocr_url('https://ocr.space/Content/Images/receipt-ocr-original.jpg'))



print(urlReq)
