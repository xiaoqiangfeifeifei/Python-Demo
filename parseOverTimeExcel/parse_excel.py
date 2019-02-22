# -*- coding: utf-8 -*- 
import xdrlib,sys
import xlrd
import xlwt
import datetime

sumTime = 0

def open_excel(file='加班表.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))
#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file = '加班表.xls', colnameindex = 0,by_index = 0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #数据列名
    list =[]
    for rownum in range(1, nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                try:
                    app[colnames[i]] = xlrd.xldate_as_tuple(table.cell(rownum,i).value, 0)
                except Exception as e:
                    app[colnames[i]] = row[i]

             list.append(app)
             for index, val in enumerate(list):
                tupleStart = val['开始时间']
                tupleEnd = val['结束时间']
                startTime = datetime.datetime(2018, 1, 28, tupleStart[3], tupleStart[4])
                endTime = datetime.datetime(2018, 1, 28, tupleEnd[3], tupleEnd[4])
                if endTime < startTime:
                    print("第" + str(index + 1) + "行的 结束时间小于开始时间，请检查")
                    return []
                
                # 可视化时间
                times1 = datetime.datetime.strptime(str(tupleStart[3]) + ":"+ str(tupleStart[4]), "%H:%M")
                times2 = datetime.datetime.strptime(str(tupleEnd[3])+ ":"+ str(tupleEnd[4]), "%H:%M")
                times = str(times2 - times1).split(':')
                difftimeChar = times[0]+'小时'+times[1]+'分钟' #时间差
                val['时间差'] = difftimeChar
                # 实际时间
                hourTimeDiff = int(times[0])
                minuteTimeDiff = int(times[1])
                if (minuteTimeDiff == 0) or (minuteTimeDiff > 0 and minuteTimeDiff < 25):
                    val['加班时间'] = hourTimeDiff
                elif minuteTimeDiff >= 25 and minuteTimeDiff < 45:
                    val['加班时间'] = hourTimeDiff + 0.5
                elif  minuteTimeDiff >= 45 and minuteTimeDiff <= 60:
                    val['加班时间'] = hourTimeDiff + 1           
    for val in list:
        val['开始时间'] = str(val['开始时间'][3]) + ':' + str(val['开始时间'][4])
        val['结束时间'] = str(val['结束时间'][3]) + ':' + str(val['结束时间'][4])
        global sumTime
        sumTime += float(val['加班时间'])
    
    return list

def writeExcel(resultList):
    workbook = xlwt.Workbook(encoding = 'ascii')
    worksheet = workbook.add_sheet('Sheet1')
    colSize = 0
    for rowindex, rowVal in enumerate(resultList):
        if colSize == 0:
            colSize = len(rowVal)
        if rowindex == 0:
            for colIdx, key in enumerate(rowVal):
                worksheet.write(0, colIdx, label = key)
                worksheet.write(1, colIdx, label = str(rowVal[key]))
        else:
            for colIdx, key in enumerate(rowVal):
                worksheet.write(rowindex + 1, colIdx, label = str(rowVal[key]))
    worksheet.write(len(resultList) + 1, colSize - 1, label = str(sumTime))
    workbook.save('加班时间'+ str(datetime.datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-') +'.xls')

def main():
   tables = excel_table_byindex()
   writeExcel(tables)

if __name__=="__main__":
    main()