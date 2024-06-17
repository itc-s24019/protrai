# s24019 def2.py
#関数で消費税を計算するコード

def postTaxPrice(Price):
    ans = Price * 1.1
    return ans

print(postTaxPrice(120),"円")
print(postTaxPrice(128),"円")
print(postTaxPrice(980),"円")
