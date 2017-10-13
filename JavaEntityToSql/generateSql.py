# -*- coding: utf-8 -*-
#!/usr/bin/env python3

__author__ = 'liqiang'

'''
根据java实体文件生成sql
'''

import os,sys,re

# 处理java文件
def eachFile():
    javaFilePath = ''
    fieldList = []
    generalFieldList = []
    entityFieldDict = {}

    pwd = os.getcwd()# 获取当前文件路径
    pathDir = os.listdir(pwd) # 获取文件夹
    for filename in pathDir: # 遍历文件夹
        if filename.find('.java') > 0:
            javaFilePath = '%s%s%s'% (pwd,'\\',filename) # 得到java文件路径

    if javaFilePath == '':
        print('java file has not found!')
        sys.exit(1) # 无java文件时系统退出
    else:
        fopen = open(javaFilePath,'r',encoding='utf-8') # 根据文件路径读取java文件
        for eachLine in fopen:# 根据注解获取文件内容并加入fieldList中
            if eachLine.find('@Table') >= 0 or eachLine.find('@Column')>= 0 or eachLine.find('@Relation')>= 0 or eachLine.find('private')>= 0:
                fieldList.append(eachLine)

    for field in fieldList:
        if field.find('@Table') >= 0:
            masterTableName = getFieldIdByRegx(field)# 获取主表name
            masterTableAlias = masterTableName.split('_')[-1] # 主表别名（list倒数第一个元素）
            if masterTableAlias == 'users':#主表别名为users时sql报错，替换掉
                masterTableAlias = 'users_'
        elif field.find('@Column') >= 0:
            columnIndex = fieldList.index(field)
            if columnIndex+2 < len(fieldList) and fieldList[columnIndex+2].find('@Relation') >= 0: # 查找@Column下一行包括@Relation的->引用实体
                entityName = getEntityName(fieldList[columnIndex+3].split(' ')[1]) # 引用实体表名
                entityAlias = entityName.split('_')[-1] # 引用实体表别名
                entitySubDict = {}
                aliasSubDict = {}
                entityFieldDict[entityName] = entitySubDict
                entitySubDict['alias'] = aliasSubDict
                aliasSubDict['aliasValue'] = entityAlias
                aliasSubDict['field_name'] = getfieldNameAlias(getFieldIdByRegx(field))
                entitySubDict['field_id_temp'] = getFieldIdByRegx(field)
                entitySubDict['field_id'] = getfieldIdAlias(getFieldIdByRegx(field))
            else:
                generalFieldList.append(getFieldIdByRegx(field)) # 主表field

    sql = 'SELECT ';
    for generalField in generalFieldList:
        sql = sql + masterTableAlias + '.' + generalField + ',\n\t\t'


    if entityFieldDict:
        print(entityFieldDict)
        for (subDictKey,subDictValue) in entityFieldDict.items():
            print(subDictKey)
            for(k,v) in entityFieldDict[subDictKey].items():
                #print(k,v)
                if k == 'field_id_temp':
                    sql = sql + masterTableAlias + '.' + v + ' AS '
                if k == 'alias':
                    for (key, value) in v.items():
                        if key == 'aliasValue':
                            aliasValue = v[key]
                        elif key == 'field_name':
                            fieldName = v[key]
                    sql = sql + aliasValue + '.name'  +' AS ' + fieldName + ',\n\t\t'
                if k == 'field_id':
                    sql = sql + v + ',' + '\n\t\t'
        print(sql)
        sql = sql[0:len(sql)-4] # 去掉sql filed尾部的逗号
        sql = sql +'\n' +' FROM '+ masterTableName + ' AS ' + masterTableAlias
        # 拼接实体表名
        for (subDictKey, subDictValue) in entityFieldDict.items():
            sql = sql + ' LEFT JOIN '+ subDictKey + ' AS ' \
                            + entityFieldDict[subDictKey]['alias']['aliasValue'] + ' ON ' \
                            + entityFieldDict[subDictKey]['alias']['aliasValue'] + '.id = '\
                            + masterTableAlias + '.' +  entityFieldDict[subDictKey]['field_id_temp'] + '\n\t\t'
        sql = sql[0:len(sql) - 3]  # 去掉\n\t
        sql = sql +'\n'+ ' WHERE ' + masterTableAlias + '.domain_id = :domainId '
        print('带引用实体的sql')
        print(sql)
    else:
        sql = sql[0:len(sql) - 4]  # 去掉sql filed尾部的逗号
        sql = sql +'\n' + 'FROM ' + masterTableName + ' AS ' + masterTableAlias + '\n'
        sql = sql + 'WHERE ' + masterTableAlias + '.domain_id = :domainId '
        print('不带引用实体的sql')
        print(sql)
    saveSqlFile('demoSql.sql',sql) # 将处理得到的sql输出


# 获取field的id
def getFieldIdByRegx(field):
    return re.findall(r'name = "(.+?)"',field)[0]

# 获取引用实体表名
def getEntityName(entityNameRef):
    str = ''
    result = ''
    for char in entityNameRef:
        if char.isupper():
            str = str + ' '
            char = char.lower()
        str = str + char

    strList = str.split(' ')[1:len(str.split(' '))-1]

    for strs in strList:
        if strs != strList[-1]:
            result = result + strs + '_'
        else:
            result = result + strs
    # 结尾加s
    if result[-1] == 's':
        result = result + 'es'
    elif result[-1] == 'y':
        result = result[0:len(result)-1] + 'ies'
    else:
        result = result + 's'
    return result

# 处理引用实体的id别名
def getfieldIdAlias(fieldIdName):
    str = ''
    fieldIdNameList = fieldIdName.split('_')
    for char in fieldIdNameList:
        if char == fieldIdNameList[-2]:
            str = str + char + '__'
        else:
            str = str + char + '_'
    return str[0:len(str)-1]

# 处理引用实体的name别名
def getfieldNameAlias(fieldName):
    str = ''
    fieldIdNameList = fieldName.split('_')
    for char in fieldIdNameList:
        if char == fieldIdNameList[-2]:
            str = str + char + '__'
        else:
            str = str + char + '_'
    return str[0:len(str)-3]+'name'
# 保存sql
def saveSqlFile(fileName,contents):
    f = open(fileName, 'w',encoding='utf-8')
    f.write(contents)
    f.close()



eachFile()



