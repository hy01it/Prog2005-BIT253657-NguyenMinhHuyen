def tinh_toan(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)
    return tong, lon_nhat, nho_nhat
nums = (3, 7, 2, 9, 5)
tong, max_val, min_val = tinh_toan(nums)
print("Tổng:", tong)
print("Giá trị lớn nhất:", max_val)
print("Giá trị nhỏ nhất:", min_val)
