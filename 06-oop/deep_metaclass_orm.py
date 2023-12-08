"""
使用 metaclass 编写一个 orm 框架示例
"""


# 定义 Field 顶层类，表示数据库的字段
class Field(object):
    # 创建时需要两个参数：字段名称和字段类型
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


# 字符串类型的字段
class StringField(Field):
    def __init__(self, name):
        # 直接调用父类的 init 方法
        super().__init__(name, 'varchar(100)')
        # super(StringField, self).__init__(name, 'varchar(100)')


# 整数类型的字段
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 编写 Model 的 metaclass，它的作用是可以将 Model class 的名称与数据库的表名做对应，将属性与数据库的字段做对应
# 为了更好的映射，所以使用该 metaclass 的类应该是一个 dict
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        # 将 Model 的属性作映射
        # ORM Model 中的属性名与数据库的表名的映射关系: Model属性名 => 数据库字段名
        mappings = dict()
        for k, v in attrs.items():
            # Model 上定义的属性为 Field 类型实例的才处理
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        # 删除多余的属性和方法，避免影响映射关系
        for k in mappings.keys():
            attrs.pop(k)
        # 保存到实例的属性上
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        # 这里假设数据库的表名和Model中的类名一致, 当然可以自定义映射规则
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


# 定义具体的 Model, 继承自 dict
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    # 获取属性，如果不存在则抛出 AttributeError，而不是 dict 本身的 KeyError
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    # 设置属性值
    def __setattr__(self, key, value):
        self[key] = value

    # orm 具体的保存到数据库的方法
    def save(self):
        fields = []
        params = []
        args = []
        # 这里的__mappings__属性是在 metaclass 中定义的
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            # 通过 getattr 方法获取当前 Model 的具体值, 默认返回 None，使用 self[k] 也可以
            args.append(getattr(self, k, None))
        # 拼装SQL， 这里的__table__属性是在 metaclass 中定义的
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


# ================================================
# 一切就绪，现在可以来使用 ORM 功能了
# ================================================


# 先定义一个 User model，也就是说数据库对应了一张 User 表
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')  # id => id: id属性对应数据库的 id 字段
    name = StringField('username')  # name => username
    email = StringField('email')  # email => email
    pwd = StringField('password')  # pwd => password


# 创建一个实例：
u = User(id=1, name='hank', email='test@g.cn', pwd='123')
# 保存到数据库：
u.save()
# Found model: User
# Found mapping: id ==> <IntegerField:id>
# Found mapping: name ==> <StringField:username>
# Found mapping: email ==> <StringField:email>
# Found mapping: pwd ==> <StringField:password>
# SQL: insert into User (id,username,email,password) values (?,?,?,?)
# ARGS: [1, 'hank', 'test@g.cn', '123']
