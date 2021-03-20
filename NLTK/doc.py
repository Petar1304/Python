import os

folder = 'camp'

# os.chdir(folder)

# for i in os.listdir():
#     if os.path.isdir(i):
#         os.chdir(i)
#         for j in os.listdir('{}'.format(i)):
#             print(j)
#     else:
#         print(i)

for root, dirs, files in os.walk(folder):
    for f in files:
        path = os.path.join(root, f)

        with open(path, 'r', encoding='UTF-8') as doc:
            text = doc.read()
            
        print(text)
        break
    break