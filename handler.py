try:
  import unzip_requirements
except ImportError:
  pass

import wget

from gluoncv.data.transforms.presets.ssd import load_test
from gluoncv.model_zoo import get_model

# use mobilenet because it's small. lambda only has 512mb of space which isn't big enough
# to download ssd or frcnn models and unzip them. hosting them on s3 unzipped is probably
# a solution
ssdnet =  get_model('ssd_512_mobilenet1.0_voc', pretrained=True, root='/tmp/models')
score_threshold = 0.5

def detect(event, context):

  # get the url
  url = event.get('url', None)

  if not url:
    response = {
      "statusCode": 500,
      "body": "Please specify a url"
    }
    return response

  # download the image
  filename = wget.download(url, out="/tmp/image.jpg")

  # classify the image
  x, _ = load_test(filename, short=512)
  classes, scores, bbox = ssdnet(x)

  results = []

  # for each result, we'll take the each
  # them if their score is greater than a given threshold
  for i in range(len(scores[0])):
      if float(scores[0][i].asnumpy().tolist()[0]) > score_threshold:
        results.append({
          "class": int(classes[0][i].asnumpy().tolist()[0]),
          "score": float(scores[0][i].asnumpy().tolist()[0]),
          "bbox": bbox[0][i].asnumpy().tolist()
        })
    

  body = {
      "bounding_boxes": results
  }

  response = {
      "statusCode": 200,
      "body": body
  }

  return response
