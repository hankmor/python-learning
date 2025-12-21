"""
练习3：Logger接口
使用ABC定义日志系统接口
"""

from abc import ABC, abstractmethod
import datetime

class Logger(ABC):
    """
    日志抽象基类
    - 定义日志接口
    - 提供公共方法
    """
    
    LOG_LEVELS = {
        'DEBUG': 0,
        'INFO': 1,
        'WARNING': 2,
        'ERROR': 3,
        'CRITICAL': 4
    }
    
    def __init__(self, level='INFO'):
        """初始化日志级别"""
        self.level = level
    
    @abstractmethod
    def write_log(self, message, level):
        """写入日志（抽象方法）"""
        pass
    
    def _should_log(self, level):
        """判断是否应该记录此级别的日志"""
        return self.LOG_LEVELS[level] >= self.LOG_LEVELS[self.level]
    
    def _format_message(self, message, level):
        """格式化日志消息（具体方法）"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] [{level}] {message}"
    
    def debug(self, message):
        """记录DEBUG级别日志"""
        if self._should_log('DEBUG'):
            formatted = self._format_message(message, 'DEBUG')
            self.write_log(formatted, 'DEBUG')
    
    def info(self, message):
        """记录INFO级别日志"""
        if self._should_log('INFO'):
            formatted = self._format_message(message, 'INFO')
            self.write_log(formatted, 'INFO')
    
    def warning(self, message):
        """记录WARNING级别日志"""
        if self._should_log('WARNING'):
            formatted = self._format_message(message, 'WARNING')
            self.write_log(formatted, 'WARNING')
    
    def error(self, message):
        """记录ERROR级别日志"""
        if self._should_log('ERROR'):
            formatted = self._format_message(message, 'ERROR')
            self.write_log(formatted, 'ERROR')
    
    def critical(self, message):
        """记录CRITICAL级别日志"""
        if self._should_log('CRITICAL'):
            formatted = self._format_message(message, 'CRITICAL')
            self.write_log(formatted, 'CRITICAL')


class ConsoleLogger(Logger):
    """控制台日志器"""
    
    def __init__(self, level='INFO', color=True):
        super().__init__(level)
        self.color = color
    
    def write_log(self, message, level):
        """输出到控制台"""
        if self.color:
            # ANSI颜色代码
            colors = {
                'DEBUG': '\033[36m',    # 青色
                'INFO': '\033[32m',     # 绿色
                'WARNING': '\033[33m',  # 黄色
                'ERROR': '\033[31m',    # 红色
                'CRITICAL': '\033[35m'  # 紫色
            }
            reset = '\033[0m'
            colored_message = f"{colors.get(level, '')}{message}{reset}"
            print(colored_message)
        else:
            print(message)


class FileLogger(Logger):
    """文件日志器"""
    
    def __init__(self, filename, level='INFO'):
        super().__init__(level)
        self.filename = filename
    
    def write_log(self, message, level):
        """写入文件"""
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(message + '\n')


class MultiLogger(Logger):
    """
    多目标日志器
    - 同时输出到多个目标
    """
    
    def __init__(self, loggers):
        """
        初始化
        Args:
            loggers: Logger列表
        """
        # 使用最低级别
        levels = [l.level for l in loggers]
        min_level = min(levels, key=lambda x: self.LOG_LEVELS[x])
        super().__init__(min_level)
        self.loggers = loggers
    
    def write_log(self, message, level):
        """写入所有日志器"""
        for logger in self.loggers:
            if logger._should_log(level):
                logger.write_log(message, level)


# 测试
if __name__ == "__main__":
    import tempfile
    import os
    
    print("=== 控制台日志器 ===")
    console = ConsoleLogger(level='DEBUG', color=True)
    console.debug("这是DEBUG信息")
    console.info("这是INFO信息")
    console.warning("这是WARNING信息")
    console.error("这是ERROR信息")
    console.critical("这是CRITICAL信息")
    
    print("\n=== 文件日志器 ===")
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
        log_file = f.name
    
    file_logger = FileLogger(log_file, level='WARNING')
    file_logger.debug("这不会被记录")
    file_logger.info("这也不会被记录")
    file_logger.warning("这会被记录")
    file_logger.error("这也会被记录")
    
    print(f"已写入日志文件: {log_file}")
    with open(log_file, 'r', encoding='utf-8') as f:
        print(f.read())
    
    print("\n=== 多目标日志器 ===")
    multi = MultiLogger([
        ConsoleLogger(level='INFO', color=False),
        FileLogger(log_file, level='ERROR')
    ])
    multi.debug("发送到: 无")
    multi.info("发送到: 控制台")
    multi.error("发送到: 控制台+文件")
    
    # 清理
    os.unlink(log_file)
