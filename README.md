# 接口自动化测试框架

基于 Python + pytest + requests 实现的短信接口自动化测试框架。

## 项目简介

本项目用于对短信提交接口进行自动化测试，涵盖了标准短信提交接口 (`/json/sms/Submit`) 以及 DFRC 相关接口的测试。框架采用数据驱动的方式，将测试数据与代码分离，便于维护和扩展。

## 目录结构

```text
pytest_demo/
├── api/                # 接口封装层，统一管理 API 请求逻辑
│   └── SmaApi.py       # SMS 及 DFRC 接口方法封装
├── config/             # 配置层
│   └── config.py       # 环境配置（URL、账号、密码等）
├── exceptions/         # 自定义异常
│   └── exceptions.py   # 接口请求异常定义
├── submit/             # 测试用例层
│   ├── test_submit.py  # 标准短信提交接口测试用例
│   └── dfrc/           # DFRC 相关测试
│       └── test_dfrc_submit.py
├── test_data/          # 测试数据层
│   ├── sms_test_data.json   # 标准短信测试数据
│   ├── dfrc_test_data.json  # DFRC 测试数据
│   └── load_data.py         # 数据加载工具类
├── util/               # 工具层
│   └── md5_util.py     # MD5 加密工具
└── README.md           # 项目说明文档
```

## 环境要求

- Python 3.x
- 依赖库：
  - pytest
  - requests

## 安装与配置

1. **克隆项目**
   ```bash
   git clone <repository_url>
   cd pytest_demo
   ```

2. **安装依赖**
   建议使用虚拟环境：
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\activate   # Windows
   pip install pytest requests
   ```

3. **配置环境**
   在 `config/config.py` 中配置测试环境信息：
   - `QAConfig`: 标准接口环境配置（URL, 账号, 密码等）。
   - `DFRCConfig`: DFRC 接口环境配置。
   - 修改 `CONFIG` 变量以指定当前使用的配置类。

## 运行测试

使用 `pytest` 命令运行测试：

```bash
# 运行所有测试
pytest

# 运行指定文件的测试
pytest submit/test_submit.py

# 运行包含特定关键字的测试用例
pytest -k "test_post_submit"

# 生成简单报告（需安装 pytest-html）
# pip install pytest-html
# pytest --html=report.html
```

## 功能特性

- **数据驱动**：使用 `@pytest.mark.parametrize` 结合 JSON 文件 (`test_data/*.json`) 加载测试用例，实现数据与逻辑分离。
- **接口封装**：`SmaApi` 类封装了底层的 HTTP 请求与异常处理，测试用例只需关注业务逻辑。
- **签名处理**：`util/md5_util.py` 提供了 MD5 签名生成工具，支持 DFRC 接口的鉴权需求。
- **异常处理**：自定义 `ApiRequestError`，统一处理接口请求超时或异常情况。

## 测试接口说明

1. **标准短信提交接口**
   - 路径：`/json/sms/Submit`
   - 测试类：`TestSubmit`
   - 数据源：`sms_test_data.json`

2. **DFRC 提交接口**
   - 路径：配置于 `DFRCConfig` (示例中为 `/xxxx`)
   - 测试类：`test_dfrc_submit`
   - 数据源：`dfrc_test_data.json`
   - 特殊逻辑：请求前会根据参数生成 MD5 签名 (`sign`)。
