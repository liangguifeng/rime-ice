# AGENTS.md

## 项目概述

本目录为 Squirrel（鼠须管）macOS 输入法的 Rime 配置目录，基于雾凇拼音（rime-ice）项目。主要包含输入方案配置、词库管理、符号库以及 Lua 脚本扩展等功能。

## 目录结构

| 目录/文件 | 说明 |
|-----------|------|
| `custom_dicts/` | 自定义用户词典目录，用于存放个人词库文件 |
| `cn_dicts/` | 中文词库目录 |
| `en_dicts/` | 英文词库目录 |
| `lua/` | Lua 脚本扩展目录 |
| `opencc/` | OpenCC 繁简转换配置目录 |
| `others/` | 其他资源文件 |
| `*.schema.yaml` | 输入方案定义文件（如 rime_ice.schema.yaml、double_pinyin_*.schema.yaml） |
| `*.dict.yaml` | 词典文件定义 |
| `squirrel.yaml` | 鼠须管主配置文件 |
| `default.yaml` | 默认配置 |
| `user.yaml` | 用户状态文件 |
| `custom_phrase.txt` | 快速输入的字符短语文件 |
| `symbols_v.yaml` | 符号配置文件 |
| `symbols_caps_v.yaml` | 大写锁定符号配置 |

## 常用操作

### 部署生效

修改配置后需要重新部署才能生效。在鼠须管菜单中选择「重新部署」，或通过命令行操作。

### 自定义词典管理

自定义词典位于 `custom_dicts/` 目录，以 `.dict.yaml` 为后缀。词典文件格式如下：

```yaml
---
name: 词典名称
version: "版本日期"
sort: by_weight
...
词条    编码
```

添加新词条时，每行包含词条和对应的拼音编码，用 Tab 或空格分隔。

### 输入方案切换

本配置支持多种输入方案，包括：
- 雾凇拼音（rime_ice）：全拼方案
- 多种双拼方案：自然码、小鹤、微软、搜狗、字母、紫光等

在「输入法设定」中选择需要的方案。

## 配置修改

### 常用配置项

| 配置文件 | 用途 |
|----------|------|
| `squirrel.yaml` | 鼠须管外观、候选窗、皮肤等配置 |
| `default.yaml` | 方案选单、按键绑定等全局配置 |
| `rime_ice.schema.yaml` | 雾凇拼音方案详细配置 |
| `custom_phrase.txt` | 自定义短语（快捷输入） |

### 修改候选词数量

在 `squirrel.yaml` 或方案对应的 `.custom.yaml` 中修改 `menu/page_size` 值。

### 修改皮肤主题

在 `squirrel.yaml` 中配置 `style/` 下的相关参数。

## 常见任务

1. **添加自定义词汇**：在 `custom_dicts/` 下创建或编辑 `.dict.yaml` 文件
2. **添加快捷短语**：编辑 `custom_phrase.txt`，格式为「快捷码\t候选词」
3. **修改候选窗样式**：编辑 `squirrel.yaml` 中的 `style/` 配置
4. **添加 Lua 扩展**：在 `lua/` 目录下添加脚本文件
5. **切换输入方案**：通过 `default.yaml` 中的 `schema_list` 配置
6. **调整词频**：手动编辑对应词典文件，或通过用户词典自动学习
7. **配置符号输入**：编辑 `symbols_v.yaml` 或使用 `v+首字母` 快捷输入

## 注意事项

- 修改 `.yaml` 配置文件时注意缩进，使用空格而非 Tab
- 自定义词典文件名即为词典名称，需要与 schema 中引用的名称一致
- 部署过程中如遇错误，检查 YAML 语法格式
- 建议定期备份 `custom_dicts/` 目录下的自定义词典
