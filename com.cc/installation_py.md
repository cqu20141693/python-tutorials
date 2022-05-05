# python 的安装
1. [python官网地址](https://www.python.org/)  特别要注意勾上Add Python 3.8 to PATH，然后点“Install Now”即可完成安装。
2. 打开命令行程序（命令提示符） win+R  输入cmd  在窗口输入python命令 出现python版本信息 >>> 说明安装成功
## Toolbox的安装 
1. [Toolbox的安装地址](https://www.jetbrains.com/zh-cn/toolbox-app/)
### pycharm配置python环境
1. 在 Toolbox 中下载pychar的社区版或者项目版 或者在官网下载 [python的安装地址](http://www.jetbrains.com/pycharm/)
2. 在setting中打开  ！[Python Interpreter](https://img-blog.csdn.net/20180212011746279),！[Python Interpreter](https://img-blog.csdn.net/20180212161507242)
3. 其中Location是工程文件夹位置，图中实例是HELLO_WORLD2 ，在下面有project Interpreter: New Virtualenv environment就是配置虚拟环境的地方。

如果选择选项New environmrnt则代表创建一个新的虚拟环境。Location 是不需要选择的，自动在工程目录下新建一个venv的文件夹，  
代表了虚拟环境的位置。创建成功后可以进入该文件夹中看其目录，由 Include、Lib、Scripts三个文件夹组成，  
Lib文件中的site-packages文件夹就将安装所有的第三方库，python.exe放在Scripts文件中。Base interpreter则代表系统安装的python的位置。
下面还有两个选项，"Inherit global site-package"的意思是继承系统python中已安装的第三方库，如果不选的话，
我们创建的新环境中是没有任何第三方库的。 "Make available to all projects"意思是将这个虚拟环境应用在所有项目里，
一般不选，我觉得选了还不如直接不用虚拟环境呢！

如果你选择的是"Existing interpreter"代表的是使用已有的解释器，这个解释器不一定是全局的python，也可以是之前创建的虚拟环境。
所以网上有的人说选这里是直接用系统python并不准确。这里根据自身的情况选择想要使用的解释器。
4. Base interpreter 是python的解释器 也就是python.exe
