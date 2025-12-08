from datetime import date
import os

print("=== Create New Blog Post ===\n")

title = input("Title: ")
category = input("Category (default: Python): ") or "Python"
summary = input("Summary: ")

# Optional: opengraph image
use_image = input("Add opengraph image? (y/n, default: n): ").lower()
og_image = ""
if use_image == 'y':
    og_image = input("Image filename (e.g., my-post-cover.jpg): ")

# Create filename from title
filename = title.lower().replace(' ', '-').replace(':', '').replace('?', '')
filepath = f"content/{filename}.md"

# Write the file
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(f"""Title: {title}
Date: {date.today()}
Category: {category}
Summary: {summary}
""")
    if og_image:
        f.write(f"opengraph_image: {og_image}\n")
    
    f.write("\n\n")

print(f"\n✓ Created: {filepath}")
print("You can now write your content in this file.")