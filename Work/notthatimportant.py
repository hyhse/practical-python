sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == 'Runoob':
        print(f"找到了 {site}永远的神")
        break
    print("循环数据 " + site)
else:
    print("到底了!")
print("完成循环!")
