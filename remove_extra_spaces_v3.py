import time


def remove_extra_spaces(text):
  newtext = ""

  for i in range(len(text)):
    if i == 0 and text[i] == " ":
      newtext += ""
    elif i == len(text) - 1 and text[i] == " ":
      newtext += ""
    elif i != 0 and text[i] == " " and text[i + 1] == " ":
      newtext += ""
    else:
      newtext += text[i]

  return newtext
 

# text = input("Enter your text:")
text = " On  my   home world "
std = "On my home world"

exp_num = 1000000
start = time.process_time()
for i in range(exp_num - 1):
  remove_extra_spaces(text)
elapsed = (time.process_time() - start)
print(f"Execution time {exp_num} experiments: {elapsed} sec")
print(f"Average time of one experiment: {elapsed / exp_num} sec")

res = remove_extra_spaces(text)
# print(text)
# print(res)

assert(res == std)