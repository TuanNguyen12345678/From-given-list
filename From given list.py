gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]
so=[]
chu=[]
for i in gadgets:
    if isinstance(i,str):
        chu.append(i)
    else:
        so.append(i)
print("List chứa chuỗi là: ",chu)
print("List chứa số là: ",so)
# Sắp xếp chuỗi:
chu.sort()
print("Sắp xếp chuỗi theo thứ tự tăng dần là: ",chu)
chu.sort(reverse=True)
print("Sắp xếp chuỗi theo thứ tự tăng dần là: ",chu)
# Sắp xếp số:
so.sort()
print("Sắp xếp số theo thứ tự tăng dần là: ",so)
so.sort(reverse=True)
print("Sắp xếp số theo thứ tự giảm dần là: ",so)