# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

def print_array_to_file (arr, dataVapor):
    with open('dataVapor.csv', 'w') as file:
        for i in range(arr.shape[0]):
            file.write('[')
            for j in range(arr.shape[1]):
                file.write('[')
                for k in range(arr.shape[2]):
                    file.write('[')
                    for l in range(arr.shape[3]):
                        file.write(str(arr[i, j, k, l])+',')
                    file.write(']' + '\n')
                file.write(']' + '\n')
            file.write(']'+'\n')
        file.write(']' + '\n')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import netCDF4 as nc
import json
import numpy as np
import matplotlib.pyplot as plt

# Open the WRF output file and using `netCDF4` to read a  NetCDF file(`file_path`) 打开、用`netCDF4`读
file_path = 'wrfout_d01_2022-08-29_00_00_00'

nc_file = nc.Dataset(file_path)

# and retrieve a 'QVAPOR' variable 提取 'QVAPOR' 变量
data = nc_file.variables['QVAPOR']

# after converting the variable data to a list 把变量数据转成 list
dataVapor = data[:] #"[:]"syntax in python called slicing, it creates a copy of the "data" variable
#print_array_to_file(dataVapor,'dataVapor.txt')

fig, ax = plt.subplots()
for i in range(0, dataVapor.shape[1]):  # `[1]` index 对应 size or length of the second dimension(axis 1) of the array
    ax.imshow(dataVapor[0, i, :, :])    # display a single image from `dataVapor` on the axes
    plt.savefig('dataVapor'+str(i)+'.png')  # `savefig()` function save figure as a PNG file
    ax.clear() # clear axes for the next iteration
plt.close(fig) # close the figure once all images are saved
# using `json.dumps()` to convert it to a JSON-formatted string, 使用 `json.dumps()` 把这个list转成一个 JSON格式的 string
#json_data = json.dumps(dataVapor)

# and finally, printing the JSON data 打印这些 JSON 数据，这些数据就是后端往前端发数据的基础了
#print(json_data)