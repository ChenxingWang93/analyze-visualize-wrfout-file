# analyze-visualize-wrfout-file

## Introduction🗣️简介
### 📌definition and the scope of this research **该研究所瞄准的领域 以及 定义**
`wrfout` 文件是由 **天气研究与预测(WRF) Weather Research and Forecasting** 模型生成的 输出文件

是一种 **数值分析** 的天气预测系统

目的是做 **大气研究** 与 **业务预测**

这些文件包含的数据包括 **各种大气参数**，如，**温度**、**压力**、**风速**、与**风向**、**湿度** 等，基于时序跨越三维网格

`wrfout`文件通常以 名为 **网络通用数据表NetCDF (Network Common Data Form)** 的形式存在

也是一系列 **软件库** 与 **自描述的**，**机器独立的** 数据形式

用于 **创建**，**访问** 与**共享** **面向数组的科学数据array-oriented scientific data**

NetCDF 文件用于 存储 多维科学数据与相关元数据

### 📌brief description of your result and impact 简要描述 结果以及 影响

<img width="1500" alt="Screen Shot 2023-05-14 at 20 36 38" src="https://github.com/ChenxingWang93/analyze-visualize-wrfout-file/assets/31954987/cf5a5533-8816-4c51-b8f6-b76300bd12f0">[收起形式]

<img width="1500" alt="Screen Shot 2023-05-14 at 21 17 47" src="https://github.com/ChenxingWang93/analyze-visualize-wrfout-file/assets/31954987/c387e68f-4b51-4dc9-bc6f-07075cecdc41">[展开形式]

<img width="100" alt="Screen Shot 2023-05-14 at 21 58 33" src="https://github.com/ChenxingWang93/analyze-visualize-wrfout-file/assets/31954987/edfa63ff-90f6-43dc-b51c-efd9445599c4">

**数据类型Data Type** 中主要有两种 `Geo2D` &`1D` 

### 📌以其中一个`Geo2D`为例
e.g. Variable "ACGRDFLX"
```
float ACGRDFLX(Time=1, south_north=250, west_east=310);
  :FieldType = 104; // int
  :MemoryOrder = "XY ";
  :description = "ACCUMULATED GROUND HEAT FLUX";
  :units = "J m-2";
  :stagger = "";
  :coordinates = "XLONG XLAT XTIME";
```
上述 code snippets 定义了一个名为 `ACGRDFLX` 的浮点类型变量

- ①
```
/*第1行*/
float ACGRDFLX(Time=1, south_north=250, west_east=310);
```
包含 `Time`、`south_north`、& `west_east` 的三维数据，数值分别为1，250，&310

- ②
```
/*第2行*/
  :FieldType = 104; // int
```
变量`ACGRDFLX` 的属性，声明了该变量的域类型field type 为 `104`

类似代码对应的 特定数据类型

（但是❗这些代码片段是 跨数据集 **非标准化** 的，会在 别处文件和文件夹 以不同的方式被定义）

- ③
```
/*第3行*/
  :MemoryOrder = "XY ";
```
此行代码代表数据是以 `X`(west_east), `Y`(south_north). 顺序存储在内存中

`XY `后的` ` 意味着 没有特定的 内存顺序 给到 **时间** 这个维度

- ④
```
/*第4行*/
  :description = "ACCUMULATED GROUND HEAT FLUX";
```
这行提供的是 一个人类可读的 对变量`ACGRDFLX`代表什么的描述 是 **累积地表热度流通量**

- ⑤
```
/*第5行*/
  :units = "J m-2";
```
描述变量值的单位 也就是 **焦耳/平方米**


- ⑥
```
/*第6行*/
  :stagger = "";
```

在 **数值天气预测**  与 **气候模型** 中常用的 交错网格

一个 `空的` 对交错属性的描述 通常意味着这个变量 并非是交错的


- ⑦
```
/*第7行*/
  :coordinates = "XLONG XLAT XTIME";
```

坐标系变量提供变量 `ACGRDFLX` 实际的 **纬度**，**经度** 与 **时间值** 指标维度 

`XLONG` 对应 `west_east`

`XLAT` 对应 `south_north` 

`XTIME` 对应 `Time`

### 📌以其中一个 `-` 为例

```
int BATHYMETRY_FLAG(Time=1);
  :FieldType = 106; // int
  :MemoryOrder = "0  ";
  :description = "Flag for bathymetry in the global attributes for metgrid data";
  :units = "-";
  :stagger = "";
```
以上 code snippet 以 NCL(NCAR Command Language), 编写 用于大气与海洋学的 **数据处理** 与 **可视化** 

代码描述了 函数 或者 变量

但 code format 上有一些 混乱

既不是 NCL 也不是其他 common language 的代码风格

- ① 
```
/*第1行*/
int BATHYMETRY_FLAG(Time=1);
```
定义了一个 integer 类型的变量 `BATHYMETRY_FLAG` 单一 `Time` 维度，值设定为1.

其他行为 变量 设定 元数据，例如 `FieldType`，`MemoryOrder`，`description`，`units`，`staggering`

如果你要创建一个 netCDF文件，以下是一个使用 带 `netCDF4` 模块的 Python 例子

``` python
from netCDF4 import Dataset

rootgrp = Dataset("test.nc", "w", format="NETCDF4")

# Define Time dimension
time = rootgrp.createDimension("Time", 1)

# Define BATHYMETRY_FLAG variable
bathymetry_flag = rootgrp.createVariable("BATHYMETRY_FLAG","i4"("Time",))

# Set attributes
bathymetry_flag.FieldType = 106
bathymetry_flag.MemoryOrder = "0  "
bathymetry_flag.description = "Flag for bathymetry in the global attributes for metgrid data"
bathymetry_flag.units = "-"
bathymetry_flag.stagger = ""

rootgrp.close()
```

### 📌以其中一个 `1D` 为例

```
float C1F(Time=1, bottom_top_stag=72);
  :FieldType = 104; // int
  :MemoryOrder = "Z  ";
  :description = "full levels, c1f = d bf / d eta, using znu";
  :units = "Dimensionless";
  :stagger = "Z";
```
只是把变量名 换成了 `C1F` 

类型为 浮点数 

netCDF 类型的格式，但不是直接执行的代码

更像是一个变量的 specification 或者 metadata 

``` python
from netCDF4 import Dataset

rootgrp = Dataset("test.nc", "w", format="NETCDF4")

# Define dimensions
time = rootgrp.createDimension("Time", 1)
bottom_top_stag = rootgrp.createDimension("bottom_top_stag", 72)

# Define C1F variable 
C1F = rootgrp.createVariable("C1F","f4",("Time","bottom_top_stag",))

# Set attributes
C1F.FieldType = 104
C1F.MemoryOrder = "Z  "
C1F.description = "full levels, c1f = d bf / d eta, using znu"
C1F.units = "Dimensionless"
C1F.stagger = "Z"

rootgrp.close()
```
# Main 🍚实验方法与步骤
## 1.File Conversion文件📃转换：
转化为通用格式 **网络通用数据表NetCDF (Network Common Data Form)** 

## 2.Web Framework 框架选择：
- [Leaflet](https://github.com/Leaflet/Leaflet): 一个 JavaScript 库的交互式地图🗺️  🔗  [leafletjs](https://leafletjs.com/)
- [OpenLayers](https://github.com/openlayers/openlayers): 另一个 JavaScript 库用来展示地图🗺️与地理空间数据  🔗  [openlayers](https://openlayers.org/)
- [Cesium](https://github.com/CesiumGS/cesium): 基于WebGL 的 JavaScript 库 渲染 3D 全球与地图🗺️ 🔗  [CesiumGS](https://cesium.com/platform/cesiumjs/)
  - 1.installation &setup: 安装与设置
  - 
  - 2.displaying a basic map: 展示基础地图
  - 
  - 3.adding entities and data: 添加实体与数据
  - 
  - 4.loading & visualizing geospatial data: 加载与可视化地理空间数据
  - 
  - 5.interactivity and user interaction: 交互性与互动
  - 
  - 6.CesiumJS extensions: CesiumJS 插件
  - 
- [D3.js](https://github.com/d3/d3): 动态交互式数据可视化 🔗  [d3js](https://d3js.org/)


## 3.Data Extraction 数据提取：
### 2023-05-23 更新
~~删除的文字内容~~

~~### 3.X.已通过非CLI安装Homebrew的可以忽略~~

~~<img width="250" alt="40e59cb5819ae2c80a44023d8235be1" src="https://github.com/ChenxingWang93/analyze-visualize-wrfout-file/assets/31954987/8ce2ae27-f684-4af3-8541-75188da1c9aa">~~

### 3.X. use homebrew to install `pip` run following command in terminal
``` bash
brew install python
```
### 3.X. verifying `pip` is working correctly by running the following command:
``` bash
pip --version
```
### 3.X. 下载并安装 `netCDF4` 库library与其依赖dependencies
``` bash
pip install netCDF4
```
<img width="250" alt="0b6d1299bb04f902bf4d63085179b50" src="https://github.com/ChenxingWang93/analyze-visualize-wrfout-file/assets/31954987/be90c9f1-5686-44a7-b0b2-d23a7bf58337">

### 2023-05-22 更新
~~### prerequisite: Python installed on system~~

~~读取 `NetCDF` 文件 访问特定 变量variables e.g.水气vapor~~

~~### 3.X.install the required libraries~~
``` shell
pip install netCDF4 xarray
```

~~### 3.X.导入必要模块~~
``` Python
import xarray as xr
import json
```

~~### 3.X.使用 `xarray` 打开 `wrfout` 文件~~
``` Python
file_path = 'path_to_your_file/wrfout.nc'  #用真实路径替代
wrf_data = xr.open_dataset(file_path)
```

~~### 3.X.提取想要转化为 `JSON` 的变量~~
``` Python
variables = ['variableName1', 'variableName2', 'variableName3'] #Water vapor mixing ratio, U-component of wind, V-component of wind
data = wrf_data[variables].to_dict()
```
~~提取转化为JSON的变量名~~

~~### 3.X.create JSON Object: 转化提取出的数据为JSON 对象 or 数据结构
以nested dictionary 或者 a list of dictionaries 表示~~
``` Python
# create JSON object
data = {
    'temperature': temperature.tolist(),
    'latitude': latitude.tolist()
}
# convert to JSON string
json_data = json.dumps(data)
```
~~`tolist()` method is used to convert the NumPy array data to a native Python list~~

~~### 3.X.Write JSON to file: 保存JSON 数据到文件~~
``` Python
with open('/path/to/output.json', 'w') as outfile:
    outfile.write(json_data)
```

~~### 3.X.for~~
``` Python
```

### 2023-05-24 更新
``` Python
import netCDF4 as nc
import json

file_path = 'path_to_your_file.nc'

nc_file = nc.Dataset(file_path)

# and retrieve a 'QVAPOR' variable \\提取 'QVAPOR' 变量
data = nc_file.variables['QVAPOR']

# after converting the variable data to a list \\把变量数据转成 list
dataVapor = data[:].tolist()

# using `json.dumps()` to convert it to a JSON-formatted string, \\使用 `json.dumps()` 把这个list转成一个 JSON格式的 string
json_data = json.dumps(dataVapor)

print(json_data)
```
<img width="750" alt="Screen Shot 2023-05-25 at 11 44 52" src="https://github.com/ChenxingWang93/analyze-visualize-wrfout-file/assets/31954987/c4aa7554-f673-4f6b-837d-acdd60d49a7b">

### 2023-06-02 更新
- ① 
``` python
pip install pandas
```
<img width="750" alt="Screen Shot 2023-06-04 at 11 01 30" src="https://github.com/ChenxingWang93/analyze-visualize-wrfout-file/assets/31954987/f6d9d785-bd5f-413d-8de7-7b0913e7eb2f">

a lib in python for data manipulation and analysis it provides data structures and functions that make it easier to work with structured data such as 
CSV 文件，
Excel 电子表格，
SQL 数据库，

- ②
``` python
pip install matplotlib
```
<img width="750" alt="Screen Shot 2023-06-04 at 11 16 36" src="https://github.com/ChenxingWang93/analyze-visualize-wrfout-file/assets/31954987/f288a6ef-bfde-4b46-b517-81b6ebefec7e">

matplotlib is a data visualization lib in Python. It provides wide range of functions and classes for creating static, animated, and interactive visualizations in various formats.

installation 安装
``` python
pip install matplotlib
```
import 导入
``` python
import matplotlib.pyplot as plt
```
2 main interfaces for creating plots: 

1.the MATLAB-style:
``` python
import matplotlib.pyplot as plt

# Data for the x-axis and y-axis
x = [1, 2, 3, 4, 5]
y = [2, 4. 6, 8, 10]

# Create a line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')

# show the plot
plt.show()
```

2.the object-oriented interface: create a Figure object and then add Axes objects
``` python
import matplotlib.pyplot as plt

# Data for the x-axis and y-axis
x = [1, 2, 3, 4, 5]
y = [2, 4. 6, 8, 10]

# create a Figure object and then add Axes objects
fig, ax = plt.subplots()

# plot the data
ax.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.set_title('Line Plot')

# show the plot
plt.show()
```
Matplotlib offers many other types of plots, including bar plots, scatter plots, histograms, pie charts, and more. extensive customization options for colors, markers, line styles, legends and annotations, [Matplotlib documentation](https://matplotlib.org/stable/contents.html)

#### line 14 

write the contents of a 4-dimensional array (`arr`) to a CSV file specified by the `filename` parameter

``` Python
def print_array_to_file(arr, dataVapor):
    with open('dataVapor.csv', 'w') as file
        for i in range(arr.shape[0]):
            file.write('[')
            for j in range(arr.shape[1]):
                file.write('[')
                for k in range(arr.shape[2]):
                    file.write('[')
                    for l in range(arr.shape[3]):
                        file.write(str(arr[i, j, k, l]) + ',')
                    file.write(']' + '\n')
                file.write(']' + '\n')
            file.write(']' + '\n')
        file.write(']' + '\n')
```

#### line 46

从 4 维数组 `dataVapor` 创建一系列图像

通过迭代 一个范围 内的值 &通过 `imshow` & `savefig`函数 保存每张图片来实现

⬇️ 保存多个图像 来实现

``` Python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

for i in range(0, 71): # `0` to `70`(71 iterations)
    ax.imshow(dataVapor[0, i, :, :]) # display a single image from `dataVapor` on the axes
    plt.savefig('dataVapor' + str(i) + '.png') # `savefig()` function save figure as a PNG file
    ax.clear() # clear axes for the next iteration
plt.close(fig) # close the figure once all images are saved
```


### 2023-06-05 更新

``` 
brew install subversion
```
<img width="750" alt="Screen Shot 2023-06-05 at 10 01 09" src="https://github.com/ChenxingWang93/analyze-visualize-wrfout-file/assets/31954987/1e7933eb-5672-41a5-886b-e9dc3be15179">


## 4.Data Processing 数据处理：
处理 提取出的数据

包含随着时间推移的聚合数据 aggregating data over time

拟合数值或者执行数值计算 interpolating values, or performing statistical calculations

## 5.Visualization 可视化：
在地图上基于时间序列绘制数据 plot the data on a map, generate time series plots

## 6.Web integration 植入：
嵌入 HTML 结构

CSS 风格化

## 7.Hosting 托管：
部署到网络服务器或者托管平台

确保必要的依赖(JavaScript libraries) wrfout 文件能够通过网页应用程序被访问

## 8.Testing 测试：
保证兼容性 

跨浏览器

跨设备

# Result 🎬 结果

# How to contribute 如何贡献？
if you are interested in joining research &development, please fork the repo and submit a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) with your changes.

如果你有兴趣加入研发过程，请 fork 仓库或者提交拉取请求

# License
to be determined 

# Copyright 版权©️
2023 Nan Xia, Hongxiong Xu, Chenxing Wang and others
other individual files related to copyright attribution await further designation

# Contact 联系
