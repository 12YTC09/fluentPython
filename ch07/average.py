#
#average_oo.py:更高階的移動平均值的計算函式

def make_averager():
    series = []

    def averager(new_value):
        self.series.append(new_value)
        total =sum(series)
        return total/len(series)

    return averager

