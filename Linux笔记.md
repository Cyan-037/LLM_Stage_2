

# Linux环境

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425102955.png" alt="image-20260425102955884" style="zoom:67%;" />

如图，我们需要用VMware workstation软件，得到虚拟的硬件，然后安装操作系统，得到虚拟机。



## VMware安装

找到课程资料内的`VMware-workstation-full-17.5.2-23775571.exe`软件打开一路下一步即可。

如果有提示

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425103054.png" alt="image-20260425103054488" style="zoom:33%;" />



### 验证安装

主要检查网卡

快捷键：`win键 + r`，输入`ncpa.cpl`

确认有2个vmware网卡

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425103147.png" alt="image-20260425103147278" style="zoom:67%;" />



### 解压虚拟机

课程资料提供了`dify_ubuntu.zip`，里面是一个安装好的虚拟机，解压后，用VMware软件打开即可直接使用。

解压这个zip包，到任意地方（建议，不在C盘，不在中文路径下）

解压后，会得到一个`dify_ubuntu`的文件夹。

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425105811.png" alt="image-20260425105811644" style="zoom:67%;" />

如图，解压后是一个文件夹，里面都是虚拟化硬件的文件。



### 打开虚拟机

先确保你解压好了。

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425105908.png" alt="image-20260425105908844" style="zoom:67%;" />

找到你刚刚解压的`dify_ubuntu`文件夹，进入找到：

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425105946.png" alt="image-20260425105946179" style="zoom:67%;" />

打开后，虚拟机就导入了`VMware`

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425110006.png" alt="image-20260425110006280" style="zoom:67%;" />



### 设置虚拟网络

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425110701.png" alt="image-20260425110701283" style="zoom:67%;" />

如图，课程提供的`dify_ubuntu`虚拟机，IP固定为`192.168.88.100`，在VMware端需要适配这个IP，即提供`192.168.88.xxx`的局域网络。



1. 打开虚拟网络编辑器

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425110804.png" alt="image-20260425110804416" style="zoom:67%;" />

2. 获得管理员权限，才能修改

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425110841.png" alt="image-20260425110841093" style="zoom:67%;" />

3. 修改子网IP为`192.168.88.0`

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425110921.png" alt="image-20260425110921242" style="zoom:67%;" />

4. `NAT`设置

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425111001.png" alt="image-20260425111001066" style="zoom:67%;" />

5. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425111041.png" alt="image-20260425111041180" style="zoom:67%;" />

6. 如图全部设置完，点击确定生效

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425111100.png" alt="image-20260425111100940" style="zoom:67%;" />



### 切换虚拟机快照

![image-20260425111459087](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425111459.png)

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425111626.png" alt="image-20260425111626167" style="zoom:67%;" />

然后就可以开机了

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425111744.png" alt="image-20260425111744150" style="zoom:67%;" />

选择我已经复制



### 账户密码

账户：`itheima`

密码：`123456`



### 检查网络

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425111917.png" alt="image-20260425111917427" style="zoom:67%;" />



输入命令：`ifconfig`

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425112006.png" alt="image-20260425112006102" style="zoom:67%;" />



是否能联网，输入命令：`curl cip.cc`：

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425112107.png" alt="image-20260425112107953" style="zoom:67%;" />







### 通过Windows终端软件远程连接虚拟机使用

1. 找到Windows内置的终端软件

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425112553.png" alt="image-20260425112553790" style="zoom:67%;" />

   如果没有，去Windows自带商店下载即可

2. 输入命令

   ```shell
   ssh itheima@192.168.88.100
   ```

3. 弹出提示，输入`yes`

   ![image-20260425112712789](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425112712.png)

4. 输入密码（输入的时候没反应，正常输入即可）

   ![image-20260425112727001](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425112727.png)

5. 如图，成功进入

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425112822.png" alt="image-20260425112822603" style="zoom:67%;" />

6. 如果关闭了，下一次打开，从`ssh itheima@192.168.88.100`再次输入即可进入



#### 扩展-保存这个链接

1. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425113053.png" alt="image-20260425113053680" style="zoom:67%;" />

2. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425113117.png" alt="image-20260425113117055" style="zoom:67%;" />

3. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425113134.png" alt="image-20260425113134342" style="zoom:67%;" />

4. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425113235.png" alt="image-20260425113235522" style="zoom:67%;" />

5. 下一次打开即可：

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425113308.png" alt="image-20260425113308056" style="zoom:67%;" />



#### 扩展 - 使用MobaXTerm软件连接Linux

> 用户替换没有Windows的终端软件用

1. 找到资料内提供的`MobaXterm_Portable_v26.3.zip`

2. 解压到任何地方（别解压到同步资料文件夹内）

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425154238.png" alt="image-20260425154238680" style="zoom:67%;" />

3. 双击运行`MobaXterm_Personal_26.3.exe`

4. 创建新会话，点击`new session`

   ![image-20260425154308548](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425154308.png)

5. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425154341.png" alt="image-20260425154341746" style="zoom:67%;" />

6. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425154356.png" alt="image-20260425154356462" style="zoom:67%;" />

7. 输入密码`123456`回车

   ![image-20260425154413613](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425154413.png)

8. 保存记录密码

   ![image-20260425154509936](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425154509.png)

9. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425154549.png" alt="image-20260425154549665" style="zoom:67%;" />

10. 连接成功

    <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425154602.png" alt="image-20260425154602620" style="zoom:67%;" />

11. 以后使用，只需要双击即可：

    <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425154636.png" alt="image-20260425154636497" style="zoom:67%;" />





## 命令行操作



### 操作系统的控制模式

- GUI模式（图形化界面），有鼠标，有窗口，有最大最小等
- 命令行模式，纯靠写命令去操作系统



#### Windows系统

- 以GUI为主
- 基本不用命令行（开发者偶尔用）

> Windows（视窗操作系统），GUI图形界面就是它的卖点，从30年前就开始定下的方向。



#### Mac系统

- 以GUI为主
- 命令行也常用（开发者）



#### Linux系统

- 以命令行为主
- GUI偶尔用（小白）
- GUI基本不用（开发者）

> Linux设计的时候，就没考虑过GUI
>
> 现在的Linux有GUI（鼠标操作），来自全球的其它程序员无私贡献代码
>
> - Linux的GUI没有Windows和Mac稳定，不好看

- 在企业中，Linux，99%都是纯命令行操作



#### 学习Linux

学的就是`命令行`中的各种命令





## Linux的目录结构

### 单树的Linux

![image-20260425121648501](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425121648.png)

如上图，Windows是多树结构，每一个树就是一个盘符。



![image-20260425121716050](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425121716.png)

如图，Linux是单树结构，仅有一个`/`，叫做根目录，简称`根`



 

### 路径描述

举例，Windows

```shell
# C盘内system文件夹内的dlls文件夹内的msvp140.dll文件

C:\system\dlls\msvp140.dll

# D盘内的dev文件夹内的code文件夹内的hello.py文件

D:\dev\code\hello.py
```

- `C:\`或`D:\`是根目录，Windows有多个根
- `\`，是Windows默认的层次符号（Windows也支持`/`表示层次结构，只是默认显示的是`\`)



Linux

```shell
# 根目录内有etc文件夹，内有config文件夹，内有mysql.inf文件
/etc/config/mysql.inf

# 根目录有var文件夹，内有local文件夹，内有hello.txt文件
/var/local/hello.txt
```

- 最左侧的`/`表示根（Linux仅有1个）
- 中间的`/`表示文件夹之间的层次关系









# Linux命令

## 基本格式

```shell
command [-options] [parameter]

说明:
- command : 命令名, 相应功能的英文单词或单词的缩写
- [-options] : 选项, 可用来对命令进行控制, 也可以省略
- [parameter]  : 传给命令的参数, 可以是 零个、一个 或者 多个
```

- `[]`表示可选，可以写也可以不写



## Linux快捷键

- `ctrl + c`，退出程序，取消运行

- `ctrl + l`，清屏

- `ctrl + d`，退出登录（就是命令`exit`效果）

- `ctrl + a`，跳到命令行头部

- `ctrl + e`，跳到命令行尾部

- `ctrl + 键盘左右`，左右跳跃整个单词

- `键盘上下`，查找历史输入过的命令

- `!内容`，从历史记录中查找，找到第一个符合内容开头的命令并执行

  <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426120831.png" alt="image-20260426120831463" style="zoom:33%;" />

- `ctrl + r`，输入内容搜索

  - 输入内容搜索
  - 搜到后，直接回车，执行
  - 搜到后，不要，`ctrl + c`退掉
  - 搜到后，想修改不直接执行，键盘左右键，就可以修改





## pwd命令

功能：列出当前命令行所在的工作目录

pwd: print work directory

示例

```python
itheima@itheima:~$ pwd
/home/itheima
```

如上，输出`/home/itheima`

- `/`最左侧`/`表示根

整体表示，你当前处在根目录内home文件夹内的itheima文件夹



> Linux终端（命令行）默认一打开就处在`/home/用户名`文件夹内





## HOME目录

在系统中，用户的`家目录`

`家目录`是每个用户的私有文件夹，用户在此文件夹内拥有全部权限。



操作系统都用HOME目录

- Windows：`C:\Users\用户名`
- Linux：`/home/用户名`
- Mac：`/Users/用户名`



## cd命令

cd：`change directory`取了c和d

作用：在命令行下切换工作目录

语法：

```shell
cd [目录]
```

示例

```shell
cd /
```

- 切换工作目录到`/`下

示例

```shell
itheima@itheima:/home$ pwd
/home
```



示例（不写目录）

```shell
cd
```

- 默认回家（回到用户的家目录）



示例

```shell
itheima@itheima:/$ cd ~
itheima@itheima:~$ pwd
/home/itheima
```

- `cd ~`也是回家，`~`代表用户家目录



## ls 命令

### 基础用法

ls：`list取了l和s`

功能：列出当前工作目录下有什么东西

示例

```shell
itheima@itheima:~$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
```

- 当前工作目录下的内容列出来，如上，表示家目录内有这么多东西



示例

```shell
itheima@itheima:/$ cd /
itheima@itheima:/$ ls
bin   cdrom  etc   lib    lib64   lost+found  mnt  proc  run   snap  swap.img  tmp  var
boot  dev    home  lib32  libx32  media       opt  root  sbin  srv   sys       usr
```

- 列出了根目录内的东西



### 带有参数使用

语法：

```shell
ls [-选项] [参数]
```

在ls中，参数表示目标路径。

默认`ls`是查看当前所在工作目录的内容，如果不切换看其他目录，可以加参数



示例

```shell
ls /
```

- 列出根目录有啥

示例

```shell
ls /tmp
```

- 列出`/tmp`内有啥



### 带有选项使用

ls的选项超级多，我们学习常用的

- `-l`
- `-a`
- `-h`



#### -l选项

- 表示，将内容以列表（类似Windows的详细信息视图）的形式展示

示例

```shell
itheima@itheima:~$ ls -l
total 32
drwxr-xr-x 2 itheima itheima 4096 Apr 25 03:29 Desktop
drwxr-xr-x 2 itheima itheima 4096 Mar  8 08:43 Documents
drwxr-xr-x 2 itheima itheima 4096 Mar  8 08:43 Downloads
drwxr-xr-x 2 itheima itheima 4096 Mar  8 08:43 Music
drwxr-xr-x 2 itheima itheima 4096 Mar  8 08:43 Pictures
drwxr-xr-x 2 itheima itheima 4096 Mar  8 08:43 Public
drwxr-xr-x 2 itheima itheima 4096 Mar  8 08:43 Templates
drwxr-xr-x 2 itheima itheima 4096 Mar  8 08:43 Videos
```

- 最左侧的`d`表示是文件夹

  - 显示为`-`表示是文件

  - 显示为`l`表示是软连接

    示例

    ```shell
    itheima@itheima:/$ ls -l
    total 3968072
    lrwxrwxrwx   1 root root          7 Sep 11  2024 bin -> usr/bin
    drwxr-xr-x   4 root root       4096 Mar  8 01:18 boot
    dr-xr-xr-x   2 root root       4096 Sep 11  2024 cdrom
    drwxr-xr-x  19 root root       4060 Apr 25 03:17 dev
    drwxr-xr-x 108 root root       4096 Mar  8 08:42 etc
    drwxr-xr-x   3 root root       4096 Mar  8 01:37 home
    lrwxrwxrwx   1 root root          7 Sep 11  2024 lib -> usr/lib
    lrwxrwxrwx   1 root root          9 Sep 11  2024 lib32 -> usr/lib32
    lrwxrwxrwx   1 root root          9 Sep 11  2024 lib64 -> usr/lib64
    lrwxrwxrwx   1 root root         10 Sep 11  2024 libx32 -> usr/libx32
    drwx------   2 root root      16384 Mar  8 01:08 lost+found
    drwxr-xr-x   2 root root       4096 Sep 11  2024 media
    drwxr-xr-x   2 root root       4096 Sep 11  2024 mnt
    drwxr-xr-x   2 root root       4096 Sep 11  2024 opt
    dr-xr-xr-x 316 root root          0 Apr 25 03:17 proc
    drwx------   4 root root       4096 Mar  8 01:37 root
    drwxr-xr-x  26 root root        780 Apr 25 03:44 run
    lrwxrwxrwx   1 root root          8 Sep 11  2024 sbin -> usr/sbin
    drwxr-xr-x   2 root root       4096 Mar  8 01:37 snap
    drwxr-xr-x   2 root root       4096 Sep 11  2024 srv
    -rw-------   1 root root 4063232000 Mar  8 01:15 swap.img
    dr-xr-xr-x  13 root root          0 Apr 25 03:17 sys
    drwxrwxrwt  13 root root       4096 Apr 25 06:49 tmp
    drwxr-xr-x  14 root root       4096 Sep 11  2024 usr
    drwxr-xr-x  13 root root       4096 Sep 11  2024 var
    ```

- 还能显示文件的修改时间，还有大小



#### -a选项

`-a`表示`all`，即显示出来隐藏文件和文件夹

示例

```shell
itheima@itheima:~$ pwd
/home/itheima
itheima@itheima:~$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
itheima@itheima:~$ ls -a
.              .bash_logout  .config   .ssh                       Desktop    Music     Templates
..             .bashrc       .local    .sudo_as_admin_successful  Documents  Pictures  Videos
.bash_history  .cache        .profile  .viminfo                   Downloads  Public
itheima@itheima:~$
```

- 如上，ls看到的内容少
- `ls -a`多一堆内容，多出来的都是隐藏，即都是以`.`开头



#### 选项混用

需求，即以列表显示，还看隐藏

示例

```shell
ls -l -a
```

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425151319.png" alt="image-20260425151319752" style="zoom:50%;" />



示例2

```shell
ls -la
# 或者
ls -al
```

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425151405.png" alt="image-20260425151405674" style="zoom:50%;" />

#### -h选项

来自单词：`humanized`，表示人性化显示文件大小

- 此选项必须搭配`-l`使用

- 可以显示文件大小的`K KB`  `M MB`  `G GB`，小于1K的不显示单位，直接是数字

使用：

```shell
ls -lh
# 或
ls -lah
```

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425151957.png" alt="image-20260425151957363" style="zoom:50%;" />



#### 语法糖`ll`命令

在我们提供的虚拟机`Ububtu`内，可以直接写命令：

```shell
ll
```

效果等同于：`ls -lh`

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425152122.png" alt="image-20260425152122516" style="zoom:50%;" />



## clear命令

清屏命令行

示例

```shell
clear
```



快捷键：

- `ctrl + l`



## 控制符号

- `~`，表示用户家目录
- `.`，表示当前目录
- `..`，表示上一级目录，相当于Windows中的`向上按钮`
- `-`，表示上一次目录，相当于Windows中的`返回按钮`



## 隐藏内容

在Linux中，名字以`.`开头，默认是隐藏的

- 文件夹
- 文件
- 都支持



## 相对和绝对路径

- 以`/`开头的路径写法，绝对路径
- 不以`/`开头的路径写法，相对路径



### 绝对路径

以根目录为起点，描述位置

比如：

```shell
/usr/local/aaa.txt
```

表示，根目录下面的usr文件夹内的local文件夹内的aaa.txt



> 类似，说地址：中国安徽合肥蜀山品恩科技206



### 相对路径

以`当前所在目录为起点`，描述位置

比如：

```shell
desktop/aaa.txt
```

表示，当前目录内的`desktop`文件夹内的`aaa.txt`

- 当前目录，就是`pwd`



> 类似，我在205
>
> 你会自动脑补：中国安徽合肥蜀山品恩科技  205
>
> 因为我在206和你说我在205，你会自动基于你所在位置推断绝对位置





### 示例

```shell
itheima@itheima:~$ # 绝对
itheima@itheima:~$ cd /home/itheima/Downloads
itheima@itheima:~/Downloads$ pwd
/home/itheima/Downloads
itheima@itheima:~/Downloads$ cd
itheima@itheima:~$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos  gb.txt  kb.txt  mb.txt
itheima@itheima:~$ # 相对
itheima@itheima:~$ cd Downloads
itheima@itheima:~/Downloads$ pwd
/home/itheima/Downloads
```





## 查看帮助命令

- `命令 --help` 查看命令的帮助
- `man 命令` 查看更详细的命令手册
  - `空格`翻页
  - `q`退出



> PS:一般也不用，纯英文，没有解释，不及豆包1%



## mkdir 命令

mkdir：make directory

功能：创建文件夹

语法：

```python
mkdir [-p] 路径 ...
```



示例

```python
# 当前目录下创建aaa
mkdir aaa
# 一次型创建多个
mkdir bbb ccc
```



### -p选项

表示创建一连串的目录

示例

```shell
mkdir -p 111/222/333
```

创建如上一连串目录





## touch 命令

功能：创建空文件



语法：

```shell
touch 文件路径 ...
```

示例

```shell
itheima@itheima:~$ # 创建1个文件
itheima@itheima:~$ touch 1.txt
itheima@itheima:~$ ls
1.txt  Desktop    Downloads  Pictures  Templates  aaa  ccc  eee     kb.txt
111    Documents  Music      Public    Videos     bbb  ddd  gb.txt  mb.txt
itheima@itheima:~$ # 创建多个文件
itheima@itheima:~$ touch 2.txt 3.txt
itheima@itheima:~$ ls
1.txt  2.txt  Desktop    Downloads  Pictures  Templates  aaa  ccc  eee     kb.txt
111    3.txt  Documents  Music      Public    Videos     bbb  ddd  gb.txt  mb.txt
```



## cat 命令

功能：查看文件内容，一次型全部在终端显示



示例

```shell
cat /var/log/cloud-init.log
```

- 查看`根目录下面的var文件夹内的log文件夹内的cloud-init.log`文件的内容



### -n选项

功能：显示文件行号

```bash
cat -n /var/log/cloud-init.log
```

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425165246.png" alt="image-20260425165246222" style="zoom:67%;" />





## more 命令

功能：查看文件内容，可以翻页查看，避免`cat`一次型全输出



示例

```bash
more /var/log/cloud-init.log
```

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425165535.png" alt="image-20260425165535132" style="zoom:67%;" />

如图有进度显示，控制快捷键：

- `空格` ，向下翻页
- `b` ，向上翻页
- `q`，退出查看



### -num选项

`-num`的num是数字的意思

示例

```bash
more -10 /var/log/cloud-init.log
```

- 一页是10行的意思
- 不写`-num`默认一页是你当前终端的屏幕行数



## head 命令

功能：查看文件的头部，默认查看前10行

语法：

```bash
head [-num] 文件
```

示例

```bash
itheima@itheima:~$ head /var/log/cloud-init.log
2026-03-08 01:36:52,425 - log_util.py[DEBUG]: Cloud-init v. 25.1.4-0ubuntu0~22.04.1 running 'init-local' at Sun, 08 Mar 2026 01:36:52 +0000. Up 5.90 seconds.
2026-03-08 01:36:52,425 - main.py[INFO]: PID [1] started cloud-init 'init-local'.
2026-03-08 01:36:52,425 - main.py[DEBUG]: No kernel command line url found.
2026-03-08 01:36:52,425 - main.py[DEBUG]: Closing stdin
2026-03-08 01:36:52,426 - util.py[DEBUG]: Writing to /var/log/cloud-init.log - ab: [640] 0 bytes
2026-03-08 01:36:52,427 - util.py[DEBUG]: Changing the ownership of /var/log/cloud-init.log to 0:4
2026-03-08 01:36:52,427 - util.py[DEBUG]: Writing to /var/lib/cloud/data/python-version - wb: [644] 4 bytes
2026-03-08 01:36:52,427 - util.py[DEBUG]: Attempting to remove /var/lib/cloud/instance/boot-finished
2026-03-08 01:36:52,428 - handlers.py[DEBUG]: start: init-local/check-cache: attempting to read from cache [check]
2026-03-08 01:36:52,428 - util.py[DEBUG]: Reading from /var/lib/cloud/instance/obj.pkl (quiet=False)
itheima@itheima:~$ head -5 /var/log/cloud-init.log
2026-03-08 01:36:52,425 - log_util.py[DEBUG]: Cloud-init v. 25.1.4-0ubuntu0~22.04.1 running 'init-local' at Sun, 08 Mar 2026 01:36:52 +0000. Up 5.90 seconds.
2026-03-08 01:36:52,425 - main.py[INFO]: PID [1] started cloud-init 'init-local'.
2026-03-08 01:36:52,425 - main.py[DEBUG]: No kernel command line url found.
2026-03-08 01:36:52,425 - main.py[DEBUG]: Closing stdin
2026-03-08 01:36:52,426 - util.py[DEBUG]: Writing to /var/log/cloud-init.log - ab: [640] 0 bytes
```

如上，默认head查看文件前10行

- `-5`表示查看前5行



## tail 命令

功能：查看文件尾部，默认看10行

语法：

```bash
tail [-num] 文件
```

示例

```bash
itheima@itheima:~$ tail /var/log/cloud-init.log
2026-04-25 03:17:26,692 - util.py[DEBUG]: Writing to /var/lib/cloud/instance/boot-finished - wb: [644] 69 bytes
2026-04-25 03:17:26,692 - handlers.py[DEBUG]: finish: modules-final/config-final_message: SUCCESS: config-final_message ran successfully and took 0.003 seconds
2026-04-25 03:17:26,692 - main.py[DEBUG]: Ran 10 modules with 0 failures
2026-04-25 03:17:26,692 - util.py[DEBUG]: Reading from /proc/uptime (quiet=False)
2026-04-25 03:17:26,692 - util.py[DEBUG]: Reading 12 bytes from /proc/uptime
2026-04-25 03:17:26,692 - atomic_helper.py[DEBUG]: Atomically writing to file /var/lib/cloud/data/status.json (via temporary file /var/lib/cloud/data/tmp4ay2usvl) - w: [644] 501 bytes/chars
2026-04-25 03:17:26,693 - atomic_helper.py[DEBUG]: Atomically writing to file /var/lib/cloud/data/result.json (via temporary file /var/lib/cloud/data/tmpz08lh0iy) - w: [644] 65 bytes/chars
2026-04-25 03:17:26,693 - util.py[DEBUG]: Creating symbolic link from '/run/cloud-init/result.json' => '../../var/lib/cloud/data/result.json'
2026-04-25 03:17:26,693 - performance.py[DEBUG]: cloud-init stage: 'modules-final' took 0.065 seconds
2026-04-25 03:17:26,693 - handlers.py[DEBUG]: finish: modules-final: SUCCESS: running modules for final
itheima@itheima:~$ tail -3 /var/log/cloud-init.log
2026-04-25 03:17:26,693 - util.py[DEBUG]: Creating symbolic link from '/run/cloud-init/result.json' => '../../var/lib/cloud/data/result.json'
2026-04-25 03:17:26,693 - performance.py[DEBUG]: cloud-init stage: 'modules-final' took 0.065 seconds
2026-04-25 03:17:26,693 - handlers.py[DEBUG]: finish: modules-final: SUCCESS: running modules for final
```

- 默认看尾巴10行
- `-3`，看尾巴3行



### -f选项

-f：follow

功能：持续的跟踪文件的改变



如果要退出，按：`ctrl + c`



## cp 命令

cp：copy

功能：复制文件或文件夹，到指定地方，并可以改名



语法：

```bash
cp [-r] src dst
```

- `-r`，可选，用于复制文件夹
- `src`，被复制的
- `dst`，要复制去的地方和命名



示例

```bash
cp 1.txt 2.txt
```

- 将1.txt复制到当前文件夹下，作为2.txt存在

示例

```bash
# 前提：当前目录有一个文件夹aaa
cp 1.txt aaa	# 将1.txt 复制到aaa文件夹内，名字不变还是1.txt

# 前提：当前目录没有aaa文件夹
cp 1.txt aaa	# 将1.txt复制到当前文件夹，改名为aaa

# 前提：当前目录有一个文件夹aaa
cp 1.txt aaa/2.txt		# 复制1.txt到aaa内，改名为2.txt
```

- 目的地是文件夹就放进去
- 不是文件夹就改名



示例

```bash
# 前提：当前目录有一个文件夹aaa
cp -r aaa bbb			# 将文件夹复制到当前目录内，改名为bbb
```

- 操作文件夹需要`-r`





## mv 命令

mv：move

功能：移动文件或文件夹，到指定地方，可以改名



语法：

```bash
mv src dst
```

- 没有`-r`，对文件或文件夹不需要`-r`
- `src`，被移动的
- `dst`，要移动去的地方或命名的名字





示例

> mv对文件或文件件操作没区别

```bash
# 前提：当前目录没有itcast这个文件夹
mv itheima itcast		# 将itheima文件夹改名为itcast

# 前提：当前目录真的有itcast这个文件夹
mv kb.txt itcast		# 将kb.txt文件移动到itcast文件夹内，名字不变

# 前提：当前目录真的有itcast这个文件夹
mv mb.txt itcast/666.txt	# 将mb.txt 移动到itcast文件夹内，改名为666.txt

# 额外说明，如果上面命令，没有itcast这个文件夹，会报错
```



## root 用户

表示，Linux中的超级管理员，拥有全部权限

root用户的家目录：`/root`



## su 命令

功能：切换用户

语法：

```bash
su - 用户名
```

示例：

```bash
su - root
```

- 切换到root用户

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425174610.png" alt="image-20260425174609973" style="zoom:67%;" />

如上图，输入密码：`123456`切换到root用户



![image-20260425174652433](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425174652.png)

如图，终端的提示：

- `@`符号之前，表示你登录的用户是啥
- `@`符号之后，表示你登录的服务器的主机名是啥（主机名，就是电脑的名字）





## exit 命令

功能，退出当前的用户登录

语法：

```bash
exit
```

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425174839.png" alt="image-20260425174839055" style="zoom:67%;" />

如上图，登录了root用户，在输入`exit`回到了`itheima`用户



## sudo 命令

sudo：super user doing

功能：给当前命令，临时提供`root`权限



语法：

```bash
sudo 命令
```

示例

```bash
itheima@itheima:~$ ls /root
ls: cannot open directory '/root': Permission denied
itheima@itheima:~$ sudo ls /root
[sudo] password for itheima:
itheima@itheima:~$ touch /root/1.txt
touch: cannot touch '/root/1.txt': Permission denied
itheima@itheima:~$ sudo touch /root/1.txt
itheima@itheima:~$ ls /root
ls: cannot open directory '/root': Permission denied
itheima@itheima:~$ sudo ls /root
```

如上操作，在`/root`的操作

- 在用户还是`itheima`前提下，带上sudo，就等于管理员执行
- 第一次用需要输入自己账户密码
- 下次退出后再用还是要输入密码



## rm 命令

rm：remove

功能：删除文件或文件夹

语法

```bash
rm [-r] [-f] 文件或文件夹 ...
```

- `-r`可选，用于删除文件夹
- `-f`可选，强制删除（不提示直接删）
- 文件或文件夹可以是多个，空格分隔即可



示例

```bash
rm 1.txt		# 删除1.txt

rm 2.txt 3.txt	# 删除这2个文件
```

示例

```bash
rm -r bbb		# 删除bbb文件夹
```



示例

```bash
rm -rf ccc		# 删除ccc文件夹（强制，不提示）
```



### 通配符

在Linux系统中，`*`代表匹配全部

- 类似Python正则中的：`.*`效果



示例

```bash
rm -rf *.txt		# 删除全部.txt结尾的文件和文件夹

rm *.txt			# 删除全部.txt结尾的文件
```

示例

```bash
rm -rf *test*		# 删除全部名字中包含test的文件或文件夹
```



示例

```bash
rm -rf aaa/*		# 删除aaa文件夹内的全部东西
```



### 注意

删除是高危操作，执行rm命令之前一定要仔细确认

删除是高危操作，执行rm命令之前一定要仔细确认

删除是高危操作，执行rm命令之前一定要仔细确认

删除是高危操作，执行rm命令之前一定要仔细确认

删除是高危操作，执行rm命令之前一定要仔细确认

删除是高危操作，执行rm命令之前一定要仔细确认

删除是高危操作，执行rm命令之前一定要仔细确认



如果你是普通用户，可能删除掉有用的内容

如果你root用户，可能啥都删掉，包括操作系统本身



一定不要写：

一定不要写：

一定不要写：

```bash
rm -rf /*

# 或者
sudo rm -rf /*
```



## apt 命令

Linux安装软件，离线安装包比较复杂，Linux好处是维护了超级丰富的`软件商店`



apt命令联网安装软件（需要管理员权限）

语法：

```bash
apt install 软件名 -[y]
```

如果你是普通用户

```bash
sudo apt install 软件名
```



示例，安装`gedit`（文本编辑器），即类似Windows的记事本

```bash
sudo apt install gedit
```

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/25/20260425181544.png" alt="image-20260425181544751" style="zoom:67%;" />



跳过提示，可以

```bash
sudo apt install gedit -y
```



## echo 命令

作用：等同于Python的print，将内容输出到控制台（终端命令行中）

语法：

```bash
echo 内容...

# 如果内容复杂可以用""包围
echo "你好帅"
```



## 重定向符号

重定向：将输出内容重新定向到指定的文件中



- `>` 覆盖重定向
- `>>` 追加重定向



示例

```bash
echo 你好帅 > 1.txt
```

将左侧命令的结果，覆盖写入1.txt（1.txt不存在会自动创建文件）



示例

```bash
ls / >> 2.txt
```

将左侧命令的结果，追加写入到2.txt





## tar命令



### 压缩格式

Windows系统常见的：

- `.zip`压缩包
- `.rar`压缩包



Linux系统中常见的：

- `.tar`压缩包  等同于打个包成为整体，没啥太好的压缩效果
- `.tar.gz`压缩包  应用`gzip`压缩算法，进行打包，有一定的压缩效果
- `.zip`



### 打包.tar

> .tar文件压缩率比较低，基本没啥体积缩小的效果

多个文件，打包为1个压缩包文件

语法

```bash
tar -cvf 压缩文件.tar  被打包的...
```

- 被打包的是多个文件或文件夹

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426095340.png" alt="image-20260426095340548" style="zoom:67%;" />

如图，`.tar`压缩率较低，基本没啥体积缩小效果，就是简单的多个文件合为一个包而已。



### 打包.tar.gz



语法：

```bash
tar -zcvf 压缩文件.tar.gz  被打包的...
```

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426100056.png" alt="image-20260426100056367" style="zoom:67%;" />

如上，打包为`.tar.gz`就有很大的体积减少效果。





### 解压.tar

语法：

```bash
tar -xvf xxx.tar [-C 目录]
```

- `-xvf`解包
- `xxx.tar`被解包的
- `-C`，注意是大写C，可选，表示解压到哪里，默认是当前文件夹

示例

```bash
itheima@itheima:~$ tar -xvf b.tar
1.txt
2.txt
itheima@itheima:~$ ll
total 170M
-rw-rw-r-- 1 itheima itheima  80M Apr 26 01:52 1.txt
-rw-rw-r-- 1 itheima itheima 5.7M Apr 26 01:52 2.txt
drwxr-xr-x 2 itheima itheima 4.0K Apr 25 10:17 Desktop
drwxr-xr-x 2 itheima itheima 4.0K Mar  8 08:43 Documents
drwxr-xr-x 2 itheima itheima 4.0K Mar  8 08:43 Downloads
drwxr-xr-x 2 itheima itheima 4.0K Mar  8 08:43 Music
drwxr-xr-x 2 itheima itheima 4.0K Mar  8 08:43 Pictures
drwxr-xr-x 2 itheima itheima 4.0K Mar  8 08:43 Public
drwxr-xr-x 2 itheima itheima 4.0K Mar  8 08:43 Templates
drwxr-xr-x 2 itheima itheima 4.0K Mar  8 08:43 Videos
-rw-rw-r-- 1 itheima itheima  10K Apr 26 01:51 a.tar
-rw-rw-r-- 1 itheima itheima  85M Apr 26 01:53 b.tar
-rw-rw-r-- 1 itheima itheima 169K Apr 26 01:54 c.tar
drwxrwxr-x 2 itheima itheima 4.0K Apr 26 01:50 itheima
```

- 将b.tar的内容解压到当前文件夹



示例

```bash
itheima@itheima:~$ ls
Desktop    Downloads  Pictures  Templates  a.tar  b.tar  itheima
Documents  Music      Public    Videos     aaa    c.tar
itheima@itheima:~$ ls aaa
itheima@itheima:~$ tar -xvf b.tar -C aaa
1.txt
2.txt
itheima@itheima:~$ ls
Desktop    Downloads  Pictures  Templates  a.tar  b.tar  itheima
Documents  Music      Public    Videos     aaa    c.tar
itheima@itheima:~$ ls aaa
1.txt  2.txt
```

- 将b.tar的内容，解压到aaa文件夹内



### 解压.tar.gz

语法

```bash
tar -zxvf xxx.tar [-C 目录]
```



示例

```bash
# 解压内容到当前文件夹
tar -zxvf c.tar.gz

# 解压内容到aaa文件夹内
tar -zxvf c.tar.gz -C aaa
```



### 总结

| 命令 | .tar                             | .tar.gz                           |
| ---- | -------------------------------- | --------------------------------- |
| 压缩 | tar -cvf xxx.tar 文件或文件夹... | tar -zcvf xxx.tar 文件或文件夹... |
| 解压 | tar -xvf xxx.tar [-C 目录]       | tar -zxvf xxx.tar [-C 目录]       |



### 扩展，解压zip

语法：

```bash
unzip xxx.zip
```



## 文件的上传和下载



自己Windows电脑的内容如何上传到虚拟机，由如何从虚拟机下载回来。



使用命令：`sftp`（在Windows执行）

语法：

```bash
sftp itheima@192.168.88.100
```

- `ssh`远程登录协议，登录服务器敲命令
- `sftp`远程文件传输协议，登录服务器搞文件上传下载





### 查看与切换目录

```
ls           # 远程目录列表
lls          # 本地目录列表
pwd          # 远程当前路径
lpwd         # 本地当前路径
cd /远程/路径 # 切远程目录
lcd D:\本地路径 # 切本地目录（Windows 用 \）
```

### 上传（put）

```
put 本地文件.txt          # 上传到远程当前目录
put D:\a\b.txt /remote/   # 指定远程路径
put -r 本地文件夹          # 上传整个文件夹
```

### 下载（get）

```
get 远程文件.txt           # 下载到本地当前目录
get /remote/b.txt D:\a\   # 指定本地路径
get -r 远程文件夹          # 下载整个文件夹
```

### 退出

```
exit
# 或
bye
```







## VIM编辑器



功能：在命令行下完成文件的编辑操作（命令行内的文本编辑器（记事本））



### 快速体验

> 先确保输入法是英文

1. 如果你linux有a.py请先rm a.py 删掉
2. vim a.py
3. 输入： i
4. print("Hello Linux")
5. 按一下 esc
6. 输入  :wq
7. 执行  python3 a.py  运行这个代码

> 这个操作就是，创建1个a.py的文件，编写代码保存退出，并执行py代码





### 模式

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426112830.png" alt="image-20260426112830411" style="zoom:67%;" />

vim使用的时候有3个模式：

1. 命令模式，可以按键盘控制内容
2. 插入模式，可以打字编辑
3. 底线命令模式，控制整个文件



### 命令模式

vim进入直接就是命令模式，快捷指令：

| 按键     | 效果                                              |
| -------- | ------------------------------------------------- |
| 上下左右 | 光标上下左右                                      |
| hjkl     | 光标上下左右（h左，l右，j下，k上）                |
| PgUp     | 向上翻页                                          |
| PgDn     | 向下翻页                                          |
| 0        | 光标移动到当前行最左侧                            |
| $        | 光标移动到当前行最右侧                            |
| /        | 开始搜索，输入搜索内容回车                        |
| n        | 在搜索中，找下一个                                |
| N        | 在搜索中，找上一个                                |
| dd       | 删除当前行                                        |
| ndd      | 删除n行，比如3dd从当前行向下删除3行（包含当前行） |
| yy       | 复制当前行                                        |
| nyy      | 复制n行，比如3yy从当前行向下复制3行（包含当前行） |
| p        | 粘贴复制的内容                                    |
| u        | 撤销                                              |
| ctrl + r | 反向撤销                                          |
| gg       | 光标跳到文件头部                                  |
| G        | 光标跳到文件底部                                  |
| dgg      | 从当前行向上全部删除（包含当前行）                |
| dG       | 从当前行向下全部删除（包含当前行）                |
| d$       | 从光标位置向右全删除                              |
| d0       | 从光标位置向左全删除                              |

进入插入模式的按键

| 按键 | 效果                                 |
| ---- | ------------------------------------ |
| i    | 光标当前位置开始编辑                 |
| a    | 光标当前位置右侧一个字符位置开始编辑 |
| I    | 当前行头部开始编辑                   |
| A    | 当前行尾部开始编辑                   |
| o    | 下一行开始编辑                       |
| O    | 上一行开始编辑                       |



### 插入模式

通过命令模式的：`i a I A o O`进入

通过`esc`按键回退到命令模式



在插入模式内，左下角会提示![image-20260426113636905](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426113637.png)

正常打字编辑即可



### 底线命令模式

> 必须从命令模式进入

进入，输入`:`

- w，保存编辑内容，不退出
- q，单纯的退出
- wq，保存并退出
- q!，放弃修改直接退出
- set nu，显示文件行号



### 扩展 练习

尝试修改固定IP地址，默认地址是192.168.88.100

可以修改为192.168.88.101等



修改文件是：

> 需要root权限

```bash
sudo vim /etc/netplan/50-cloud-init.yaml
```

![image-20260426115945560](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426115945.png)



### 重启网卡

```bash
sudo systemctl restart network
```

- systemctl 是控制操作系统内部服务的启动和关闭，需要root权限

```bash
systemctl restart|start|stop|status 服务名
```

- restart重启
- start启动
- stop关闭
- status查看状态





# Docker的使用

## 基础概念【了解】

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426150705.png" alt="image-20260426150705025" style="zoom:67%;" />

需求：我有10款不同的应用程序开发完成，要交付给客户电脑中部署。

### 方案A：

创建10个虚拟机，每个虚拟机针对我们的程序安装各类依赖，配置环境，部署程序，搞定后将10个虚拟机打包为压缩包发给客户。

- 10个虚拟机，每个体积20GB，运行内存占用单个2G，共20GB
- 客户收到后，打开VMware，导入10个虚拟机，启动10个虚拟机
- 共占用客户硬盘空间200GB，内存20GB
- 10个程序本身，只有1GB大小，内存也只需要1GB

优点：

- 开箱即用，客户只要有VMware，导入虚拟机开机即可，内部各类复杂配置都做好了

缺点：

- 性能垃圾，跑了10个完整的操作系统，服务10个程序
- 90%的内存和CPU占用，都服务这10个虚拟机内的操作系统了
- 仅有10%的内存和CPU用于我们自己的程序



### 方案B：

基于Docker技术，创建10个容器，每个容器针对10个程序进行配置，将10个容器打包发给客户

客户只需要有Docker软件即可，运行10个容器

- 10个容器，每个200MB，运行内存占用100MB
- 客户运行10个容器，共占用硬盘2GB，内存1GB
- 因为10个容器，共用客户电脑的同一个操作系统



优点：

- 开箱即用，客户只要有Docker软件，导入容器启动即可，内部复杂配置都做好了
- 资源占用极低（对比VMware完整虚拟机）

缺点：

- 木有
- Docker的安装比VMware复杂
  - VMware小白也会装
  - Docker基于Linux系统运行，小白不一定装得好





### 对比

| 对比                           | 硬件           | 操作系统                   | 虚拟化层次                                             |
| ------------------------------ | -------------- | -------------------------- | ------------------------------------------------------ |
| 不同的VMware虚拟机在运行的时候 | VMware虚拟硬件 | 每个虚拟机一个完整操作系统 | 完整虚拟化，可以运行完整操作系统                       |
| 不同的Docker容器在运行的时候   | 共用真实硬件   | 共用一个操作系统           | 不完全虚拟化，使用真实操作系统，不同容器做运行环境隔离 |





### 介绍

Docker是一种容器虚拟化技术，可以在一台电脑上，做到提供不同的隔离环境，供不同的程序使用。

所有程序共用电脑的操作系统、底层硬件，仅在各自的运行环境上，做隔离。







## Docker基础使用

2种使用Docker的姿势：

1. 自己创建Docker容器，供别人用
2. 下载别人的Docker容器，给自己用



我们主要用Docker，下载别人做好的容器，运行。

Docker有一个Docker hub的网站，里面有全球范围内开发者开发的各类容器：



### docker启动关闭

```bash
# 启动
sudo systemctl start docker
# 关闭
sudo systemctl stop docker
# 查看状态
sudo systemctl status docker
```

查看状态

![image-20260426155437590](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426155437.png)





### 拉取MySQL容器（网络不好可以跳过）

```bash
# 联网下载官方提供的MySQL镜像
sudo docker pull mysql:8.0
```



### 离线导入MySQL容器（上面如果成功，这里可以跳过）

导入别人做好的MySQL容器，导入到Docker内，启动就可以得到MySQL软件。



在课程资料中，可以找到：`mysql8.tar`



上传到Linux虚拟机内。



执行命令导入这个MySQL8容器（镜像）

```bash
sudo docker load -i mysql8.tar
```

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426163956.png" alt="image-20260426163955962" style="zoom:67%;" />

检查是否导入成功

```bash
sudo docker images
```

![image-20260426164049876](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426164049.png)



### 运行MySQL8容器

命令

```bash
sudo docker run -d --name mysql8 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql:8.0
```

- docker run,运行容器
- -d，后台执行，运行后没什么感知
- --name，给这个容器起个名字
- -p，指定mysql的运行端口   3306mysql默认的运行端口
- -e MYSQL_ROOT_PASSWORD，默认设置root用户密码为123456
- mysql:8.0，你要运行的镜像是什么（刚刚离线导入的）

![image-20260426170205296](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426170205.png)



### 检查MySQL8容器运行

命令

```bash
sudo docker ps
```

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426170249.png" alt="image-20260426170249803" style="zoom:67%;" />

能看到，就说明容器运行正常



### 设置MySQL可以远程登录

MySQL默认绑定在：`127.0.0.1:3306`，即只允许本地连接。



命令

```bash
sudo docker exec -it mysql8 mysql -uroot -p123456
```

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426170605.png" alt="image-20260426170605276" style="zoom:67%;" />

能看到`mysql >`一切正常



在执行2条命令即可

```bash
ALTER USER 'root'@'%' IDENTIFIED BY '123456';
FLUSH PRIVILEGES;
```



### Python接入Docker中的MySQL（测试连接）



安装第三方库

- （Windows系统操作）打开anaconda prompt软件，执行下面命令

```python
pip install pymysql -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```





# MySQL

## DataGrip软件的安装和使用

1. 找到安装包，一路下一步安装即可，安装好后运行软件

2. 提示

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426180418.png" alt="image-20260426180418316" style="zoom:50%;" />

   点击`continue`

3. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426180441.png" alt="image-20260426180440869" style="zoom:67%;" />

4. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426180604.png" alt="image-20260426180604085" style="zoom:67%;" />

5. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426180626.png" alt="image-20260426180626384" style="zoom:67%;" />

6. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426180659.png" alt="image-20260426180658881" style="zoom:67%;" />

7. 随便起个名字

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426180724.png" alt="image-20260426180723845" style="zoom:67%;" />

8. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426180818.png" alt="image-20260426180818054" style="zoom:67%;" />

9. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426181031.png" alt="image-20260426181031055" style="zoom:67%;" />

10. ![image-20260426180910632](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426180910.png)

11. 上图下载中等待完成，完成后如下图操作

12. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426181108.png" alt="image-20260426181108384" style="zoom:67%;" />

13. ![image-20260426181124878](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426181125.png)

14. ![image-20260426181239044](https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/26/20260426181239.png)

15. 如图一切正常





## 数据库的概念

数据库是一种电子化的信息集合。

数据库的常见组织形式分3个层级：

- 库
- 表
- 行



如果想要在电脑中使用数据库，需要借助数据库管理软件实现。

常见的数据库管理软件（DBMS）有：

- `MySQL`，全球范围内最知名开源数据库
- `PostgreSQL`，全球范围内知名数据库
- `Oracle`，知名收费数据库



借助MySQL，就能在你电脑中提供电子化的数据集合和管理。

### MySQL的数据组织层级

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/28/20260428094736.png" alt="image-20260428094735902" style="zoom:67%;" />

借助MySQL软件，可以帮助我们维护三个层级：

- 库层级（Database、Schema），MySQL可以维护多个库，每个库内部有多个表
- 表层级（Table），每个库内有多个表，每个表就是一个二维表格（有行有列）
- 行层级（Row），每个表内，是多个数据行和数据列，每一条数据称之为数据行



### SQL概念

MySQL软件可以维护电子化的信息集合，对于这些数据的操作，使用`sql`语言来完成。



SQL：结构化查询语言，是一种"编程语言"，专为操作数据库管理软件而设计。

通过SQL语言，可以完成数据的存入、删除、修改、查询等操作。



学习数据库本身就是学习SQL语法。





### MySQL的连接

MySQL本身是CS架构，即MySQL是服务器，需要用客户端连接使用。



2种方式：

- CLI命令行中，登录，CLI命令行就是客户端
- 第三方软件，`DataGrip`，连接使用



#### CLI连接

命令：

```bash
sudo docker exec -it mysql8 mysql -uroot -p
```

- `sudo docker exec -it mysql8`，是Docker命令，表示要对MySQL8这个容器执行命令
- `mysql -uroot -p`，是mysql自身的客户端登录命令
  - `-uroot`，表示账户名是root
  - `-p`用密码认证



如下：

```bash
itheima@itheima:~$ sudo docker exec -it mysql8 mysql -uroot -p
Enter password:  # 密码输入的时候没反应
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.46 MySQL Community Server - GPL

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```





#### DataGrip的连接

略，参考上文



## SQL语法

学习数据库，学习SQL语法操作数据库



### SQL分类

```sql
DDL: 数据定义语言:简称DDL(Data Definition Language)
        作用: 用来定义数据库对象：数据库，表，列/字段等。
        关键字: create，drop，alter等

DML: 数据操作语言:简称DML(Data Manipulation Language)
        作用:用来对数据库中表的记录进行更新。
        关键字: insert，delete，update等

DQL: 数据查询语言:简称DQL(Data Query Language)
        作用:用来查询数据库中表的记录。
        关键字: select，from，where等

DCL: 数据控制语言：简称DCL(Data Control Language)
        用来定义数据库的访问权限和安全级别，及创建用户。
```

- DDL ，建库建表，删库删表
- DML，新增删除修改数据
- DQL，查询查看数据
- DCL，控制MySQL数据库本身，权限、安全认证、密码修改、账户创建



我们主要学习：DDL、DML、DQL

DCL不学习，运维工程师专供



### DataGrip中写SQL

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/28/20260428100730.png" alt="image-20260428100730670" style="zoom:67%;" />



### SQL通用语法



1. SQL语句可以换行写，但是一个SQL语句必须以`;`结尾

   ```sql
   select 
       * 
   from 
       db;
   ```

2. SQL语法中，空格和缩进不算代码，可以随意添加

   ```sql
   select 
                  * 
                                 from 
       db;
   ```

   如上，空格可以随意加，不影响，`;`必须有

3. SQL不区分大小写

   ```sql
   SeLeCt
                  *
                                 FROm
       db;
   ```

4. 注释

   1. 单行注释：

      1. `#`开头，建议`#` 后有一个空格
      2. `--`开头，必须`--`后有一个空格

   2. 多行注释：

      以`/*开头` 以 `*/`结尾

   ```sql
   SeLeCt
       # 我是注释
       -- 我是注释
       /*
        我是
        注释
        哈哈哈
        */
                  *
                                 FROm
       db;
   ```





### 数据库操作语法

##### 创建语法

```sql
CREATE DATABASE [IF NOT EXISTS] 数据库名字 [CHARSET UTF8];
```

示例

```sql
CREATE DATABASE hf1;

CREATE DATABASE IF NOT EXISTS hf1;

CREATE DATABASE IF NOT EXISTS hf2 CHARSET UTF8;
```



##### 删除

```sql
DROP DATABASE [IF EXISTS] 数据库名字;
```





##### 选择数据库

后续对表的操作，需要确定是哪个库，可以通过语法，先锁定库

```sql
USE 数据库名字;
```



##### 查看当前锁定的库

```sql
SELECT database();
```



##### 查看有哪些库在MySQL内

```sql
SHOW DATABASES;
```



### 数据类型

创建表需要指定列的类型，通过类型决定能存储什么数据。



字符串类型：

- `varchar(num)`，num表示最大长度范围：0~255
- `text`，文本字符串类型，长度不限

数字：

- `int`，整数
- `float`
- `decimal(m, n)`  m总长度，n小数长度
  - `decimal(10, 2)`，最大支持：总长度为10，小数为2

日期

- `date`， 2026-04-28的年月入结构
- `datetime`，2026-04-28 10:00:00 年月日时分秒结构
- `year`，2026，纯年份



### 表操作

做表的操作之前，请先确定你要操作的库

#### 创建表

```sql
CREATE TABLE [IF NOT EXISTS] 表名称(
	列1名称 类型 [约束...], 
	列2名称 类型 [约束...], 
	列3名称 类型 [约束...], 
    ...
	列n名称 类型 [约束...]
);
```

```sql
# 记录学生信息的表
# id、name、age、gender、height
CREATE TABLE IF NOT EXISTS stu2(
    id INT ,
    name VARCHAR(20),
    age INT,
    gender VARCHAR(5),
    height DECIMAL(10, 2)
);
```



#### 表删除

语法：

```sql
DROP TABLE [IF EXISTS] 表名称;
```



#### 查看库中有哪些表

语法：

```sql
SHOW TABLES;
```



#### 查看表详情

语法：

```sql
DESC 表名称;
```



#### 列的约束

在SQL中，创建表可以提供列的约束

- `primary key`主键约束，表示这个列不可以为`null`也不能值重复
- `auto_increment`，自增约束，可以让列不提供值，自动+1，一般搭配主键使用
- `not null`，非空约束，不允许值为空
- `unique`，唯一约束，不允许这个列的值重复
- `default`，默认约束，如果不给列提供值，则使用默认值
- `foreign key` 外键约束，用来联系2个有关系的表



示例

```sql
create table student(
	id int primary key auto_increment, 
    name varchar(255) not null, 
    sfz varchar(18) unique, 
    gj varhcar(255) default '中国', 
);
```





### 数据行操作



#### 插入数据行操作

语法：

```sql
INSERT INTO 表名[(列的列表)] VALUES (数据集)[, (数据集)...];
```

- `[]`表示可选
- `...`，表示数量任意



示例1

```sql
INSERT INTO stu VALUES (4, '林军杰', 11, '男', 172.66);
```

- 按照类似Python位置传参的模式，将5份数据提供给5个列，一一对应
- 字符串要求`''`包围



示例2

```sql
INSERT INTo stu VALUES (5, '王小锤', 22, '女', 175.68),
                       (6, '王小锤锤', 22, '女', 175.68),
                       (7, '王大小锤', 22, '女', 175.68);
```

- 一次型插入3条数据



示例3

```sql
INSERT INTO stu(id, name) VALUES (8, '旺达小锤锤');
```

- 如上，仅为id和name 2个列提供数据值





#### 更新（修改）数据行

语法：

```sql
UPDATE 表名称 SET 列=值 [WHERE 条件];
```

示例

```sql
update stu set age=11;
```

- 全部age改11



示例

```sql
# 修改王大锤年龄为22
update stu set age=22 where name='王大锤';

# 修改男的年龄为22
update stu set age=22 where gender='男';

# id >= 5改为age=5
update stu set age=5 where id>=5;
```

- 带有条件更新，where等同于Python的if判断



#### 删除数据行

语法：

```sql
DELETE FROM 表 [WHERE 条件];
```

示例

```sql
delete from stu;
```

- 删除全部

示例

```sql
# 删除id为1的信息
delete from stu where id=1;
# 删除id>6
delete from stu where id>6;
```

- 带条件删除



#### 删除全部数据行

语法：

```sql
TRUNCATE 表名称;
```



区别：

- `delete from 表`，一条条删除，慢
- `truncate 表`，删除整个表，重新创建，快





### 单表查询

#### 数据准备

```sql
# 创建数据库: create database 库名;
CREATE DATABASE IF NOT EXISTS my_db CHARSET=utf8;

# 使用数据库: use 库名;
USE my_db;

# 创建表: create table 表名(字段名 字段类型 [约束],...);
# 建测试表
drop table if EXISTS products;
CREATE TABLE IF NOT EXISTS products
(
    id          INT PRIMARY KEY AUTO_INCREMENT, -- 商品ID
    name        VARCHAR(24)    NOT NULL,        -- 商品名称
    price       DECIMAL(10, 2) NOT NULL,        -- 商品价格
    score       DECIMAL(5, 2),                  -- 商品评分，可以为空
    is_self     VARCHAR(8),                     -- 是否自营
    category_id INT                             -- 商品类别ID
);

drop table if EXISTS category;
CREATE TABLE IF NOT EXISTS category
(
    id   INT PRIMARY KEY AUTO_INCREMENT, -- 商品类别ID
    name VARCHAR(24) NOT NULL            -- 类别名称
);

# 插入数据: insert into 表名 (字段名,字段名) values(字段值,字段值),(字段值,字段值);
# 添加测试数据
INSERT INTO category
VALUES (1, '手机'),
       (2, '电脑'),
       (3, '美妆'),
       (4, '家居');

INSERT INTO products
VALUES (1, '华为Mate50', 5499.00, 9.70, '自营', 1),
       (2, '荣耀80', 2399.00, 9.50, '自营', 1),
       (3, '荣耀80', 2199.00, 9.30, '非自营', 1),
       (4, '红米note 11', 999.00, 9.00, '非自营', 1),
       (5, '联想小新14', 4199.00, 9.20, '自营', 2),
       (6, '惠普战66', 4499.90, 9.30, '自营', 2),
       (7, '苹果Air13', 6198.00, 9.10, '非自营', 2),
       (8, '华为MateBook14', 5599.00, 9.30, '非自营', 2),
       (9, '兰蔻小黑瓶', 1100.00, 9.60, '自营', 3),
       (10, '雅诗兰黛粉底液', 920.00, 9.40, '自营', 3),
       (11, '阿玛尼红管405', 350.00, NULL, '非自营', 3),
       (12, '迪奥996', 330.00, 9.70, '非自营', 3);
```

复制粘贴这些SQL，在DataGrip中选中这部分代码，`ctrl + enter`即可执行。



#### 完整的查询语法

```sql
SELECT ..列列表|聚合函数|*... FROM 表 
[WHERE 条件] 
[GROUP BY 列]
[HAVING 条件]
[ORDER BY 列]
[LIMIT 条件]
```





#### 基础查询

语法：

```sql
SELECT *|列列表|distinct 列 [[AS] 别名] FROM 表;
```

示例

```sql
# 查询表中全部行和全部列
# * 表示查询全部列
select * FROM products;

# 查询name和price2个列
select name, price FROM products;

# 信息去重
select distinct is_self FROM products;

# 别名，别名不需要''包围，AS本身可以不用写
select name as 商品名, price 价格 FROM products;
```



#### 条件查询

使用`where`完成内容的过滤（满足条件方可显示）

```sql
SELECT ... FROM 表 WHERE 条件;
```





##### where 比较运算

- `>` 大于
- `<` 小于
- `=` 等于
- <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/28/20260428144112.png" alt="image-20260428144112501" style="zoom:67%;" /> 小于等于
- <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/28/20260428144132.png" alt="image-20260428144132411" style="zoom:67%;" />大于等于
- <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/28/20260428144153.png" alt="image-20260428144152936" style="zoom:67%;" /> 不等于

```sql
# 查询价格大于1000
select * from products where price>1000;
# 查询id为3的商品的name和price
select name, price from products where id=3;
# 查询商品分数小于9.5分的商品全部信息
select * from products where score<9.5;
```

- `select xxx` 确定查询哪些列
  - `select name, price`，查看name和price列
- `from 表`,确定哪个表被查
- `where 条件`,条件做判断，符合条件的出现在结果中

> 顺序不要乱，SQL写起来就是：
>
> SELECT ... -> FROM ... -> WHERE ...





##### where 逻辑判断

- `and`
- `or`
- `not`

示例

```sql
# 查询价格小于4000 且大于1000的商品
select * from products where price<4000 and price>1000;
# 查询价格小于1000，或者分数大于9.5分
select * from products where price < 1000 or score > 9.5;
# 不是自营的商品
select * from products where not is_self='自营';
```



##### where 范围判断

- 连续范围
- 非连续范围



连续范围

```sql
where 列 between num1 and num2;
```

- 表示列的值在num1和num2之间（包含num1和num2）

示例

```sql
# 查询价格小于等于4000 且大于等于1000的商品
select * from products where price<=4000 and price>=1000;		# 写法1
select * from products where price between 1000 and 4000;		# 写法2 between and
```



非连续范围

```sql
where 列 [not] in (值, 值, 值...);
```

示例

```sql
# 查询商品分数是9.2 或 9.5 或 9.7的商品全部信息
select * from products where score in (9.2, 9.5, 9.7);
# 上面写法等于： score = 9.2 or score = 9.5 or score = 9.7
# 查询商品分数不不不不不是9.2 或 9.5 或 9.7的商品全部信息
select * from products where score not in (9.2, 9.5, 9.7);
```



##### 模糊查询

只用于字符串

语法：

```sql
where 列 like '';
```

- `_`，字符数量1个字符，匹配内容随意
  - 类似python正则 `.`
- `%`，字符数量任意，匹配内容随意
  - 类似Python正则 `.*`



示例

```sql
# 找出名字为xxMate50的商品
# xx是任意字符数量为2
select * from products where name like '__Mate50';

# 找出名字内包含数字1的商品
select * from products where name like '%1%';

# 找出华为开头的商品
select * from products where name like '华为%';
```



##### 非空匹配

> - 在Python中，空内容：`None`
> - 在SQL中，空内容：`null`

示例

```sql
# 找null
select * from products where score is null;
# 找非null
select * from products where score is not null;
```



#### 聚合函数

> 作用：将一批输出传入，计算一个结果

- `count(列|*)`，计算数量
- `sum(列)`，计算列的和
- `avg(列)`,计算列的平均
- `min(列)`，计算列的最小值
- `max(列)`，计算列的最大值



语法

```sql
select 聚合函数... from 表;
```

- 在不写`group by`情况下，select中必须全部是聚合

示例

```sql
# 找出价格之和
select sum(price) from products;
# 找出平均价格
select avg(price) as 平均价 from products;
# 找出最小分数
select min(score) from products;
# 找出最大分数
select max(score) from products;

# 找出价格的数量
select count(price) from products;
# 找出有多少个有效分数，如果是null不计数
select count(score) from products;

# 找出行，count(*)统计行数
select count(*) from products;

#
select max(score), avg(score), min(score), max(score), count(score) from products;
```



#### 分组操作

> 作用：将数据按指定列的值，分为不同组。使用聚合统计不同组的聚合结果。

语法：

```sql
select 分组列, 聚合... from 表
group by 列;
```

示例

```sql
# 统计平均价格，要求自营和非自营分开统计
select is_self, avg(price) from products group by is_self;
# 统计最大和最小价格，要求自营和非自营分开统计
select max(price), min(price), is_self from products group by is_self;
```

- 注意，当使用聚合的时候，group by哪个列，哪个列才能在select中搭配聚合一起写



#### 排序操作

> 作用：对已经计算好的结果集，按指定列重新排序

语法：

```sql
select ...
from ...
where ...
group by ...
order by 列 ([ASC]|DESC)[, 列 ([ASC]|DESC)...];
```

- ([ASC]|DESC)，表示这里的内容是 [ASC] 和 DESC二选一
  - 如果选择DESC，则DESC必写
  - 如果选择ASC，ASC可写可不写

- `DESC`，倒序排序，从上到下，值从大到小
- `ASC`，升序排序，从上到下，值从小到大，ASC是默认，可以不写



示例

```sql
# 统计价格大于1000的商品信息，按分数升序显示
select * from products where price > 1000 order by score;

# 统计价格大于1000的商品信息，按分数降序显示
select * from products where price > 1000 order by score DESC;

# 多列排序
# 统计价格大于1000的商品信息，按商品类别降序排序，再按分数升序排序
select * from products where price > 1000 order by category_id DESC, score ;
```



#### limit限制

> 作用：对已有结果集做条数限制

语法：

```sql
select ...
from ...
where ...
group by ...
order by ...
limit [m, ]n;
```

- n，必写，表示限制结果条数
- m，可选，表示起始索引



示例

```sql
# 找出价格最高的3个商品信息
select * from products order by price desc limit 3;

# 找出价格最高的第四第五第六 3个商品信息
select * from products order by price desc limit 3, 3;
# 第一个3，起始位置，从第三条（不含）开始取
# 第二个3，取3条
```



#### SQL顺序

书写上一定要保持：

```sql
1. select
2. from
3. where
4. group by
5. order by
6. limit
```

顺序不能乱，也就是group by 不能写在where之前，类似这样

- `wehre group by order by limit`都是按需取用，不是必写
- 但凡你需要写，顺序要保持上面的要求



### 多表查询 - 了解



#### 交叉连接

2个表产生笛卡尔积，即A表的每一条和B表的每一条都连接一下。

连接：列和列的拼接

如下交叉连接示例：

```sql
# from表a和b结果是
/*
 A 表
 a, 1
 b, 2
 c, 3

 B 表
 x
 y
 z

 from a, b后结果
 a, 1, x
 a, 1, y
 a, 1, z
 b, 2, x
 b, 2, y
 b, 2, z
 c, 3, x
 c, 3, y
 c, 3, z

 */
```



示例

```sql
# 需求：查询全部的商品信息+商品类别名称
select * from products, category where products.category_id = category.id;
# 有效条件是：products.category_id = category.id

# 简化写法
select * from products as p, category c where p.category_id = c.id;
```

查询中，表名可以写别名



上述查询是2步动作：

1. 先形成交叉连接（笛卡尔积）结果
2. 再where保留需要的



#### 内连接

内连接：在2个表合并的时候，判断，只保留合格的。（对比交叉连接，1步操作）

语法

```sql
from 表1 join 表2 on 条件;
```

示例：

```sql
# 交叉连接
select * from products as p, category c where p.category_id = c.id;

# 内连接
select * from products p join category c on p.category_id = c.id;
```



> 弊端：不符合连接条件的结果，不会显示，即某些数据行就不出现了。

#### 外连接

在外连接下，有一个表为主表，另一个是附表。

语法：

```sql
from 表a left|right join 表b on 条件;
```

- `left`表示表a为主
- `right`表示表b为主

效果：主表的全部数据行都会出现，如果找不到对应附表的信息，以`null`显示

示例

```sql
# 需求，查询全部全部全部全部全部全部全部商品的name、price、类别id、类别名称
select p.name, price, category_id, c.name
from products p left join category c on p.category_id = c.id;
```

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/28/20260428170046.png" alt="image-20260428170046505" style="zoom:67%;" />

如图，P表的id13商品，必须出现，找不到对应的`c.name`，则`c.name`以`null`显示



示例

```sql
select p.name, price, category_id, c.name
from products p right join category c on p.category_id = c.id;
```

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/28/20260428170134.png" alt="image-20260428170134411" style="zoom:67%;" />

类别表的全部数据，必须全部出现，最后家居必然出现，找不到对应的`p.name price category_id`，全部以`null`显示



### 自连接查询

#### 数据

找到课程资料中提供的`areas.sql`文件，拖动到datagrip，点击文件名右键运行

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/28/20260428171634.png" alt="image-20260428171633559" style="zoom:67%;" />

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/28/20260428171700.png" alt="image-20260428171700283" style="zoom:67%;" />

#### 示例

```sql
-- 自连接查询
-- 查询'河北省'下所有城市

select
    a1.title 省,
    a2.title 市 
from areas a1 join areas a2 on a1.id = a2.pid where a1.title='河北省';
```



a1和a2都是areas表

在表中 a1的id 如果和a2记录的pid相同

a1是父级，a2就是子级

上面sql，让父子关系连接起来



#### 示例2

```sql
# 查询三级关系对照
# 省市区
select
    a1.title 省,
    a2.title 市,
    a3.title 区县
from areas a1 join areas a2 on a1.id=a2.pid
join areas a3 on a2.id = a3.pid where a1.title='安徽省';
```



- a1的id为a2的pid，则a1是a2的父级
- a2的id为a3的pid，则a2是a3的父级
- 2个join 2个条件，都满足，则a1是省、a2是市、a3是区县



### 子查询

示例

```sql
# 查询河北省的城市
select id from areas where title='河北省';
select title from areas where pid=(select id from areas where title='河北省');
select title from areas where pid=(select id from areas where title='安徽省');
```

SQL的结果，也可以作为数据提供给查询判断用。





# Python操作MySQL

## 库安装

```bash
pip install pymysql
```



## 基础查询

```sql
# 查询商品名称、品牌、价格，要求是大于5000的价格
# 输出格式是： 每一个商品输出为： 商品名称：xxx，商品品牌：xxx，商品价格：xxx
import pymysql

# conn连接（TCP 三次握手）
conn = pymysql.connect(
    host="192.168.88.100",
    port=3306,
    user="root",
    password="123456",
    charset="utf8",
    database="jing_dong",
)

# 创建干活的小弟游标对象
cursor = conn.cursor()

# 查询
cursor.execute("select name, brand_name, price from goods where price > 5000")

# 抓取结果      all_result ==> ((name, brand_name, price), (), (), ...)
all_result = cursor.fetchall()

# 循环输出
for row in all_result:
    name = row[0]
    brand_name = row[1]
    price = row[2]

    print(f"商品名称：{name}，商品品牌：{brand_name}，商品价格：{price}")

# 关闭小弟
cursor.close()

# 关闭连接（断网，四次挥手）
conn.close()

```

- pymysql.connect，创建`connection`类对象，保持了TCP连接到MySQL服务器
- conn.cursor()，创建游标对象，干活是游标对象，即执行sql和获取结果

执行SQL：

- `cursor.execute(sql字符串)`

获取结果：

- cursor.fetchone()，获取一行，结构：`(列, 列, 列, ...)`
- cursor.fetchall()，获取全部结果，结构：`( (列, 列, 列, ...), (), (), ... )`



完事了需要：

- `cursor.close()`关闭干活的游标
- `conn.close()`关闭TCP连接



## 基础增删改

```sql
# 向user表插入10000条数据
import pymysql
import random

names = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 1. 连接（TCP）
conn = pymysql.connect(
    host="192.168.88.100",
    port=3306,
    user="root",
    password="123456",
    charset="utf8",
    database="jing_dong",
)

# 2. cursor
cursor = conn.cursor()

# 3. 执行sql
for data_id in range(4, 10004):
    user = random.choice(names) + random.choice(names) + random.choice(names)
    password = "123456"

    sql = f"INSERT INTO user VALUES({data_id}, '{user}', '{password}')"
    cursor.execute(sql)

# 4. 确认
conn.commit()

# 5. 关闭
cursor.close()
conn.close()

```

- 增删改操作，需要`conn.commit()`来做确认



## 关于commit

如果是select，不需要`conn.commit()`，但是需要`cursor.fetchall()`抓取结果

如果是insert update delete，需要`conn.commit()`，但是不需要`cursor.fetchall()`抓取结果



## 回滚 - 了解



对数据库的查询，没有`commit`确认一说，因为不涉及到数据库的修改（新增、删除、更新）。

对修改的commit涉及到事务的确认。



对数据库的修改，一般认为需要符合：

- 要么全部成功，要么全部失败。
- 不允许，成功一半失败一半





如果要达成这个效果：

- 如果没有异常，最后`commit()`确认即可
- 如果有异常，最后`rollback()`回滚即可



### 基础结构

```python
try:
    cursor.execute(...)
    
    
    conn.commit()		# 没问题确认
except Exception:	
    conn.rollback()		# 有问题撤回
```



示例

```python
import pymysql
import random

# 1. conn
conn = pymysql.connect(
    host="192.168.88.100",
    port=3306,
    user="root",
    password="123456",
    database="company_db",
    charset="utf8",
)

# 2. cursor
cursor = conn.cursor()

# 3. 执行sql
try:
    for i in range(1, 10001):
        name = f"王大锤{i}"
        gender = random.choice(["男", "女"])
        height = random.randint(160, 186)
        age = random.choice([22, 11, 33, 21, 25, 26, 28, 20])

        if i == 5001:
            sql = f"INSERT INTO student VALUES({i}, '{name}', '{gender}', {height}, {age}, 12345)"
        else:
            sql = f"INSERT INTO student VALUES({i}, '{name}', '{gender}', {height}, {age})"

        cursor.execute(sql)

        if i % 1000 == 0:
            print(f"插入了{i}条数据")

    conn.commit()       # 确认这些操作生效
except Exception:
    print(f"插入数据库中途出现问题，前面全部操作撤回")
    conn.rollback()     # 撤回

# 4. close
cursor.close()
conn.close()

```



## SQL变量的注入

为了避免安全问题，不建议使用字符串格式化的方式，生成SQL，而是使用pymysql内置的SQL格式化形式。

语法：

```sql
sql = "insert into table values(%s, %s, %s)"
cursor.execute(sql, [值1, 值2, 值3])
```

- 通过`%s`占位
- execute的时候，提供一个列表，列表里面就是要填充的值
- 和%s是一一对应即可



示例

```python
import pymysql

username = input("请输入账户")
password = input("请输入密码")

# 1. 创建连接，代码（客户端）到服务器MySQL的TCP连接，获得连接类的类对象
conn = pymysql.connect(
    host="192.168.88.100",
    port=3306,
    user="root",
    password="123456",
    database="jing_dong",
    charset="utf8",
)

# 2. cursor
cursor = conn.cursor()

# 3. 执行SQL
# 使用%站位，等同字符串格式化，%s
sql = "SELECT * FROM user WHERE user=%s and pwd=%s"
print(sql)
cursor.execute(sql, [username, password])
# ((), ())
all_result = cursor.fetchall()
if len(all_result) > 0:
    print("认证通过")
else:
    print("认证失败")

# 4. close
cursor.close()
conn.close()

```



反向示例（没有使用内置的%s占位注入，则密码输入 `' or 1=1 or ' `则100%登录成功）

```python
import pymysql

username = input("请输入账户")
password = input("请输入密码")

# 1. 创建连接，代码（客户端）到服务器MySQL的TCP连接，获得连接类的类对象
conn = pymysql.connect(
    host="192.168.88.100",
    port=3306,
    user="root",
    password="123456",
    database="jing_dong",
    charset="utf8",
)

# 2. cursor
cursor = conn.cursor()

# 3. 执行SQL
sql = f"SELECT * FROM user WHERE user='{username}' and pwd='{password}'"
print(sql)
cursor.execute(sql)
# ((), ())
all_result = cursor.fetchall()
if len(all_result) > 0:
    print("认证通过")
else:
    print("认证失败")

# 4. close
cursor.close()
conn.close()

```





# Redis数据库入门

## 介绍

Redis是一款主要基于内存记录数据的`非关系型数据库`产品。

- 数据存储结构，典型键值对结构，即存放的任何数据都是：Key -> Value

- > 可以认为，Redis就是把Python的字典，做成了数据库产品



特点：

1. 性能极其之高（如果MySQL是1，Redis大概是1000）
2. Redis能托管的数据量非常低的（MySQL可以上百TB数据，Redis一般就几个GB级别）
3. 原因：
   1. Redis数据主要依靠内存
   2. MySQL主要依靠硬盘



场景：

1. 高速数据缓存
2. 数据的临时中转站



在我们AI中：

1. MySQL或本地文件，一般用于全量记忆（对话历史记录）的存储
2. Redis，用于当前会话，记忆的缓存



## 环境部署（基于Docker）



### 下载和启动容器



1. 下载容器（Windows使用虚拟机的同学，可以跳过，仅Mac同学需要执行）

   ```bash
   # 使用虚拟机的同学
   sudo docker pull redis:6-alpine
   # Mac同学
   docker pull redis:6-alpine
   ```

2. 【可选，如果下载不下来可以导入】

   ```bash
   # 从课程资料中找到 redis-6-alpine.tar
   # 上传到虚拟机
   # 虚拟机同学
   sudo docker load -i redis-6-alpine.tar
   # Mac同学
   docker load -i redis-6-alpine.tar
   ```

3. 执行命令验证下载

   ```bash
   # 使用虚拟机同学
   sudo docker images			# 这个命令的含义是查看docker已经下载好的容器列表
   # Mac同学
   docker images
   ```

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/29/20260429104939.png" alt="image-20260429104939618" style="zoom:67%;" />

4. 首次启动容器

   ```bash
   # 虚拟机同学
   sudo docker run -d --name my-redis -p 6379:6379 redis:6-alpine
   # Mac同学
   docker run -d --name my-redis -p 6379:6379 redis:6-alpine
   ```

   - `-d`，后台执行
   - `--name`，给容器起个名字，自己随便起，我用my-redis
   - `-p`指定端口，redis默认运行在`6379`
   - `redis:6-alpine`，通过下载好的redis:6-alpine启动容器

5. 查看正在运行的容器

   ```bash
   # 虚拟机同学
   sudo docker ps
   # Mac同学
   docker ps
   ```



一旦启动后，以后使用就2个操作

```bash
# 停止
sudo docker stop my-redis
# 启动
sudo docker start my-redis
```



### 连接redis

我们的DataGrip可以连接Redis

1. 选择数据源

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/29/20260429105638.png" alt="image-20260429105638120" style="zoom:67%;" />

2. 设置IP地址和驱动

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/29/20260429105742.png" alt="image-20260429105742604" style="zoom:67%;" />

3. 选择1.0驱动

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/29/20260429105819.png" alt="image-20260429105818859" style="zoom:67%;" />

4. 选择后会下载

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/29/20260429105859.png" alt="image-20260429105859409" style="zoom:67%;" />

5. 等待下载完成

6. <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/29/20260429105937.png" alt="image-20260429105936920" style="zoom:67%;" />

7. 测试连接

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/29/20260429105958.png" alt="image-20260429105958446" style="zoom:67%;" />

8. 成功后，点击确定

   <img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/29/20260429110029.png" alt="image-20260429110029302" style="zoom:67%;" />



### 安装redis的Python库

通过pip安装redis即可

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/04/29/20260429110309.png" alt="image-20260429110309245" style="zoom:67%;" />



### Python代码验证redis连接

```python
import redis

# 创建 Redis 连接对象
r = redis.Redis(
    host='192.168.88.100',  # Redis 服务器地址
    port=6379,         		# Redis 服务器端口
    db=0,              		# 数据库编号，默认0
    password=None,     		# 密码，如果没有设置密码则为None
    decode_responses=True   # 自动解码，返回字符串而不是字节
)

# 测试连接
try:
    response = r.ping()
    print("Redis 连接成功:", response)
except redis.ConnectionError as e:
    print("Redis 连接失败:", e)
```



## 字符串操作

Redis的存储，都是Key-Value，Key永远为字符串，Value可以是：

- 字符串
- hash（字典）
- 列表
- 集合





示例

```python
import redis

r = redis.Redis(
    host="192.168.88.100",
    port=6379,
    db=0,
    password=None,
    decode_responses=True
)

# redis结构是K+V
# K字符串
# V是各类类型，我们现在的V演示为字符串
# set存入  set(k, v)
r.set('name', '周杰轮')
r.set('age', '19')

# 取出  get取出，  v = r.get(k)
name = r.get('name')
age = r.get('age')
age123 = r.get('age123')        # K不存在，结果为None
print(f"取出name：{name}，age：{age}, {age123}")

print("-----------------------------------------")
# mset multi set
# r.mset({k:v, k: v, K:v})
r.mset({"hobby": "唱跳RAP", "money": "123456", "gender": "男"})
# r.mget([k, k, k])   返回值 -> [v, v, v]
values = r.mget(['hobby', 'money', 'gender'])
print(f"一次型取出：{values}")
r.close()

```

示例（数值操作）

```python
import redis

r = redis.Redis(
    host="192.168.88.100",
    port=6379,
    db=0,
    password=None,
    decode_responses=True
)

r.set('num', '0')

# incr -> increment
r.incr('num')   # num的值+1
print('自增+1后', r.get('num'))

# incrby -> increment by
r.incrby('num', 5)
print('增长+5：', r.get('num'))

# decr -> decrement
r.decr('num')
print('自减-1后', r.get('num'))
# decrby -> decrement by
r.decrby('num', 3)
print('自减-3后', r.get('num'))

# 如果是复杂计算，就取出来，自己算，算完存回去
# num = int(r.get('num'))
# num = num * 10 + 2
# r.set('num', num)
# print('计算后：', r.get('num'))

r.close()

```



## hash哈希操作

所谓的hash，指的是一个键值对（k-v）

redis存的都是k-v，redis的k就是字符串，v就是hash

redis存hash，本质是存了： k（字符串） -> v（hash，k -> v)



常用方法：

- `r.hset(k1, k2, v, mapping)`
  - 一次设置一个键值对
  - `r.hset(k, k2, v)`
  - 一次设置多个键值对
  - `r.hset(k, mapping={k:v, k:v, ...})`
- `r.hget(k1, k2)`，可以获取指定的v
- `r.hgetall(k)`，可以获取指定key内部的全部信息（字典）



示例

```python
import redis

r = redis.Redis(
    host="192.168.88.100",
    port=6379,
    db=0,
    password=None,
    decode_responses=True
)

# hset(k1, k2, v)
# redis记录的k-v
# k就是k1   v(k2->v)

r.hset('user小曹', 'age', '21')
r.hset('user小曹', 'hobby', '写代码')
r.hset('user小曹', 'height', '185.55')

# 取出
# r.hget(k1, k2)
hobby = r.hget('user小曹', 'hobby')
print(hobby)

# 取出全部的字段
userinfo: dict = r.hgetall('user小曹')
print(userinfo)

print("--------------------")
# 过期方法，能用
r.hmset(
    'user小锤', {
        'name': '王小锤',
        'age': 11,
        'gender': '男'
    }
)
# 新方法，能用
r.hset('user大锤', mapping={'name': '曹大锤', 'age': 12, 'gender': '男'})

r.close()

```



## 列表操作

在redis中存列表，本质是存K->V，  k：字符串， V->列表

示例代码

```python
# list操作，  redis  ：k -> v   ，  k字符串， v是list
import redis

r = redis.Redis(
    host="192.168.88.100",
    port=6379,
    db=0,
    password=None,
    decode_responses=True
)

# 存入列表
# 从列表左侧插入
r.lpush("lst1", 't1', 't2', 't3')
# 从列表右侧插入
r.rpush('lst1', 't4', 't5', 't6')

# 长度
length = r.llen('lst1')
print(f"列表长度：", length)

# 获取下标范围的元素
all_element = r.lrange('lst1', 0, -1)
print(f"全部列表内容：", all_element)
# 获取前3      # 包头包尾
all_element = r.lrange('lst1', 0, 2)
print(f"全部列表内容：", all_element)

# 取出第一个元素，弹出数量不管是1还是多，都是结果为[x,...]
first_e = r.lpop('lst1', 1)
print("左弹出：", first_e)
right_e = r.rpop('lst1', 2)
print("右弹出：", right_e)

r.close()

```



## 集合操作

在redis中存集合，本质是存K->V，K：字符串，V->集合

示例

```python
import redis

r = redis.Redis(
    host="192.168.88.100",
    port=6379,
    db=0,
    password=None,
    decode_responses=True
)

# 存入集合（去重）
r.sadd("set1", 'python', 'itheima', 'itcast', 'python')
# 获取全部
all_tags: set = r.smembers('set1')
print(all_tags)

# 判断元素是否有
is_member = r.sismember('set1', 'python')
print('是否有python结果：', is_member)        # 结果1 True 0为False

# 弹出元素（集合没下标）
tag = r.spop('set1')
print('弹出：', tag)

# 指定弹出（删除）元素
r.srem('set1', 'itheima')
print("删除后：", r.smembers('set1'))

r.sadd('seta', 'a', 'b', 'c')
r.sadd('setb', 'd', 'b', 'c')

# 交集
intersection = r.sinter('seta', 'setb')
print("交集", intersection)

# 并集
union = r.sunion('seta', 'setb')
print("并集", union)

# 差集
difference = r.sdiff('setb', 'seta')
print(f"差集：", difference)
r.close()
```



## 有序集合 - 了解

在redis中存储有序集合，本质存放的是：K->V，K：字符串，V：字典（k：被存的信息，v：信息的分数）

分数用于给被存的信息，做排名、排序的依据

示例

```python
import redis

r = redis.Redis(
    host="192.168.88.100",
    port=6379,
    db=0,
    password=None,
    decode_responses=True
)

# zadd添加有序集合   -> mapping -> dict
r.zadd("leaderboard", {
    "小曹": 2000,         # k->v   信息->分数
    "小花": 5000,
    "小旺": 6000,
    "小翠": 1000,
})
asc_names = r.zrange('leaderboard', 0, -1)
print(asc_names)

# 升序
asc_names = r.zrange('leaderboard', 0, -1, withscores=True)
print(asc_names)
# 降序
desc_names = r.zrevrange('leaderboard', 0, -1, withscores=True)
print(desc_names)

# 获取分数
print("小曹分数:", r.zscore("leaderboard", '小曹'))

# 增加分数
r.zincrby("leaderboard", 1000, '小曹')
print("小曹分数:", r.zscore("leaderboard", '小曹'))

# 得到排名从高到低  从0开始排名
print("小曹排名:", r.zrevrank('leaderboard', '小旺'))

# 按分数范围获取
scores = r.zrangebyscore('leaderboard', 1000, 5000, withscores=True)
print(scores)
r.close()

```



## 总结

| 类型   | 在redis中的存储结构    |
| ------ | ---------------------- |
| 字符串 | K->V；K字符串，V字符串 |
| hash   | K->V；K字符串，V字典   |
| 列表   | K->V；K字符串，V列表   |
| 集合   | K->V；K字符串，V集合   |





## 设置Key的TTL

TTL：Time To Live剩余生存时间

Key默认永久存在，如果不需要永久可以设置TTL



示例

```python

import redis

r = redis.Redis(
    host="192.168.88.100",
    port=6379,
    db=0,
    password=None,
    decode_responses=True
)

# 检查K是否存在
print("hobby存在？：", r.exists("hobby"))
print("hobby222存在？：", r.exists("hobby222"))

# TTL（Time To Live 剩余生存时间）设置
# hobby 5秒后删除
r.expire("hobby", 5)

# r.expire("num", 300)
# 查看TTL
num_ttl = r.ttl("num")
print("key num ttl: ", num_ttl)

# 取消TTL   persist(持久化)
r.persist("num")
# TTL为-1表示永久
print("key num ttl: ", r.ttl("num"))

# 查看redis全部key
keys = r.keys("*")
print(keys)

# 查看全部user开头的key
user_keys = r.keys("user*")     # 等同于linux * 通配符写法
print(user_keys)

# 彻底删除key
r.delete("user大锤")
r.close()

```



## 操作总结

### 一、通用操作（所有类型都能用）

| API 方法                 | 作用                    | 示例                              |
| :----------------------- | :---------------------- | :-------------------------------- |
| `r.exists(key)`          | 判断 key 是否存在       | `r.exists("name")`                |
| `r.expire(key, seconds)` | 设置 key 过期时间（秒） | `r.expire("hobby",5)`             |
| `r.ttl(key)`             | 查看 key 剩余过期时间   | `r.ttl("num")`                    |
| `r.persist(key)`         | 取消过期时间，永久保存  | `r.persist("num")`                |
| `r.keys(pattern)`        | 查找符合规则的 key      | `r.keys("*")` / `r.keys("user*")` |
| `r.delete(key)`          | 删除指定 key            | `r.delete("user大锤")`            |
| `r.close()`              | 关闭 Redis 连接         | `r.close()`                       |

### 二、字符串（String）操作

| API 方法                    | 作用                                  |
| :-------------------------- | :------------------------------------ |
| `r.set(key, value)`         | 存储单个字符串键值对                  |
| `r.get(key)`                | 获取单个字符串值，key 不存在返回 None |
| `r.mset({k:v, ...})`        | 批量存储多个字符串                    |
| `r.mget([key1, key2, ...])` | 批量获取多个字符串值，返回列表        |

### 三、哈希（Hash）操作（类似字典）

| API 方法                      | 作用                           |
| :---------------------------- | :----------------------------- |
| `r.hset(name, key, value)`    | 哈希中设置单个字段             |
| `r.hset(name, mapping={...})` | 哈希中批量设置字段（推荐）     |
| `r.hmset(name, { ... })`      | 哈希批量设置字段（旧方法）     |
| `r.hget(name, key)`           | 获取哈希中单个字段             |
| `r.hgetall(name)`             | 获取哈希所有字段和值，返回字典 |

### 四、列表（List）操作

| API 方法                    | 作用                                |
| :-------------------------- | :---------------------------------- |
| `r.lpush(key, *values)`     | 从列表**左侧**插入元素              |
| `r.rpush(key, *values)`     | 从列表**右侧**插入元素              |
| `r.llen(key)`               | 获取列表长度                        |
| `r.lrange(key, start, end)` | 获取列表指定范围元素（0=-1 取全部） |
| `r.lpop(key, count=1)`      | 从列表**左侧**弹出元素              |
| `r.rpop(key, count=1)`      | 从列表**右侧**弹出元素              |

### 五、集合（Set）操作（无序、去重）

| API 方法                   | 作用                                    |
| :------------------------- | :-------------------------------------- |
| `r.sadd(key, *members)`    | 向集合添加元素（自动去重）              |
| `r.smembers(key)`          | 获取集合所有元素                        |
| `r.sismember(key, member)` | 判断元素是否在集合中（返回 True/False） |
| `r.spop(key)`              | 随机弹出一个元素                        |
| `r.srem(key, member)`      | 删除集合中指定元素                      |
| `r.sinter(key1, key2)`     | 求多个集合的**交集**                    |
| `r.sunion(key1, key2)`     | 求多个集合的**并集**                    |
| `r.sdiff(key1, key2)`      | 求集合的**差集**（key1 - key2）         |

### 六、有序集合（ZSet / Sorted Set）操作

| API 方法                                          | 作用                              |
| :------------------------------------------------ | :-------------------------------- |
| `r.zadd(key, {member: score, ...})`               | 添加有序集合元素（成员 + 分数）   |
| `r.zrange(key, 0, -1, withscores=True)`           | 按分数**升序**获取元素            |
| `r.zrevrange(key, 0, -1, withscores=True)`        | 按分数**降序**获取元素            |
| `r.zscore(key, member)`                           | 获取指定成员的分数                |
| `r.zincrby(key, increment, member)`               | 给指定成员增加分数                |
| `r.zrevrank(key, member)`                         | 获取成员**降序排名**（从 0 开始） |
| `r.zrangebyscore(key, min, max, withscores=True)` | 按分数范围查询元素                |



## Redis缓存案例

```python
import redis
import pymysql


class MySQLService:

    def __init__(self,
                 host="192.168.88.100",
                 port=3306,
                 user="root",
                 pswd="123456",
                 db="my_db",
                 charset="utf8"):
        # 连接对象
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=pswd,
            db=db,
            charset=charset
        )
        # 创建游标对象，用于执行sql
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_user_info(self, username):
        sql = "SELECT * FROM userinfo WHERE name=%s"
        self.cursor.execute(sql, [username])

        # 获取结果
        return self.cursor.fetchall()


class RedisService:

    def __init__(self, ms: MySQLService, host="192.168.88.100", port=6379, pswd=None, db=0):
        self.redis_conn = redis.Redis(
            host=host,
            port=port,
            password=pswd,
            db=db,
            decode_responses=True,
        )

        self.ms: MySQLService = ms

    def __del__(self):
        self.redis_conn.close()

    def __ttl_reset(self, key, ttl_time=15):
        # 设置TTL
        self.redis_conn.expire(key, ttl_time)

    def __save_user_info(self, username, infos):
        # 周杰轮: -> ((), ())
        # redis: key:周杰轮， value：list[(id, name, age), (), ()]
        for info in infos:
            msg = ",".join([str(col) for col in info])
            self.redis_conn.rpush(username, msg)
        # 首次设置过期时间
        self.__ttl_reset(username)

    def get_user_info(self, username):
        # redis有没有？
        if self.redis_conn.exists(username):        # 1 True
            # 找到缓存
            print(f"查询{username}，缓存命中，重设TTL")
            # 重设TTL
            self.__ttl_reset(username)

            #
            return self.redis_conn.lrange(username, 0, -1)

        print(f"查询{username}，缓存未命中，跳转MySQL查询")

        infos = self.ms.get_user_info(username)     # ((), ())

        if infos:       # 空元组是False，非空是True
            print(f"查询{username}，缓存未命中，从MySQL中查询得到信息，同检索到{len(infos)}条信息")
            self.__save_user_info(username, infos)
        else:
            print(f"查询{username}，缓存未命中，MySQL也没查到，没有此用户")

        return infos


if __name__ == '__main__':
    ms = MySQLService()
    rs = RedisService(ms)

    while True:
        username = input("输入要查询的姓名，要退出输入exit")
        if username == "exit":
            break

        infos = rs.get_user_info(username)
        print(infos)

```



# 数据分析三剑客

## 概述

- `numpy`，科学计算库，主要做数学计算
- `pandas`，数据分析库，主要做数据的清洗过滤、统计分组、查询计算等
- `matplotlib`，可视化框架，主要针对数据产出可视化图表（衍生于：`matlab`）



三者的关系：

- `numpy`提供底层的数学计算支持。加减乘除平方方差标准差点积等等计算
- `pandas`，提供数据的处理、整理、分析、统计
- `matplotlib`，完成结果的可视化展示



## numpy

三剑客不是Python自带的，需要安装

### 安装

```bash
pip install numpy pandas matplotlib -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```



### 核心对象ndarray的创建

numpy的核心对象是`<class numpy.ndarray>`，我们使用numpy第一步是将数据转换为`ndarray`类对象



示例

```python
import numpy as np

# numpy的核心对象是ndarray对象，需要将数据对象如list、元组等转换为ndarray
# -> 从列表创建 -> ndarray
arr1: np.ndarray = np.array([1, 3, 5, 7, 9])
print("一维数组arr1：", arr1, type(arr1))

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("二维数组arr2：\n", arr2)

# 创建特殊数组
# 全是0的数组
zeros_arr = np.zeros((3, 4))        # 传入元组，3和4,3行4列，二维
print("全0数组：\n", zeros_arr)
# 全是1的数组
ones_arr = np.ones((5, 6))
print("全1数组：\n", ones_arr)

# 创建序列数组，包头，不包尾巴，类似python range
range_arr: np.ndarray = np.arange(0, 10, 2)
print("序列数组：\n", range_arr, type(range_arr))

# 等分数组
linspace_arr = np.linspace(0, 12, 6)
print("等分数组：\n", linspace_arr)

# 随机数组
random_arr = np.random.rand(3, 3)
print("随机数组：\n", random_arr)

# 标准正态分布数组
randn_arr = np.random.randn(3, 3)
print("正态数组：\n", randn_arr)

```

- 用的最多的，就是np.array(列表)，基于列表创建



### 查看ndarray对象的属性

```python
import numpy as np
# [   [], [],   ]  二维数组

# a = [
#         [
#             [],
#             [],
#         ],
#         [
#             [],
#             [],
#         ],
# ]   三维数组
# 创建示例的数组
arr: np.ndarray = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 属性，ndarray是一个class的类对象，类里面有方法也有变量（属性）
print("数组：", arr)
print("数组维度：", arr.ndim)        # 访问ndim成员属性
print("数组形状：", arr.shape)       # 形状（行数、列数）
print("数组大小：", arr.size)        # 元素总数
print("数据类型：", arr.dtype)       # 存的数据类型
# 数组int默认存储为int64（8字节 8bytes）
# python的int默认存储为int32（4字节 4bytes）

```





### ndarray的索引和切片



索引

```python
arr[下标]
arr[x, y]		# x为行下标, y列下标

# 创建示例数组
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("原始数组:\n", arr)

# 索引
print("第一个元素：", arr[0, 0])
print("最后一行：", arr[-1])
print("第二列：", arr[:, 1])        # 不关心行只关心列，行用:代替  [:, 列] 取指定列   [:数字]切片
```



切片

```python
arr[a: b]				# a起始 b结束（不含），和列表一样
arr[a1: b1, a2: b2]		# a1:b1 控制行   a2:b2控制列

# 切片
print("前两行", arr[0: 2])
print("前两行前两列", arr[:2, :2])
print("每隔一个元素要一个(行和列都隔)", arr[::2, ::2])
```



布尔索引

```python
# 布尔索引
bool_arr = arr > 5
print("布尔结果：\n", bool_arr)
# 结果
 [[False False False False]
 [False  True  True  True]
 [ True  True  True  True]]
```



```bash
1. 创建1个二维 内容不限，结构3x4
2. 取出 第二行第三列
3. 取出第二第三行，第二第三列
4. 创建1个1维数组内容不限，元素数量15个
5. 将其重塑为 3x5的二维
6. 转换为5x3的二维
7. 将5x3的二维摊平得到1维
```



### 数学计算

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print("数组a:", a)
print("数组b:", b)

# 算术运算
print("加法：\n", a + b)
print("减法：\n", a - b)
print("乘法：\n", a * b)
print("除法：\n", a / b)
print("幂运算：\n", a ** 2)

# 比较
print("大于比较：\n", a > b)     #  [False False False False]
print("小于比较：\n", a < b)     #  [ True  True  True  True]

# 矩阵乘法(点积)      点积和模长是计算余弦相似度的基础算术计算
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
res = np.dot(arr1, arr2)
print(res)


# 广播机制
import numpy as np

# 广播示例
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])       # 3x3

b = np.array([10, 20, 30])      # 1x1

print("数组a:\n", a)
print("数组b:", b)
print("广播加法:\n", a + b)  # b被广播到a的每一行

c = np.array([[1], [2], [3]])   # 3x1       每一行，广播给对方的每一行， 1给了a里面的[1, 2, 3]  2给了a里面的[4, 5, 6]
print("广播乘法：\n", a * c)

```



### 统计计算

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("数组:\n", arr)
print("总和:\n", np.sum(arr))
print("每列总和:\n", np.sum(arr, axis=0))       # 0表示列方向
print("每行总和:\n", np.sum(arr, axis=1))       # 1表示行方向

print("平均值:\n", np.mean(arr))                # mean平均
print("标准差:\n", np.std(arr))
print("方差:\n", np.var(arr))

print("最大:\n", np.max(arr))
print("最大值的索引:\n", np.argmax(arr))
print("最小:\n", np.min(arr))
print("最小值的索引:\n", np.argmin(arr))

```



## pandas

### 安装

```bash
pip install numpy pandas matplotlib -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```



### 结构

pandas的数据结构：

- 一维结构：`Series`
- 二维结构：`DataFrame`

关系如下：

<img src="https://image-set.oss-cn-zhangjiakou.aliyuncs.com/img-out/2026/05/05/20260505104700.png" alt="image-20260505104700715" style="zoom:67%;" />

DataFrame就是二维表格，每一列就是一个Series

### Series的创建

```python
# pandas的数据也有维度，分为1维和2维
# 一维可以看做是一个只有一个列的数据库表
# 二维可以可看做是由多个类的数据库表
import pandas as pd

# 一维Series  <class 'pandas.Series'>
# 从列表创建
s1 = pd.Series(["a", "b", "c"])     # numpy纯玩数字，pandas玩的是数据（数字、字符串都支持）
print(s1)
print(type(s1))
print("-"*20)

# 从字典创建
# 字典key作为数据的索引，字典的value就是数据
s2 = pd.Series({"a": 1, "b": 2, "c": 3})
print(s2)
print("-"*20)

# 指定索引
s3 = pd.Series([100, 200, 300], index=['x', 'y', 'z'])
print(s3)
print("-"*20)

# 取值
print("s3全部值：", s3.values, type(s3.values))
print("s3全部索引：", s3.index)

```

### DataFrame的创建

```python
import pandas as pd

# 基于字典
data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 30, 35, 28],
    '城市': ['北京', '上海', '广州', '深圳'],
    '工资': [5000, 7000, 6000, 8000]
}       # key就是列名，value是列表，当前列的每一行数据
df1 = pd.DataFrame(data)
print(df1)
print(type(df1))
print("="*20)

# 基于列表
data_list = [
    ['张三', 25, '北京', 5000],
    ['李四', 30, '上海', 7000],
    ['王五', 35, '广州', 6000],
    ['赵六', 28, '深圳', 8000]
]
df2 = pd.DataFrame(data_list)       # 没有列名，列默认0 -> 1 -> 2 -> ...
print(df2)
print("="*20)

# 查看DataFrame的基本信息
print("形状：", df1.shape)
print("列名：", df1.columns)           # 列索引
print("索引：", df1.index)             # 行索引
print("数据类型：", df1.dtypes)         # 每个列的类型

```



### 数据查看和数据选择

- df.head(n) 查看前n行
- df.tail(n) 查看尾n行
- df.loc[行索引] 取某一行用行索引
- df.loc[[行索引, 行索引, ..]]   # 取指定的多个行
- df.loc[行索引:行索引]   切片，从start行索引到stop行索引结束（包含尾巴）
- df.iloc[0|1|2|...] 用行自带的012索引取行
  - df.iloc[0] 取第一行
- df.iloc[[0, 2]]    # 取指定的0和2行即：第一行和第三行
- df.iloc[x:y]       # x和y是0123的数字行索引， 从x开始到y结束（不含尾巴）
- df[列索引]   # 取某个列
- df[[列索引, 列索引, ...]]   # 取指定的多个列

```python
import pandas as pd

# 创建示例DataFrame
data_list = [
    ['张三', 25, '北京', 5000],
    ['李四', 30, '上海', 7000],
    ['王五', 35, '广州', 6000],
    ['赵六', 28, '深圳', 8000]
]

# 手动指定行列索引的名字（默认都是0、1、2、...）   column列 row行
df = pd.DataFrame(
    data_list,
    columns=["姓名", "年龄", "地址", "薪资"],       # 手动提供列索引
    index=["row1", "row2", "row3", "row4"]       # 手动提供行索引
)
print(df)
print("="*20)

# 选择行
# 查看前2行
print("前两行：\n", df.head(2))
print("="*20)
# 查看尾2行
print("尾两行：\n", df.tail(2))
print("="*20)
# 查看df整体的描述信息
print("df信息：\n", df.describe())     # 类似sql： desc 表;
print("="*20)

# 选择列
# select 列, 列
# 单独看姓名列： select 姓名 from 表;
# df[列索引]   df[3]  df['姓名']
print("姓名列：\n", df['姓名'])
print("列类型：\n", type(df['姓名']))     # Series
print("="*20)
# 看姓名和年龄列
# select 姓名, 年龄 from 表;
# 语法： df[[列索引, 列索引, ...]]
print("姓名，年龄列：\n", df[['姓名', '年龄']])
print("="*20)

# 通过行索引选择
# df.loc[行索引]
# df.loc[[行索引, 行索引, ...]]
print("第一行：\n", df.loc["row1"])
print("="*20)
print("第一行和第三行：\n", df.loc[["row1", "row3"]])

# 切片
print("切片：\n", df["row1": "row3"])      # 切片尾巴是包含

# 行索引默认0123...是一直存在，如果你手动设置了行索引，那么0123也存在，还是可以用
# df.iloc  可以用0123
# df.loc 用行索引名
print("第一行：\n", df.iloc[0])
print("第一第三行：\n", df.iloc[[0, 2]])
print("前三行：\n", df.iloc[0: 2])          # 不包含尾巴

```



### 数据过滤

```python
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [25, 30, 35, 28, 32],
    '部门': ['技术部', '销售部', '技术部', '人事部', '销售部'],
    '工资': [5000, 7000, 6000, 5500, 7500]
})

print("原始数据：\n", df)
print("="*20)

# 条件筛选 df[筛选条件]    筛选条件 => df['列'] > 30  指定列大于30
# 示例  df[ df['列'] > 30  ]
# 年龄大于30
print("年龄大于30：\n", df[df['年龄'] > 30])

# 技术部
print("技术部内容：\n", df[df['部门'] == '技术部'])

# 类sql查询过滤   where 年龄 > 28 and 工资 < 700
print("年龄大于28且工资小于7000：\n", df.query('年龄 > 28 and 工资 < 7000'))

# 排序
print("按工资降序排序：\n", df.sort_values('工资', ascending=False))      # ascending默认True（升序）

# 多列排序
print("多列排序：\n", df.sort_values(['部门', '工资'], ascending=False))
print("多列排序：\n", df.sort_values(['部门', '工资'], ascending=[True, False]))

```

- `df.query(类sql where字符串条件)`  where过滤
- `df.sort_values`  排序



### 数据清洗

清洗：将垃圾数据做处理（删除、填充）

```python
import pandas as pd

# 读取csv
# df = pd.read_csv("../data/test.csv", sep="|")
df = pd.read_csv(
    "../data/清洗数据.csv",
    sep=","         # 分隔符是啥，不填默认认为是,
)
print(df)

print("\n缺失值统计")
print(df.isnull().sum())

print("\n非缺失值统计")
print(df.notnull().sum())

print("\n删除含有缺失值的行")
print(df.dropna())            # na 表示缺失

print("\n删除全部都是缺失值的行")
print(df.dropna(how='all'))

# 不想删除，可以填充
print("\n填充缺失值")
print(df.fillna(0))

print("\n均值填充缺失值")
print(df.fillna(df.mean()))     # mean 平均

print("\n均值填充最大值")
print(df.fillna(df.max()))

print("\n均值填充最小值")
print(df.fillna(df.min()))

```

### 数据统计

```python
import pandas as pd

df = pd.read_csv("../data/分组聚合数据.csv", sep=",")

print(df)
# 分组统计  group by + 聚合
# group by 产品 sum(销售额)
print("\n按产品分组统计销售额的和")
# df.groupby(列)[列].sum|min|max|mean|count()
print(df.groupby('产品')['销售额'].sum())
print("\n按产品分组统计销售额的最小")
print(df.groupby('产品')['销售额'].min())


# 多列分组，多聚合
# select sum(销售额), avg(销售额) from df group by 产品, 地区;
print("\n按产品和地区分组统计销售额的和以及平均")
# df.groupby([列,列])[列].agg(['sum', 'mean', 'max', ...])
print(df.groupby(['产品', '地区'])['销售额'].agg(['sum', 'mean']))


print("\n数据透视表")
# 产品分组  sum销售额
pivot_df = df.pivot_table(index='产品', values='销售额', aggfunc='sum')
print(pivot_df)

```



## matplotlib

### 折线图

```python
import numpy as np
import matplotlib.pyplot as plt         # plot 画板画画
import matplotlib

# 注意:新版本需要指定 matplotlib 使用 TkAgg 作为图形后端来渲染和显示图表
matplotlib.use('TkAgg')
# 注意:中文显示需要额外设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 准备数据
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 5, 11, 3, 6])

# 画图
# 创建画板（空白）
plt.figure(figsize=(8, 5))      # 8比5比例画板
# 画线
plt.plot(x, y, color='blue')        # 参数1和2 x和y轴数据          plot折线图
# 添加标题
plt.title("测试折线图")
# 给x轴取名字
plt.xlabel("这是x轴")
# y轴取名字
plt.ylabel("这是y轴")
# 显示网格
plt.grid()

# 显示
plt.show()

```



### 散点图

```python
import numpy as np
import matplotlib.pyplot as plt         # plot 画板画画
import matplotlib

# 注意:新版本需要指定 matplotlib 使用 TkAgg 作为图形后端来渲染和显示图表
matplotlib.use('TkAgg')
# 注意:中文显示需要额外设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置种子
np.random.seed(55)
x = np.random.randn(50)     # 生成随机50个数字
y = x * 2 + np.random.randn(50) * 0.6       # 在x的技术上y有一点偏移

# 画图
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='red')           # scatter 散点图

plt.title("测试散点图")
plt.xlabel("x轴")
plt.ylabel("y轴")
plt.grid()

plt.show()

```



### 案例

```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
# 注意:中文显示需要额外设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv(
    '1960-2019全球GDP数据.csv',
    sep=',',
    encoding='gbk'
)

# 干掉空值
# inplace=True 表示原地更改，即修改自己，不会返回新的DataFrame
df.dropna(inplace=True)

# 过滤
# .copy()就是复制一份数据返回，避免对老的DataFrame产生影响
df_cn = df[df['country'] == '中国'].copy()
df_jp = df[df['country'] == '日本'].copy()
df_us = df[df['country'] == '美国'].copy()

# 将年份设置为索引值，x轴数据一般被拿来做索引
df_cn.set_index('year', inplace=True)
df_jp.set_index('year', inplace=True)
df_us.set_index('year', inplace=True)

# 为了避免图例的冲突，将每份数据的GDP列名改为各自国家
df_cn.rename(columns={"GDP": "中国"}, inplace=True)
df_jp.rename(columns={"GDP": "日本"}, inplace=True)
df_us.rename(columns={"GDP": "美国"}, inplace=True)

plt.figure(figsize=(10, 6))
plt.plot(df_cn.index, df_cn["中国"], color="red", label="中国")     # label给这个线起名
plt.plot(df_jp.index, df_jp["日本"], color="green", label="日本")
plt.plot(df_us.index, df_us["美国"], color="blue", label="美国")
plt.title("中美日GDP")
plt.legend()            # 显示图例
plt.grid()

plt.show()

```

