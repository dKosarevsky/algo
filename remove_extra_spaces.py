import time


# text = input("Enter your text:")
text = " On  my   home world "
std = "On my home world"

exp_num = 1000000
start = time.process_time()
for i in range(exp_num - 1):
  " ".join(text.split())
elapsed = (time.process_time() - start)
print(f"Execution time {exp_num} experiments: {elapsed} sec")
print(f"Average time of one experiment: {elapsed / exp_num} sec")

text = " ".join(text.split())
# print(text)

assert(text == std)