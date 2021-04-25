def test(a, b, operation="+"):
	if operation == "+" :
		print(a + b)

	elif operation == "-":
		print(a - b)

	elif operation == "*":
		print(a * b)

	elif operation == "/":
		print(a / b)

	else:
		print("Unknown operation")

       

test(10, 20)

test(20, 30)

test(10, 20, "-")

test(10, 20, "*")

test(10, 20, "a")