def rec(ar,ans,mp,cmb,ind):
    if ind>len(ar):
        return
    if len(cmb)==len(ar):
        ans.append(cmb[:])
        return
    numb=ar[ind]
    code=mp[numb]
    for x in code:
        rec(ar,ans,mp,cmb+x,ind+1)

    return ans



data = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
a='34'
import matplotlib.pyplot as plt

an=rec(a,[],data,'',0)

print(an)
data = {'velocity' : [2,4,6,8,12,50],
        'time' : ['12:08:00', '12:08:02', '12:08:04', '12:08:06', '12:08:08', '2:08:10']}

plt.plot(data['velocity'])
plt.xticks(range(len(data['time'])), data['time'])