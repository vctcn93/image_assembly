# 如何使用此程序

### 脚本下载

```bash
git clone 
```

### 安装依赖

```bash
pip install -r requirements.txt
```

### `config` 设置

`config.ini` 文件位于 `project_name` 目录下，用以记录各个通道的详细参数设置，其格式为 `16位字符色号` 跟参数名与参数值，如：

```ini
[000000]
亮度=62
对比度=30

[ffff00]
亮度=30
对比度=-19
```

目前仅仅支持 RGB 为 `255, 128, 0` 三个值搭配的 `9` 种通道，如果有其他的 RGB 数值，则程序会自动将其数值纯化为 `255, 128, 0` 中最近的个。

### `image` 文件夹

图像文件与其对应的通道文件，文件名必须一致，通道文件必须遵循 `源文件名 + _ch` 格式，如：

```bash
example.jpeg
example_ch.jpeg
```

### `lib` 文件夹

`lib` 文件夹内为调试器设计，所有调试器必须继承 `IConverter` 类，并且遵循其 API 设计。

### 主文件

主文件记录了脚本运行的顺序与调试器设置，用户可以修改调试器的引用。一个主程序中可且仅可存在一个调试器。

### 运行

在 console 中输入：

```bash
python mian_script.py project_name
```

即可完成图片的批量调整，所有结果将被保存在 `project_name/export/` 路径下。
