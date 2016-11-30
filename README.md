pinyin.py
=========


## 背景

有一天回家, 看到产品忽然提出一个问题: 

	  目前介质上传之前，媒资人员需求人工手动将中文名修改成拼音；现需求如下：
	       提供一个批量将中文名修改成拼音的脚本，
	       流程：
	       1、媒资人员提供 excel 表格，表格信息包括：节目名称、地址；  
	       2、运维人员将中文名修改成拼音；        


## 分析
于是搜索, 有没有已经可以用的 `python` 小脚本可以将汉子转为拼音呢? 搜一搜得到两个结果:  
1. [https://github.com/mozillazg/python-pinyin][1]  
2. [https://github.com/cleverdeng/pinyin.py][2]  

第一个没有折腾通, 于是作罢. 开始折腾至二个. 最终想要实现的结果是....

`excel → .json → 读取 → 转拼音 → 写入`

## 最终实现

1. 把你需要转的东西从 excel 变成 .json 文件. 
2. 把 `.json` 文件命名为 `data.json`
3. 然后运行 `python pinyin.py`
4. 最后的结果会在 `finalPinyin.csv` 中.

[1]:	https://github.com/mozillazg/python-pinyin
[2]:	https://github.com/cleverdeng/pinyin.py