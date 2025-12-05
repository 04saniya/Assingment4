with open("assingment4/output.txt", "w") as file :
  content=input("Enter text to write to the file: ")
  file.write(content)
  print("Data successfully written to output.txt")
  
with open("assingment4/output.txt", "a") as file :
  content2=input("\nEnter additional data to append : ")
  file.write("\n"+ content2)
  print("Data successfully appended.")

with open("assingment4/output.txt", "r") as file :
    print("\nFinal content of output.txt")
    for line in file :
      print(line.strip())


  
  #print("\nFile content of output.txt:","\n",content,"\n",content2)



