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

以其中一个`Geo2D`为例
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

#### 
