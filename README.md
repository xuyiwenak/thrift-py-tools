# thrift工程使用方法

## 1. thrift工程结构
```
.
|-- README.md               #说明文档
|-- __init__.py
|-- build.sh                #静态文件生成类文件工具
|-- java                    #java类文件
|-- js                      #js类文件
|-- protos                  #thrift协议定义文件
`-- py                      #python类文件

```
通过修改build.sh 构建脚本可以修改thrift生成对应的语言具体如下
```
# 支持的语言可以根据情况自己调整
lang_list=(py java js)
```
## 2. 使用方法
- 根据范例，在protos目录下定义thrift静态文件，具体定义规则参考
```
# protos 是工具对应的文件夹名称
sh build.sh protos
```
这里需要注意，python项目默认生成的名称是gen-py，目前没有找到可以修改目标文件夹的地方，为了能成功import到项目中，统一改名gen_py  
检查执行结果无误可以进行正常的项目引用