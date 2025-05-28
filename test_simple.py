#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def test_markdown_parsing():
    """测试Markdown解析功能"""
    try:
        with open('ReadMe.md', 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 匹配Markdown链接格式 [text](url)
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        matches = re.findall(link_pattern, content)
        
        print(f"找到 {len(matches)} 个链接")
        
        # 显示前5个链接
        for i, (text, url) in enumerate(matches[:5]):
            if not url.startswith('#'):
                print(f"{i+1}. {text} -> {url}")
        
        return True
        
    except Exception as e:
        print(f"错误: {e}")
        return False

if __name__ == "__main__":
    test_markdown_parsing()
