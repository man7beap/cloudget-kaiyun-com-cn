#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
from datetime import datetime


SITE_DATA = {
    "name": "CloudGet 开云平台",
    "url": "https://www.cloudget-kaiyun.com.cn",
    "keywords": ["开云", "云服务", "CloudGet", "云计算", "资源管理"],
    "description": "开云（CloudGet）是一个面向中小企业的轻量级云资源管理与调度平台，提供弹性计算、存储及基础网络服务。",
    "tags": ["云计算", "企业服务", "SaaS", "基础设施"],
    "release_date": "2024-06-15",
    "version": "2.3.1"
}


def format_date(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%Y年%m月%d日")
    except ValueError:
        return date_str


def build_summary_block(data):
    lines = []
    lines.append("=" * 48)
    lines.append(" 站点摘要")
    lines.append("=" * 48)

    lines.append(f"  名称：        {data['name']}")
    lines.append(f"  URL：         {data['url']}")
    lines.append(f"  版本：        {data['version']}")
    lines.append(f"  发布日期：    {format_date(data['release_date'])}")

    tags_str = ", ".join(data['tags'])
    lines.append(f"  标签：        {tags_str}")

    keywords_str = ", ".join(data['keywords'])
    lines.append(f"  关键词：      {keywords_str}")

    lines.append("-" * 48)
    lines.append(f"  说明：{data['description']}")
    lines.append("-" * 48)

    lines.append(f"  生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 48)
    return "\n".join(lines)


def generate_html_snippet(data):
    safe_name = data['name'].replace("<", "&lt;").replace(">", "&gt;")
    safe_url = data['url'].replace("<", "&lt;").replace(">", "&gt;")
    safe_desc = data['description'].replace("<", "&lt;").replace(">", "&gt;")

    snippet = (
        '<div class="site-card">\n'
        f'  <h3><a href="{safe_url}" target="_blank">{safe_name}</a></h3>\n'
        f'  <p>{safe_desc}</p>\n'
        f'  <span class="tag">{data["tags"][0]}</span>\n'
        "</div>"
    )
    return snippet


def export_json(data):
    export_data = {
        "site": data["name"],
        "url": data["url"],
        "keywords": data["keywords"],
        "tags": data["tags"],
        "description": data["description"]
    }
    return json.dumps(export_data, ensure_ascii=False, indent=2)


def main():
    mode = "text"
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()

    if mode == "json":
        output = export_json(SITE_DATA)
        print(output)
    elif mode == "html":
        output = generate_html_snippet(SITE_DATA)
        print(output)
    else:
        output = build_summary_block(SITE_DATA)
        print(output)


if __name__ == "__main__":
    main()