try:
  with open("assingment4/sample.txt", "r") as file:
     content= file.read().splitlines()
     for index, line in enumerate(content, start=1):
       print(f"line{index}:{line}")

except FileNotFoundError:
  print("Error: The file sample text was not found")
   


