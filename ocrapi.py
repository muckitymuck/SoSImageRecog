# OCR.SPACE API KEY 7528f1b76188957

import ocrspace


# Or if you have an API key or desired language, pass those:
# api = ocrspace.API('Insert key here', ocrspace.Language.Croatian)

api = ocrspace.API('7528f1b76188957')

api.ocr_file('receipt2.jpg')

