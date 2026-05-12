import re
import gzip

# read header
with open("html_gz.h", "r", encoding="utf-8") as f:
    text = f.read()

# extract hex bytes
hex_values = re.findall(r'0x([0-9a-fA-F]{2})', text)

# convert to bytes
data = bytes(int(h,16) for h in hex_values)

# decompress
html = gzip.decompress(data)

# save
with open("index.html", "wb") as f:
    f.write(html)

print("index.html extracted successfully")