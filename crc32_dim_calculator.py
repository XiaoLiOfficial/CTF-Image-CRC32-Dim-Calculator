import binascii
import struct

prefix = b"IHDR"
suffix = b"\x08\x02\x00\x00\x00"

def make_data(width, height):
    return prefix + struct.pack('>II', width, height) + suffix

# 获取用户输入的CRC32校验值（支持0x前缀或十进制）
user_input = input("请输入开头的CRC32校验值（0x开头十六进制或十进制）: ").strip()
if user_input.lower().startswith("0x"):
    crc32_target = int(user_input, 16)
else:
    crc32_target = int(user_input)

found = False
for i in range(1, 2000):  # 宽度从1开始
    for j in range(1, 2000):  # 高度从1开始
        data = make_data(i, j)
        if binascii.crc32(data) == crc32_target:
            print(f"找到宽度和高度: {i} {j}")
            found = True
if not found:
    print("未找到匹配的宽度和高度。")