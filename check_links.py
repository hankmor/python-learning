
import os
import re

MD_DIR = "/Users/hank/workspace/mine/website-projects/hankmo.com/content/drafts"
REPO_DIR = "/Users/hank/workspace/mine/python-projects/python-learning"
BASE_URL = "https://github.com/hankmor/python-learning/tree/main/"

def check_links():
    md_files = [f for f in os.listdir(MD_DIR) if f.endswith(".md")]
    
    print(f"Scanning {len(md_files)} markdown files...")
    
    missing_count = 0
    total_links = 0
    
    for filename in sorted(md_files):
        filepath = os.path.join(MD_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all links valid for our repo
        for match in re.finditer(r'https://github\.com/hankmor/python-learning/tree/main/([a-zA-Z0-9\-\/_]+)', content):
            total_links += 1
            rel_path = match.group(1)
            # Remove possible trailing ) or " or whitespace if regex over-matched (unlikely with this regex but be safe)
            rel_path = rel_path.strip()
            
            full_path = os.path.join(REPO_DIR, rel_path)
            
            if not os.path.exists(full_path):
                missing_count += 1
                print(f"[MISSING] {filename}: {rel_path}")
            else:
                pass
                # print(f"[OK] {filename}: {rel_path}")

    print(f"\nTotal Links Checked: {total_links}")
    print(f"Missing Paths: {missing_count}")

if __name__ == "__main__":
    check_links()
