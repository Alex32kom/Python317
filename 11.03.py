root = r'nested1\nested2'
objs = os.listdir(root)
print(objs)
objs = list(map(lambda i: os.path.join(root, i), objs))
print(objs)


obj_sort = sorted(objs, key = os.path.isfile, reverse=True)
print(obj_sort)
print(sorted(objs, reverse=True))