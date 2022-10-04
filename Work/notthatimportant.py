data = b'Hello World\r\n'
print(data)
print(len(data))                         # 13
print(data[0:5])                         # b'Hello'
print(data.replace(b'Hello', b'Cruel'))  # b'Cruel World\r\n'