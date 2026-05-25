# Saucedemo 自动化测试项目


## 项目简介
这是基于[Saucedemo](https://www.saucedemo.com/)电商网站的UI自动化测试项目


## 技术栈
- python3.11
- pytest
- selenium
- Page objects
- pytest-html
- 失败自动截图


## 如何运行
 ### 1.安装依赖
```bash
pip install -r requirements.txt
```
### 2.运行
```bash
pytest -v -s
```
### 3.生成html报告
```bash
pytest --html=report.html --self-contained-html
```

## 测试场景覆盖

| 模块  | 测试内容                      |
|:----|:--------------------------|
| 登录 | 正常用户登录，锁定错误用户登录（包含错误信息断言） |
| 购物车 | 添加商品，购物车徽章验证，清空购物车        |
|  结算   | 正常结算流程，字段为空的异常处理（参数化）     |
|  登出   | 登出后返回登录页面                 |

## 失败截图
测试用例失败时，自动保存截图存放在screenshots目录下，格式为用例名_时间戳.png

## 项目结构

```
saucedemo_test/
├── pages/              # Page Object 页面封装
│   ├── login_page.py
│   ├── shop_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── continue_page.py
├── screenshots/        # 失败截图目录
├── conftest.py         # pytest 配置（失败截图钩子）
├── pubulic.py          # 公共 fixture
├── test_login.py       # 登录测试
├── test_trolly.py      # 购物车测试
├── test_settlement.py  # 结算测试
├── test_logout.py      # 登出测试
├── report.html         # HTML 测试报告
└── README.md           # 项目说明
```

### 作者
李湘湘

### 参考资料
- pytest文档
- selenium文档
- Saucedemo官网








