# install metamind api first
# run the command: pip install MetaMindApi --upgrade

try:
    from metamind.api import ClassificationData, ClassificationModel, set_api_key
except ImportError:
    print "Could not import metamind.api packages"

# api key in your profile, might need to change it to work
set_api_key('Authorization: Basic wC5gH0A9hi37QAQA3i5oH045ofG1jNV07FhLQ1iwe5rmIJBtET')

# need classifier id, classifier has to be public
classifier = ClassificationModel(id='YOUR_CLASSIFIER_ID')

# change urls to image urls for ingredients we trained for
print classifier.predict(['http://www.grubdaily.com/wp-content/uploads/2011/01/IMG_4514-copy.jpg', 'http://static.chefkoch-cdn.de/ck.de/rezepte/1/1642/103048-960x720-spaghetti-carbonara.jpg'], input_type='urls')