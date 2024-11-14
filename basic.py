from rembg import remove # type: ignore
from PIL import Image # type: ignore


input = Image.open('dog.png')

output = remove(input)

output.save('out.png')