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
### prerequisite: Python installed on system
读取 `NetCDF` 文件 访问特定 变量variables e.g.水气vapor
### 3.X.install the required libraries 
``` shell
pip install netCDF4 xarray
```

### 3.X.导入必要模块 
``` Python
import xarray as xr
import json
```

### 3.X.使用 `xarray` 打开 `wrfout` 文件 
``` Python
file_path = 'path_to_your_file/wrfout.nc'  #用真实路径替代
wrf_data = xr.open_dataset(file_path)
```

### 3.X.提取想要转化为 `JSON` 的变量
``` Python
variables = ['variableName1', 'variableName2', 'variableName3']  #Water vapor mixing ratio, U-component of wind, V-component of wind
data = wrf_data[variables].to_dict()
```
提取转化为JSON的变量名

### 3.X.create JSON Object: 转化提取出的数据为JSON 对象 or 数据结构
以nested dictionary 或者 a list of dictionaries 表示
``` Python
# create JSON object
data = {
    'temperature': temperature.tolist(),
    'latitude': latitude.tolist()
}
# convert to JSON string
json_data = json.dumps(data)
```
`tolist()` method is used to convert the NumPy array data to a native Python list 

### 3.X.Write JSON to file: 保存JSON 数据到文件
``` Python
with open('/path/to/output.json', 'w') as outfile:
    outfile.write(json_data)
```

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
