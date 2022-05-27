"""
以太坊命名服务（ENS）地址算法：
对给定字符串按照分隔符分隔，并对每一部分做递归hash运算

subdomain.example.eth的计算过程：按照"."分隔递归计算，直到没有"."时计算Root Node，Root Node根节点定义为
0x0000000000000000000000000000000000000000000000000000000000000000，即32个零字节，0x后边64个0。
=> keccak( keccak(<example.eth>) + keccak('subdomain')
=> keccak( keccak( keccak(<eth>) + keccak('example')) + keccak('subdomain')
=> keccak( keccak( keccak( keccak(<RootNode>) + keccak('eth') ) + keccak('example')) + keccak('subdomain')

keccak对应python中的sha3。
"""
import sys
import hashlib
import _pysha3 as sha3


# import pysha3 as sha3


def name_hash(name):
    if name == '':
        return '\0' * 32  # string
    else:
        '''
        将字符串按照给定符号分隔：
        label：分隔符之前的部分
        separator：分隔符
        reminder：剩下的部分
        '''
        label, separator, reminder = name.partition('.')
        label_hash = hashlib.sha3_256(label.encode()).hexdigest()
        return hashlib.sha3_256((name_hash(reminder) + label_hash).encode()).hexdigest()


def name_keccak(name):
    if name == '':
        return '\0' * 32
    else:
        label, separator, reminder = name.partition('.')
        label_hash = sha3.keccak_256(label.encode()).hexdigest()
        return sha3.keccak_256((name_hash(reminder) + label_hash).encode()).hexdigest()


def keccak(str):
    return sha3.keccak_256(str.encode()).hexdigest()


if __name__ == '__main__':
    domain = 'ethereum.eth'
    # print(domain.partition("."))
    # print(hashlib.sha3_512(domain.encode()).hexdigest())
    v1 = name_hash(domain)  # ethereum . eth
    v2 = name_keccak(domain)  # ethereum . eth
    # 合约：0xcf6aded7ef4ba665cc86789ac890bf23f5f26cc42fbf9499300e39125b3c89eb
    # d60259c834f9086190ff3aa5174ab5dadb0b7825f7b5e9ca29c90244a5ab586d
    # 01cf817eb884b7a1b85815d2f9ab9961ddae0b2cf1d8956a6da555dff92c38db
    print(v1)
    print(v2)
    domain = "subdomain.example.eth"
    v1 = name_hash(domain)
    v2 = name_keccak(domain)
    print(v1)
    print(v2)
    # c40c12d6c8f7524f6357814cf52d9a9139a7cc2024eca5c45a9842a11441947d
    # 1a855a7e587c4ad220ff3102b16767ad5da7fb785b38861536a2b929e3796dc7
    print("------")
    print(keccak("test123"))
    # solidity: 0xf81b517a242b218999ec8eec0ea6e2ddbef2a367a14e93f4a32a39e260f686ad
    # python  :   f81b517a242b218999ec8eec0ea6e2ddbef2a367a14e93f4a32a39e260f686ad
    # 加密结果不同？？？
