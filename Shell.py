import KAAAPL

while True:
	text = input('KAAAPL > ')
	if text.strip() == "": continue
	result, error = KAAAPL.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))