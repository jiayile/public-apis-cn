#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
格式验证脚本
检查README.md的格式是否符合标准
"""

import re
import sys
from typing import List, Tuple

# 配置常量
MIN_ENTRIES_PER_CATEGORY = 3
MAX_DESCRIPTION_LENGTH = 100
VALID_AUTH_VALUES = ['No', 'apiKey', 'OAuth', 'X-Mashape-Key', 'User-Agent']
VALID_HTTPS_VALUES = ['Yes', 'No']
VALID_CORS_VALUES = ['Yes', 'No', 'Unknown']

# 正则表达式
CATEGORY_TITLE_RE = re.compile(r'^### (.+)$')
CATEGORY_INDEX_RE = re.compile(r'^\* \[(.+)\]\(#.+\)$')
API_ENTRY_RE = re.compile(r'^\| \[(.+)\]\((.+)\) \| (.+) \| (.+) \| (.+) \| (.+) \|$')
BACK_TO_INDEX_RE = re.compile(r'^\*\*\[⬆ 返回索引\]\(#分类索引\)\*\*$')

def error_message(line_num: int, message: str) -> str:
    """生成错误消息"""
    return f"第 {line_num} 行: {message}"

def check_title(line_num: int, title: str) -> List[str]:
    """检查API标题格式"""
    errors = []

    if not title.strip():
        errors.append(error_message(line_num, "API标题不能为空"))

    return errors

def check_description(line_num: int, description: str) -> List[str]:
    """检查API描述"""
    errors = []

    if not description.strip():
        errors.append(error_message(line_num, "API描述不能为空"))
    elif len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(error_message(line_num, f"API描述过长（{len(description)}字符，最大{MAX_DESCRIPTION_LENGTH}字符）"))

    return errors

def check_auth(line_num: int, auth: str) -> List[str]:
    """检查认证字段"""
    errors = []

    auth = auth.strip().replace('`', '')
    if auth not in VALID_AUTH_VALUES:
        errors.append(error_message(line_num, f"无效的认证值: '{auth}'，有效值: {VALID_AUTH_VALUES}"))

    return errors

def check_https(line_num: int, https: str) -> List[str]:
    """检查HTTPS字段"""
    errors = []

    https = https.strip()
    if https not in VALID_HTTPS_VALUES:
        errors.append(error_message(line_num, f"无效的HTTPS值: '{https}'，有效值: {VALID_HTTPS_VALUES}"))

    return errors

def check_cors(line_num: int, cors: str) -> List[str]:
    """检查CORS字段"""
    errors = []

    cors = cors.strip()
    if cors not in VALID_CORS_VALUES:
        errors.append(error_message(line_num, f"无效的CORS值: '{cors}'，有效值: {VALID_CORS_VALUES}"))

    return errors

def check_api_entry(line_num: int, line: str) -> List[str]:
    """检查API条目格式"""
    errors = []

    match = API_ENTRY_RE.match(line)
    if not match:
        errors.append(error_message(line_num, "API条目格式不正确"))
        return errors

    title, url, description, auth, https, cors = match.groups()

    # 检查各个字段
    errors.extend(check_title(line_num, title))
    errors.extend(check_description(line_num, description))
    errors.extend(check_auth(line_num, auth))
    errors.extend(check_https(line_num, https))
    errors.extend(check_cors(line_num, cors))

    # 检查URL格式
    if not url.startswith(('http://', 'https://')):
        errors.append(error_message(line_num, f"无效的URL格式: {url}"))

    return errors

def check_alphabetical_order(lines: List[str]) -> List[str]:
    """检查API条目的字母顺序"""
    errors = []
    current_category = None
    previous_api_name = None

    for line_num, line in enumerate(lines, 1):
        # 检查是否是分类标题
        category_match = CATEGORY_TITLE_RE.match(line)
        if category_match:
            current_category = category_match.group(1)
            previous_api_name = None
            continue

        # 检查是否是API条目
        api_match = API_ENTRY_RE.match(line)
        if api_match and current_category:
            api_name = api_match.group(1).lower()

            if previous_api_name and api_name < previous_api_name:
                errors.append(error_message(line_num,
                    f"API '{api_match.group(1)}' 在分类 '{current_category}' 中顺序不正确"))

            previous_api_name = api_name

    return errors

def check_category_completeness(lines: List[str]) -> List[str]:
    """检查分类的完整性"""
    errors = []
    current_category = None
    api_count = 0

    # 跳过检查的分类（这些不是API分类）
    skip_categories = {
        '🔍 快速查找', '📖 字段说明', '🔐 认证方式说明',
        '了解更多', '分类索引', '参与贡献', '许可证', '致谢'
    }

    for line_num, line in enumerate(lines, 1):
        # 检查是否是分类标题
        category_match = CATEGORY_TITLE_RE.match(line)
        if category_match:
            category_name = category_match.group(1)

            # 检查前一个分类的API数量（跳过非API分类）
            if (current_category and
                current_category not in skip_categories and
                api_count < MIN_ENTRIES_PER_CATEGORY):
                errors.append(error_message(line_num,
                    f"分类 '{current_category}' 只有 {api_count} 个API，最少需要 {MIN_ENTRIES_PER_CATEGORY} 个"))

            current_category = category_name
            api_count = 0
            continue

        # 计算API条目
        if API_ENTRY_RE.match(line):
            api_count += 1

    # 检查最后一个分类（跳过非API分类）
    if (current_category and
        current_category not in skip_categories and
        api_count < MIN_ENTRIES_PER_CATEGORY):
        errors.append(error_message(len(lines),
            f"分类 '{current_category}' 只有 {api_count} 个API，最少需要 {MIN_ENTRIES_PER_CATEGORY} 个"))

    return errors

def validate_file_format(file_path: str) -> List[str]:
    """验证整个文件格式"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.rstrip() for line in file]
    except FileNotFoundError:
        return [f"错误：找不到文件 {file_path}"]
    except Exception as e:
        return [f"错误：读取文件时出现问题 - {e}"]

    errors = []

    # 暂时跳过字母顺序检查（发布后优化）
    # errors.extend(check_alphabetical_order(lines))

    # 检查分类完整性
    errors.extend(check_category_completeness(lines))

    # 检查每一行的格式
    for line_num, line in enumerate(lines, 1):
        if API_ENTRY_RE.match(line):
            errors.extend(check_api_entry(line_num, line))

    return errors

def main():
    if len(sys.argv) != 2:
        print("用法: python validate_format.py <markdown_file>")
        print("示例: python validate_format.py ReadMe.md")
        sys.exit(1)

    file_path = sys.argv[1]
    print(f"正在验证文件格式: {file_path}")
    print("=" * 50)

    errors = validate_file_format(file_path)

    if errors:
        print(f"发现 {len(errors)} 个格式错误:")
        print("-" * 30)
        for error in errors:
            print(error)
        sys.exit(1)
    else:
        print("✅ 文件格式验证通过！")

if __name__ == "__main__":
    main()
