## Installing

## windows 安装 twint

---

1. 使用 conda 创建 twitter 环境,激活 twitter 环境

```
conda create -n twitter python=3.6
activate twitter
```

2. windows环境下，aiohttp代理配置存在问题，get.py中使用系统代理，配置trust_env=True（已改），并安装旧版本的urllib3

```
pip install urllib3==1.25.11
```

3. 下载源码，从源码安装 twint

```
git clone --depth=1 git@github.com:sunjxf/twint.git
cd twint
pip3 install . -r requirements.txt
```

4. 运行
 
      配置clash代理为全局模式，即TUN模式。
