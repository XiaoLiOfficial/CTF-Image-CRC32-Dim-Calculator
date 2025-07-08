# CTF-Image-CRC32-Dim-Calculator

## 项目简介 / Project Overview

**中文**:  
这是一个用于 CTF（Capture The Flag）比赛的 Python 脚本，通过输入 PNG 图片的 CRC32 校验值，爆破可能的图片宽高组合。脚本针对 PNG 图片的 IHDR 块进行 CRC32 计算，遍历宽度和高度，找到匹配用户输入 CRC32 的宽高组合。

**English**:  
This is a Python script designed for CTF (Capture The Flag) competitions. It brute-forces possible image width and height combinations based on a given CRC32 checksum. The script computes the CRC32 of the PNG IHDR chunk, iterating through width and height values to find a match for the user-provided CRC32 value.

## 功能 / Features

- **输入灵活**: 支持十六进制（以 `0x` 开头）或十进制的 CRC32 校验值输入。  
- **宽高爆破**: 遍历宽度和高度（1 到 1999），找到匹配的宽高组合。  
- **简单高效**: 使用 Python 的 `binascii` 和 `struct` 模块，快速计算 CRC32 值并输出结果。  

- **Flexible Input**: Accepts CRC32 checksums in hexadecimal (with `0x` prefix) or decimal format.  
- **Dimension Brute-Force**: Iterates through width and height values (1 to 1999) to find matching combinations.  
- **Simple and Efficient**: Utilizes Python's `binascii` and `struct` modules to compute CRC32 values and output results quickly.

## 依赖 / Dependencies

- Python 3.x
- 标准库模块: `binascii`, `struct` （无需额外安装）

- Python 3.x
- Standard library modules: `binascii`, `struct` (no additional installation required)

## 安装 / Installation

1. 确保你的系统已安装 Python 3.x。  
2. 下载或克隆本仓库到本地：  
   ```bash
   git clone https://github.com/XiaoLiOfficial/CTF-Image-CRC32-Dim-Calculator
   ```
3. 进入项目目录：  
   ```bash
   cd CTF-Image-CRC32-Dim-Calculator
   ```

1. Ensure Python 3.x is installed on your system.  
2. Download or clone this repository:  
   ```bash
   git clone https://github.com/XiaoLiOfficial/CTF-Image-CRC32-Dim-Calculator
   ```
3. Navigate to the project directory:  
   ```bash
   cd CTF-Image-CRC32-Dim-Calculator
   ```

## 使用方法 / Usage

1. 运行脚本：  
   ```bash
   python crc32_dim_calculator.py
   ```
2. 根据提示输入 CRC32 校验值（十六进制以 `0x` 开头，或直接输入十进制值）。  
3. 脚本将遍历宽高组合，输出匹配的宽度和高度（如果存在）。  

1. Run the script:  
   ```bash
   python crc32_dim_calculator.py
   ```
2. Enter the CRC32 checksum as prompted (hexadecimal with `0x` prefix or decimal).  
3. The script will iterate through width and height combinations and output any matches found.

## 示例 / Example

**输入 / Input**:  
```
请输入开头的CRC32校验值（0x开头十六进制或十进制）: 0xC6FD1515
```

**输出 / Output**:  
```
找到宽度和高度: 985 1456
```

## 注意事项 / Notes

- 脚本遍历宽度和高度范围为 1 到 1999。如果需要更大的范围，可以修改代码中的 `range(1, 2000)`。  
- 如果输入的 CRC32 值无效或无法找到匹配，脚本会提示未找到结果。  
- 本脚本专为 PNG 图片的 IHDR 块设计，基于固定的前缀 `b"IHDR"` 和后缀 `b"\x08\x02\x00\x00\x00"`（表示 8 位颜色深度、RGB 类型、无压缩、无滤波、无隔行扫描）。  
- 爆破 1999×1999 组合可能耗时较长，建议根据 CTF 题目提示缩小范围以提高效率。  

- The script iterates through width and height values from 1 to 1999 by default. Modify `range(1, 2000)` in the code for larger ranges.  
- If the input CRC32 is invalid or no match is found, the script will indicate no results.  
- This script is designed for PNG images' IHDR chunk, using a fixed prefix `b"IHDR"` and suffix `b"\x08\x02\x00\x00\x00"` (indicating 8-bit color depth, RGB type, no compression, no filtering, no interlacing).  
- Brute-forcing 1999×1999 combinations may take time; consider narrowing the range based on CTF problem hints for better efficiency.

## 许可证 / License

本项目采用 MIT 许可证。详情见 [LICENSE](LICENSE) 文件。  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
