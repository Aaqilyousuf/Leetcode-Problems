class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
       
        f = (celsius*(9/5)) + 32
        k = celsius + 273.15
        return [k, f]