# 程序目录结构说明

```
hopeHandler  # 主目录
├── README.md  # 说明文档
├── requirements.txt   # 依赖包列表
├── run.py   # 入口文件
├── settings.py  # 配置文件
├── src    # 程序源码
│   └── Plugins  # 插件
│       ├── __init__.py   # 核心程序
│       ├── error_501.py  # 处理 error 501 的插件，下面三个均是处理不同关键字数据的插件。
│       ├── error_eq.py
│       ├── invalid_ecid.py
│       └── invalid_port.py
├── test   # 测试用例
│   └── DevOps_interview_data_set
└── test-case.py  # 测试程序

3 directories, 11 files
```

# 使用方法

## python 版本
本程序使用 python3 开发。

## 依赖包

在终端中执行如下命令安装依赖包。

```bash
pip3 install -r 程序主目录/requirements.txt
```

> 测试时不用安装依赖包，因为它仅会把结果打印到终端。


## 测试程序

执行 `test-case.py`

这测试会读取 test 目录下的文件作为数据源进行处理。

处理后会输出 JSON 数据到终端。

## 运行程序

### 配置

在配置文件 `settings.py` 中，你可以配置具体需要处理的文件的路径。

```
file_path = "test/DevOps_interview_data_set"
```

也可以添加或者删除要处理的关键字。

```
PLUGINS_TEMPLATE = {
    "error_eq": {"keyword": "error =", "module": "src.Plugins.error_eq"},
    "error_501": {"keyword": "error: 0 501", "module": "src.Plugins.error_501"},
    "invalid_port": {"keyword": "destination port", "module": "src.Plugins.invalid_port"},
    "invalid_ecid": {"keyword": "with invalid ecid","module": "src.Plugins.invalid_ecid"}
}
```

### 运行

配置完成后，就可以执行入口文件了。

`python3  run.py`

# 输出 JSON 数据说明

整个 JSON 数据是一个大字典

JSON 数据包含了：
1. 每小时所有的关键字出现的次数。
   比如:

   ```
   {
       "1800": {
           "numberOfOccurrence": 25,
           ...
       }
   }
2. 每小时中每种关键字出现的次数。
   比如:

   ```
   {
       "1800": {
           "numberOfOccurrence": 25,
           "errors_kw_summary": {
               "invalid_port": {
                   "numberOfOccurrence": 21,
                   ...
               }
           }
       }
   }
   ```
3. 每小时中每种关键字的详情列表。
   例如：

    ```
      {
       "1800": {
           "numberOfOccurrence": 25,
           "errors_kw_summary": {
               "invalid_port": {
                   "numberOfOccurrence": 21,
                   "errors": [{"deviceName": "BBAOMACBOOKAIR2",
                               "processId": "557",
                                "processName": "xpcproxy[55218]",
                                "description": "invalid destination port",
                                "timeWindow": "1800"
                              }, 
                                ...
                    ]
                },
                ...
           }
       }
   }
   ```

# 思路说明

1. 首先以小时为突破点，把每小时中出现的异常关键字的数据集中，并统计次数。

2. 再把集中对每小时内出现个同类关键字数据集中，通统计次数。

3. 针对不同的关键字进行不同的处理，并把我们需要的数据，组成 JSON 数据返回。

