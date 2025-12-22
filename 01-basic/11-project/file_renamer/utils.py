# utils.py
import os

def list_files(directory, extension=None, pattern=None):
    """
    列出目录中的文件
    
    Args:
        directory: 目标目录
        extension: 文件扩展名过滤（如'.txt'）
        pattern: 文件名模式（简单的包含匹配）
    
    Returns:
        文件路径列表
    """
    files = []
    
    # 检查目录是否存在
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return []

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # 只处理文件，忽略目录
        if not os.path.isfile(filepath):
            continue
        
        # 扩展名过滤
        if extension and not filename.endswith(extension):
            continue
        
        # 文件名模式过滤
        if pattern and pattern not in filename:
            continue
        
        files.append(filepath)
    
    return files
