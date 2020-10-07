import pandas
from pandas import DataFrame

if __name__ == '__main__':
    print("parser rdf")
    file = open('1.rdf', 'rb')
    data = dict()
    out = dict()
    
    f = 1
    while f != '>':
    	f = file.read(1)

    df = DataFrame()
    df.to_excel('1.xlsx', sheet_name="Sheet 1")
    writer = pandas.ExcelWriter('1.xlsx')

    legenda = ['№ Исходник','формат','Результат','имя','группа']

    name_group = ['AnalogInput','AnalogInput','AnalogInput','AnalogInput','AnalogInput',
                  'DigitalInput','DigitalInput',
                  'DigitalOutput','DigitalOutput','DigitalOutput','DigitalOutput','DigitalOutput','DigitalOutput','DigitalOutput','DigitalOutput','DigitalOutput',
                  'DigitalInput','DigitalInput','DigitalInput','DigitalInput',
                  'not',
                  'DigitalInput','DigitalInput','DigitalInput','DigitalInput','DigitalInput','DigitalInput','DigitalInput','DigitalInput','DigitalInput','DigitalInput','DigitalInput','DigitalInput','DigitalInput','DigitalInput','DigitalInput','DigitalInput',
                  'AnalogInput','AnalogInput','AnalogInput']

    name_param = ['Ia_kt','ic_kt','ia_bb1','uab_bb1','uab_bb2','bus2_u03_up','bus1_u03_up','mestn','kt_vkl','cb_vkl','cb_otkl',
                'bb1_otkl','bb1_vkl', 'bb2_otkl','bb2_vkl','zb_otkl','shu_vkl','bb2_off','cb_off','bb1_off','not','kt_imax_down',
                'kt_imin1_down','kt_imin3_down','sinxrn_block','faza1_less','bus1_u08_down','bus1_u06_up','bb1_imax_down','bb1_imin_down',
                'bb1_u09_down','faza2_less','bus2_u08_down','bus2_u06_up','bb2_imax_down','bb2_imin_down','bb2_u09_down','ia_bb2','ic_bb2',
                'ic_bb1']

    number = ['1','2','3','4','5','','','','','6','','','','','','','','','7','','','','','','','','','8','','','','','','','9','','','10','11','12']

    j = 1

    leg = dict()

    for i in range(40):
        leg['Type signal'] = name_param

    out[0] = leg

    for str in file:
        d = {name_param[0]: 0, name_param[1]: 0, name_param[2]: 0, name_param[3]: 0, name_param[4]: 0,name_param[5]: 0, name_param[6]: 0,
             name_param[7]: 0, name_param[8]: 0, name_param[9]: 0, name_param[10]: 0, name_param[11]: 0, name_param[12]: 0,
             name_param[13]: 0, name_param[14]: 0, name_param[15]: 0, name_param[16]: 0, name_param[17]: 0, name_param[18]: 0
            , name_param[19]: 0, name_param[20]: 0, name_param[21]: 0, name_param[22]: 0, name_param[23]: 0, name_param[24]: 0,
             name_param[25]: 0, name_param[26]: 0, name_param[27]: 0, name_param[28]: 0, name_param[29]: 0,
             name_param[30]: 0, name_param[31]: 0, name_param[32]: 0, name_param[33]: 0, name_param[34]: 0,
             name_param[35]: 0, name_param[36]: 0, name_param[37]: 0, name_param[38]: 0, name_param[39]: 0}

        f1 = int.from_bytes(str[0:2],'little')
        f2 = int.from_bytes(str[2:4],'little')
        f3 = int.from_bytes(str[4:6],'little')
        f4 = int.from_bytes(str[6:8],'little')
        f5 =  int.from_bytes(str[8:10],'little')
        f6 = int.from_bytes(str[10:11],'big')
        f7 = int.from_bytes(str[11:12],'big')
        f8 = int.from_bytes(str[12:13],'big')
        f9 = int.from_bytes(str[14:15],'big')
        f10 = int.from_bytes(str[15:17],'little')
        f11 = int.from_bytes(str[17:19],'little')
        f12 = int.from_bytes(str[19:21],'little')

        d[name_param[0]] = f1;
        d[name_param[1]] = f2;
        d[name_param[2]] = f3;
        d[name_param[3]] = f4;
        d[name_param[4]] = f5;
        d[name_param[5]] = f6 & 1;
        d[name_param[6]] = (f6 >> 1) & 1;
        d[name_param[7]] = (f6 >> 2) & 1;
        d[name_param[8]] = (f6 >> 3) & 1;
        d[name_param[9]] = (f6 >> 4) & 1;
        d[name_param[10]] = (f6 >> 5) & 1;
        d[name_param[11]] = (f6 >> 6) & 1;
        d[name_param[12]] = (f6 >> 7) & 1;
        d[name_param[13]] = f7 & 1;
        d[name_param[14]] = (f7 >> 1) & 1;
        d[name_param[15]] = (f7 >> 2) & 1;
        d[name_param[16]] = (f7 >> 3) & 1;
        d[name_param[17]] = (f7 >> 4) & 1;
        d[name_param[18]] = (f7 >> 5) & 1;
        d[name_param[19]] = (f7 >> 6) & 1;
        d[name_param[20]] = (f7 >> 7) & 1;
        d[name_param[21]] = f7 & 1;
        d[name_param[22]] = (f8 >> 1) & 1;
        d[name_param[23]] = (f8 >> 2) & 1;
        d[name_param[24]] = (f8 >> 3) & 1;
        d[name_param[25]] = (f8 >> 4) & 1;
        d[name_param[26]] = (f8 >> 5) & 1;
        d[name_param[27]] = (f8 >> 6) & 1;
        d[name_param[28]] = (f8 >> 7) & 1;
        d[name_param[29]] = f9 &1;
        d[name_param[30]] = (f9 >> 1) & 1;
        d[name_param[31]] = (f9 >> 2) & 1;
        d[name_param[32]] = (f9 >> 3) & 1;
        d[name_param[33]] = (f9 >> 4) & 1;
        d[name_param[34]] = (f9 >> 5) & 1;
        d[name_param[35]] = (f9 >> 6) & 1;
        d[name_param[36]] = (f9 >> 7) & 1;
        d[name_param[37]] = f10;
        d[name_param[38]] = f11;
        d[name_param[39]] = f12;
        out[j] = d
        j = j + 1

df_ = DataFrame(out)
df_.to_excel(writer, startcol=1, startrow=1, header=None)
writer.save()

