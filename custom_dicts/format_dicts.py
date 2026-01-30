#!/usr/bin/env python3
import os
import re
import sys

def format_rime_dict(filepath):
    """
    格式化 Rime 词典文件：
    1. 保持 YAML 头部不变
    2. 将数据部分的「词条」和「编码」之间的分隔符统一为 Tab
    3. 去除行首行尾空白
    """
    print(f"正在处理: {filepath}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"  读取失败: {e}")
        return

    # 寻找 YAML 头部的结束标记 ...
    header_end_index = -1
    for i, line in enumerate(lines):
        if line.strip() == '...':
            header_end_index = i
            break
    
    new_lines = []
    
    # 如果找到头部，保留头部
    if header_end_index != -1:
        new_lines.extend(lines[:header_end_index+1])
        start_index = header_end_index + 1
    else:
        # 如果没找到头部，假设整个文件都是数据（或者头部没有 ... 结束符）
        # 为了安全，我们只处理看起来像数据的行
        start_index = 0
        print("  注意: 未找到 '...' 头部结束标记，将尝试处理全文。")

    change_count = 0
    
    for i in range(start_index, len(lines)):
        line = lines[i]
        stripped = line.strip()
        
        # 跳过空行和注释行
        if not stripped or stripped.startswith('#'):
            new_lines.append(line) # 保持原样（包括缩进和换行）
            continue
            
        # 尝试解析行结构
        # 使用 split() 将行按空白字符（空格、Tab）分割成片段
        # 这会自动处理多个连续空格的问题，将它们视为一个分隔符
        parts = stripped.split()
        
        if len(parts) >= 2:
            word = parts[0]      # 第一部分是词条
            last_part = parts[-1] # 最后一部分可能是权重
            
            # 判断最后一部分是否为数字（权重）
            # Rime 权重通常是整数，但也可能是浮点数
            is_weight = False
            if last_part.isdigit():
                is_weight = True
            else:
                # 简单的浮点数检查
                try:
                    float(last_part)
                    is_weight = True
                except ValueError:
                    is_weight = False

            if is_weight and len(parts) > 2:
                # 格式：词条 <Tab> 编码序列 <Tab> 权重
                # 编码序列由中间部分组成，用空格连接（规范化拼音分隔）
                code_parts = parts[1:-1]
                code = " ".join(code_parts)
                weight = last_part
                new_line = f"{word}\t{code}\t{weight}\n"
            else:
                # 格式：词条 <Tab> 编码序列 (无权重，或者最后一部分被当作编码的一部分)
                # 这种情况下，除第一个词条外，后面所有都视为编码
                code_parts = parts[1:]
                code = " ".join(code_parts)
                new_line = f"{word}\t{code}\n"
            
            if new_line != line:
                change_count += 1
            new_lines.append(new_line)
        else:
            # 只有一部分或者为空，保持原样（虽然通常是不合法的词典行，但安全起见不乱改）
            new_lines.append(stripped + '\n')

    # 写入文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
        
    print(f"  完成。修正了 {change_count} 行。")

def main():
    # 获取脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 遍历目录下所有 .dict.yaml 文件
    count = 0
    for filename in os.listdir(current_dir):
        if filename.endswith(".dict.yaml"):
            filepath = os.path.join(current_dir, filename)
            format_rime_dict(filepath)
            count += 1
            
    if count == 0:
        print("未找到 .dict.yaml 文件。")
    else:
        print("所有文件处理完毕。")

if __name__ == "__main__":
    main()
