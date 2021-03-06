# 解释作业、进程、线程的概念，进程和线程概念的提出分别解决了什么问题？

作业：计算机操作者交给操作系统的执行单位

进程：计算机中的程序关于某数据集合上的一次运行活动，是系统进行资源分配和调度的基本单位

线程：是程序执行流的最小单元，由线程ID，当前指令指针(PC)，寄存器集合和堆栈组成，是被系统独立调度和分派的基本单位

进城概念的提出解决的问题：如何深刻描述程序动态执行过程的性质

线程概念提出解决的问题：解决了进程在创建、撤消与切换存在较大的时空开销，多个进程并行开销过大的问题。解决了进程之间的资源竞争。

# 调研虚拟存储器的概念，描述其工作原理和作用

虚拟存储器是计算机系统内存管理的一种技术。它使得应用程序认为它拥有连续的可用的内存(一个连续完整的地址空间)，而实际上，它通常是被分隔成多个物理内存碎片，
还有部分暂时存储在外部磁盘存储器上，在需要时进行数据交换。

工作原理：虚拟存储器是由硬件和操作系统自动实现存储信息调度和管理的。它的工作过程包括6个步骤:

①中央处理器访问主存的逻辑地址分解成组号a和组内地址b，并对组号a进行地址变换，即将逻辑组号a作为索引，查地址变换表，以确定该组信息是否存放在主存内。

②如该组号已在主存内，则转而执行④;如果该组号不在主存内，则检查主存中是否有空闲区，如果没有，便将某个暂时不用的组调出送往辅存，以便将这组信息调入主存。

③从辅存读出所要的组，并送到主存空闲区，然后将那个空闲的物理组号a和逻辑组号a登录在地址变换表中。

④从地址变换表读出与逻辑组号a对应的物理组号a。

⑤从物理组号a和组内字节地址b得到物理地址。

⑥根据物理地址从主存中存取必要的信息。

调度方式有分页式、段式、段页式3种。页式调度是将逻辑和物理地址空间都分成固定大小的页。
主存按页顺序编号，而每个独立编址的程序空间有自己的页号顺序，通过调度辅存中程序的各页可以离散装入主存中不同的页面位置，并可据表一一对应检索。
页式调度的优点是页内零头小，页表对程序员来说是透明的，地址变换快，调入操作简单;缺点是各页不是程序的独立模块，不便于实现程序和数据的保护。
段式调度是按程序的逻辑结构划分地址空间，段的长度是随意的，并且允许伸长，它的优点是消除了内存零头，易于实现存储保护，便于程序动态装配;缺点是调入操作复杂。
将这两种方法结合起来便构成段页式调度。在段页式调度中把物理空间分成页，程序按模块分段，每个段再分成与物理空间页同样小的页面。
段页式调度综合了段式和页式的优点。其缺点是增加了硬件成本，软件也较复杂。大型通用计算机系统多数采用段页式调度。

作用：扩大内存

随机存储器发生运行缓慢的现象，操作系统会把随机存储器调动到一个叫做“分页文件”的临时空间当中，
当RAM进入到分页文件里面将会被立即释放，能够有效地帮助操作系统更快地完成程序操作

电脑运行程序所需要的RAM，即随机存储器，空间不足的话，
电脑的操作系统也会自动调用虚拟存储器对随机存储器进行补偿，将它们组合成临时的空间组合
