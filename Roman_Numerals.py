class RomanNumerals(object):
    @staticmethod
    def from_roman(s):
        roman_l = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(s):
            if i+1<len(s) and s[i:i+2] in roman_l:
                num+=roman_l[s[i:i+2]]
                i+=2
            else:
                num+=roman_l[s[i]]
                i+=1
        return num

    @staticmethod
    def to_roman(numb):
        arabic_l = {1:'I',3: "III",2:"II",5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM',
                    8:"VIII", 7:"VII", 6:"VI",  2000:"MM", 3000:"MMM", 700:"DCC", 600:"DC", 300:"CCC", 200:"CC", 1990: "MCMXC",
                    80:"LXXX", 70:"LXX", 60:"LX", 30:"XXX", 20:"XX", 0: "",4000: "MMMM", 5000: "MMMMM", 6000: "MMMMMM"
                    }
        i = 0
        str_numb = str(numb)
        num = ""
        if numb in arabic_l.keys():
            return arabic_l[numb]
        while i < len(str_numb):
            if i+1<len(str_numb) and int(str_numb[i:i+2])*10**(len(str_numb)-1-i) in arabic_l:
                num+= arabic_l[int(str_numb[i:i+2])*10**(len(str_numb)-1-i)]
                i+=2
            else:
                num+=arabic_l[int(str_numb[i])*10**(len(str_numb)-1-i)]
                i+=1
        return num