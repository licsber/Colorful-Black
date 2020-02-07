#  五彩斑斓的黑

## 项目简介

把pdf文件转化为五彩斑斓的pdf！  
这样看黑白论文的时候就不无聊了（

## 效果图
![](https://img2018.cnblogs.com/blog/1007765/202002/1007765-20200205231311731-1891686149.jpg)
![](https://github.com/Licsber/Colorful-Black/raw/master/example.jpg)

## 环境依赖

```
conda install flask imagemagick wand ghostscript opencv -c conda-forge
yum install mesa-libGL.x86_64
```

## 运行

```
python server.py
```

## TODOS

异步返回处理结果  
使用`OSS`减轻网络io负担  
更多文件图片格式支持

## 介绍文章

[我的博客园: 五彩斑斓的黑](https://www.cnblogs.com/licsber/p/colorful-black.html)

## 备注

写着玩的项目，看心情维护
