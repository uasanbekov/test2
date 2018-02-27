import re
pattern = r"\d+"
text = "12 ай, 12 жыл, 12 уй, 12 киши"
res = re.findall(pattern, text)
if res:
	print(res)