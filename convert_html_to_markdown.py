#!/usr/bin/env python3
import os
import re
from bs4 import BeautifulSoup

def convert_html_to_markdown(html_file, output_dir):
    # 读取HTML文件
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 解析HTML
    soup = BeautifulSoup(content, 'html.parser')
    
    # 提取文章标题
    title_tag = soup.find('h1', class_='post-full-title')
    if not title_tag:
        print(f"跳过文件: {html_file} - 未找到标题")
        return
    title = title_tag.get_text(strip=True)
    
    # 提取发布时间
    time_tag = soup.find('time', class_='post-full-meta-date')
    date = time_tag.get_text(strip=True) if time_tag else ''
    
    # 提取标签
    tag_a = soup.find('a', href=re.compile(r'^/tag/'))
    tags = [tag_a.get_text(strip=True)] if tag_a else []
    
    # 提取文章内容
    markdown_content = soup.find('div', class_='kg-card-markdown')
    if not markdown_content:
        print(f"跳过文件: {html_file} - 未找到文章内容")
        return
    content_markdown = markdown_content.decode_contents()
    
    # 清理内容，去除多余的HTML标签
    # 移除所有HTML标签，保留Markdown格式
    clean_content = re.sub(r'<[^>]+>', '', content_markdown)
    
    # 生成Markdown文件内容
    markdown = f"# {title}\n"
    if date:
        markdown += f"\n**发布时间:** {date}\n"
    if tags:
        markdown += f"\n**标签:** {', '.join(tags)}\n"
    markdown += "\n"
    markdown += clean_content
    
    # 生成输出文件名
    base_name = os.path.basename(html_file)
    md_file_name = os.path.splitext(base_name)[0] + '.md'
    output_path = os.path.join(output_dir, md_file_name)
    
    # 写入Markdown文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f"转换完成: {html_file} -> {output_path}")

def main():
    # 输入目录
    input_dir = '/home/trafalgarlu/trafalgarricardolu.github.io/backup'
    # 输出目录
    output_dir = '/home/trafalgarlu/trafalgarricardolu.github.io/markdown'
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 遍历所有HTML文件
    for root, dirs, files in os.walk(input_dir):
        # 跳过tag和author目录
        if 'tag' in root or 'author' in root:
            continue
        
        for file in files:
            if file.endswith('.html'):
                html_file = os.path.join(root, file)
                convert_html_to_markdown(html_file, output_dir)

if __name__ == "__main__":
    main()
