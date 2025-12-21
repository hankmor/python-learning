
import os
import re

MD_DIR = "/Users/hank/workspace/mine/website-projects/hankmo.com/content/drafts"
BASE_PREFIX = "https://github.com/hankmor/python-learning/tree/main/"

# Mapping from "Old/Missing Suffix" to "New RepoSuffix"
# Note: Use forward slashes.
REPLACEMENTS = {
    "04-functions/02-lambda": "04-functional-programming",
    "04-functions/05-packages": "05-module",
    "04-functions/06-generators": "02-advance/02-list-generator",
    "04-functions/07-iterators": "02-advance/03-iterator",
    "04-functions/08-builtins": "01-basic/17-other/builtins_demo.py",
    "05-file-io/01-basics": "07-io",
    "06-exceptions/01-basics": "02-advance/05-error",
    "06-exceptions/02-context-managers": "07-io/context_manager_demo.py",
    "07-testing/01-unittest": "09-test/unittest",
    "04-functions/summary": "01-basic/05-func",
    "04-functions/09-project-task-manager": "01-basic/30-task-manager",
    "08-oop/04-magic-methods": "08-oop/04-magic-method",
}

def fix_links():
    md_files = [f for f in os.listdir(MD_DIR) if f.endswith(".md")]
    count = 0
    
    for filename in md_files:
        filepath = os.path.join(MD_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        
        for old_suffix, new_suffix in REPLACEMENTS.items():
            old_link = BASE_PREFIX + old_suffix
            new_link = BASE_PREFIX + new_suffix
            
            if old_link in new_content:
                new_content = new_content.replace(old_link, new_link)
                print(f"Fixed in {filename}: {old_suffix} -> {new_suffix}")
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1

    print(f"\nUpdated {count} files.")

if __name__ == "__main__":
    fix_links()
