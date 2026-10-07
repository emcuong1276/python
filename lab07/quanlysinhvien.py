danh_sach_sv = [
    {
        "ma_sv": "SV001",
        "ho_ten": "Nguyen Van An",
        "diem": 8.5
    },
    {
        "ma_sv": "SV002",
        "ho_ten": "Tran Thi Binh",
        "diem": 6.5
    },
    {
        "ma_sv": "SV003",
        "ho_ten": "Le Van Cuong",
        "diem": 4.5
    }
]


def nhap_so():
    while True:
        try:
            return float(input("Nhập điểm: "))
        except ValueError:
            print("Lỗi! Vui lòng nhập số.")


def xep_loai(diem):
    if diem >= 8:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"


def hien_thi_sinh_vien():
    print("\n===== DANH SÁCH SINH VIÊN =====")

    if len(danh_sach_sv) == 0:
        print("Chưa có sinh viên.")
        return

    for sv in danh_sach_sv:
        print(
            f"Mã: {sv['ma_sv']} | "
            f"Họ tên: {sv['ho_ten']} | "
            f"Điểm: {sv['diem']} | "
            f"Xếp loại: {xep_loai(sv['diem'])}"
        )


def tim_sinh_vien():
    ma_sv = input("Nhập mã sinh viên cần tìm: ")

    for sv in danh_sach_sv:
        if sv["ma_sv"] == ma_sv:
            print("\nTìm thấy sinh viên:")
            print(f"Mã: {sv['ma_sv']}")
            print(f"Họ tên: {sv['ho_ten']}")
            print(f"Điểm: {sv['diem']}")
            print(f"Xếp loại: {xep_loai(sv['diem'])}")
            return

    print("Không tìm thấy sinh viên.")


def them_sinh_vien():
    print("\n===== THÊM SINH VIÊN =====")

    ma_sv = input("Nhập mã sinh viên: ")

    for sv in danh_sach_sv:
        if sv["ma_sv"] == ma_sv:
            print("Mã sinh viên đã tồn tại!")
            return

    ho_ten = input("Nhập họ tên: ")
    diem = nhap_so()

    if diem < 0 or diem > 10:
        print("Điểm phải từ 0 đến 10!")
        return

    sinh_vien = {
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "diem": diem
    }

    danh_sach_sv.append(sinh_vien)

    print("Thêm sinh viên thành công!")


def sua_sinh_vien():
    print("\n===== SỬA SINH VIÊN =====")

    ma_sv = input("Nhập mã sinh viên cần sửa: ")

    for sv in danh_sach_sv:
        if sv["ma_sv"] == ma_sv:
            sv["ho_ten"] = input("Nhập họ tên mới: ")
            sv["diem"] = nhap_so()

            print("Cập nhật thành công!")
            return

    print("Không tìm thấy sinh viên.")


def xoa_sinh_vien():
    print("\n===== XÓA SINH VIÊN =====")

    ma_sv = input("Nhập mã sinh viên cần xóa: ")

    for sv in danh_sach_sv:
        if sv["ma_sv"] == ma_sv:
            danh_sach_sv.remove(sv)
            print("Xóa sinh viên thành công!")
            return

    print("Không tìm thấy sinh viên.")


def thong_ke():
    print("\n===== THỐNG KÊ =====")

    gioi = 0
    kha = 0
    trung_binh = 0
    yeu = 0

    for sv in danh_sach_sv:
        loai = xep_loai(sv["diem"])

        if loai == "Giỏi":
            gioi += 1
        elif loai == "Khá":
            kha += 1
        elif loai == "Trung bình":
            trung_binh += 1
        else:
            yeu += 1

    print(f"Số sinh viên Giỏi: {gioi}")
    print(f"Số sinh viên Khá: {kha}")
    print(f"Số sinh viên Trung bình: {trung_binh}")
    print(f"Số sinh viên Yếu: {yeu}")


def menu():
    while True:
        print("\n========== QUẢN LÝ SINH VIÊN ==========")
        print("1. Hiển thị danh sách sinh viên")
        print("2. Tìm sinh viên")
        print("3. Thêm sinh viên")
        print("4. Sửa sinh viên")
        print("5. Xóa sinh viên")
        print("6. Thống kê")
        print("0. Thoát")
        print("========================================")

        lua_chon = input("Nhập lựa chọn: ")

        if lua_chon == "1":
            hien_thi_sinh_vien()
        elif lua_chon == "2":
            tim_sinh_vien()
        elif lua_chon == "3":
            them_sinh_vien()
        elif lua_chon == "4":
            sua_sinh_vien()
        elif lua_chon == "5":
            xoa_sinh_vien()
        elif lua_chon == "6":
            thong_ke()
        elif lua_chon == "0":
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")


menu()