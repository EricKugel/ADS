import json
import base64

all_images = []
with open("Silly Goofy Haha/data.json") as file:
    all_images = json.loads(file.read())

print(all_images[3])

for i, data in enumerate(all_images):
    with open("Silly Goofy Haha/images/" + str(i) + ".png", "wb") as image_file:
        image_file.write(base64.b64decode(data.replace("data:image/png;base64,", "")))