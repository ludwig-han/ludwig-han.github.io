import os
import sys
from datetime import datetime
import re

def slugify(title):
    # 한글, 영어, 숫자만 남기고 띄어쓰기 -> 하이픈, 소문자 변환
    slug = re.sub(r'[^가-힣a-zA-Z0-9\s]', '', title)
    slug = slug.strip().replace(' ', '-')
    slug = slug.lower()
    return slug

def create_post(title):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    datetime_str = now.strftime("%Y-%m-%d %H:%M:%S +0900")
    slug = slugify(title)
    filename = f"{date_str}-{slug}.md"
    post_path = os.path.join("_posts", filename)
    img_folder = os.path.join("assets", "images", f"{date_str}-{slug}")

    # _posts 폴더 없으면 생성
    os.makedirs("_posts", exist_ok=True)
    # 이미지 폴더 생성
    os.makedirs(img_folder, exist_ok=True)

    if os.path.exists(post_path):
        print(f"⚠️ 이미 파일이 존재합니다: {post_path}")
        return

    content = f"""---
title: "{title}"
author: Ludwig
date: {datetime_str}
categories: [Blogging]
tags: [your, tags]
comments: true

toc: true
toc_sticky: true
---

## ✍️ 글 소개

여기에 글 소개를 작성하세요.

---

## 📌 주요 내용

### 1. 소제목

본문 내용을 입력하세요.

---

## 🖼️ 이미지 첨부 예시

![설명](/assets/images/{date_str}-{slug}/example.png)

---

## 📮 연락

[📧 Gmail로 보내기](https://mail.google.com/mail/?view=cm&fs=1&to=ludwighan.dev@gmail.com)
"""

    with open(post_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ 새 포스트 파일 생성됨: {post_path}")
    print(f"✅ 이미지 폴더 생성됨: {img_folder}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❗ 사용법: python create_post.py \"글 제목\"")
        sys.exit(1)
    title = sys.argv[1]
    create_post(title)
