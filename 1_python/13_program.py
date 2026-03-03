import re

text = "connect me at 1234567899 or email me at example@example.com"

digits = re.findall(r'\d+', text)
print("Digits found:", digits)

updated_text = re.sub(r'\d', 'x', text)
print("Updated text:", updated_text)