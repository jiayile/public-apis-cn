#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
简单的链接验证脚本
用于检查README.md中的API链接是否有效
"""

import re
import sys
import requests
from urllib.parse import urlparse
import time

def extract_links_from_markdown(file_path):
    """从Markdown文件中提取所有链接"""
    links = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 匹配Markdown链接格式 [text](url)
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        matches = re.findall(link_pattern, content)

        for text, url in matches:
            # 过滤掉内部锚点链接
            if not url.startswith('#'):
                links.append({
                    'text': text,
                    'url': url,
                    'line': content[:content.find(f'[{text}]({url})')].count('\n') + 1
                })

    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        return []
    except Exception as e:
        print(f"错误：读取文件时出现问题 - {e}")
        return []

    return links

def validate_url(url, timeout=10):
    """验证单个URL是否有效"""
    try:
        # 设置请求头，模拟浏览器访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.head(url, headers=headers, timeout=timeout, allow_redirects=True)

        # 如果HEAD请求失败，尝试GET请求
        if response.status_code >= 400:
            response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)

        return {
            'valid': response.status_code < 400,
            'status_code': response.status_code,
            'final_url': response.url
        }

    except requests.exceptions.Timeout:
        return {'valid': False, 'error': '请求超时'}
    except requests.exceptions.ConnectionError:
        return {'valid': False, 'error': '连接错误'}
    except requests.exceptions.RequestException as e:
        return {'valid': False, 'error': str(e)}
    except Exception as e:
        return {'valid': False, 'error': f'未知错误: {str(e)}'}

def main():
    if len(sys.argv) != 2:
        print("用法: python validate_links.py <markdown_file>")
        print("示例: python validate_links.py ReadMe.md")
        sys.exit(1)

    file_path = sys.argv[1]
    print(f"正在验证文件: {file_path}")
    print("=" * 50)

    # 提取链接
    links = extract_links_from_markdown(file_path)

    if not links:
        print("没有找到任何链接")
        return

    print(f"找到 {len(links)} 个链接，开始验证...")
    print()

    invalid_links = []
    valid_count = 0

    # 限制验证数量以避免过长时间
    max_links = min(10, len(links))
    print(f"为了演示，只验证前 {max_links} 个链接")
    print()

    for i, link in enumerate(links[:max_links], 1):
        url = link['url']
        text = link['text']
        line = link['line']

        print(f"[{i}/{len(links)}] 验证: {text}")
        print(f"    URL: {url}")
        print(f"    行号: {line}")

        # 验证URL
        result = validate_url(url)

        if result['valid']:
            print(f"    状态: ✅ 有效 (HTTP {result['status_code']})")
            valid_count += 1
        else:
            print(f"    状态: ❌ 无效")
            if 'status_code' in result:
                print(f"    错误: HTTP {result['status_code']}")
            elif 'error' in result:
                print(f"    错误: {result['error']}")

            invalid_links.append({
                'text': text,
                'url': url,
                'line': line,
                'error': result.get('error', f"HTTP {result.get('status_code', 'Unknown')}")
            })

        print()

        # 添加延迟，避免请求过于频繁
        time.sleep(0.5)

    # 输出总结
    print("=" * 50)
    print("验证完成！")
    print(f"总链接数: {len(links)}")
    print(f"验证链接数: {max_links}")
    print(f"有效链接: {valid_count}")
    print(f"无效链接: {len(invalid_links)}")
    if max_links > 0:
        print(f"验证成功率: {valid_count/max_links*100:.1f}%")

    if invalid_links:
        print("\n无效链接详情:")
        print("-" * 30)
        for link in invalid_links:
            print(f"行 {link['line']}: {link['text']}")
            print(f"  URL: {link['url']}")
            print(f"  错误: {link['error']}")
            print()

    # 如果有无效链接，返回非零退出码
    if invalid_links:
        sys.exit(1)

if __name__ == "__main__":
    main()
