class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ch = [['','I','II','III','IV','V','VI','VII','VIII','IX'],
        ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
        ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
        ['','M','MM','MMM']]

        str = ''

        str += ch[3][num//1000 % 10]
        str += ch[2][num//100 % 10]
        str += ch[1][num//10 % 10]
        str += ch[0][num%10]

        return str