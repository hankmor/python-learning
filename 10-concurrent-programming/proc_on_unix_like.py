"""
类 unix 系统可以使用系统级的 fork 来创建子进程， fork 在 windows 上不被支持，所以只有 linux、unix、macOS 可以使用

Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。子进程永远返回0，而父进程返回子进程的ID。
这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程
"""
import os

# 该方法返回两次，如果是 0 则表示是子进程返回的，否则是父进程返回的子进程 id
id = os.fork()
if id == 0:  # 如果是子进程返回的值，会返回 0
    print("i am a child process, my id is %d and my pid is %d" % (
        os.getpid(), os.getppid()))  # os.getpid() 返回当前进程的id，os.getppid() 返回子进程的父进程 id
else:  # 如果是父进程返回的值，则会返回子进程 id
    print("i am a parent process, my id is %d, i create a child process with id %d" % (os.getpid(), id))
# i am a parent process, my id is 12413, i create a child process with id 12414
# i am a child process, my id is 12414 and my pid is 12413
