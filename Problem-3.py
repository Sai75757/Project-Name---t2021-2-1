#python
def generate_series(x):
    series = []
    for i in range(1, x*2):
        if i % 2 != 0:
            series.append(i)
        if len(series) == x:
            break
    return series
# Example
input_a = int(input("enter a number= "))
output = generate_series(input_a)
print(output)
