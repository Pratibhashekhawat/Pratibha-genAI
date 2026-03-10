#Unique Product Purchase Analyzer
class Solution:
    def unique_products(self, products):
        result = []
        #Write your code here
        for p in products:
            if products.count(p)==1:
                result.append(p)

        return result