k# 将每一页为A3大小的pdf拆分为两页A4大小，并保存为pdf文件
from PyPDF2 import PdfWriter, PdfReader


def split_pdf(input_pdf_path, output_pdf_path):
    """
    将A3大小的PDF页面拆分为两个A4页面

    参数:
        input_pdf_path: 输入PDF文件路径
        output_pdf_path: 输出PDF文件路径
    """
    # 创建PDF写入器
    writer = PdfWriter()

    # 打开输入PDF文件
    with open(input_pdf_path, "rb") as file:
        reader = PdfReader(file)
        total_pages = len(reader.pages)

        print(f"原始PDF共有 {total_pages} 页")
        print("开始拆分...")

        # 遍历每一页
        for page_num in range(total_pages):
            # 获取原始页面
            original_page = reader.pages[page_num]

            # 获取原始页面的尺寸
            page_width = float(original_page.mediabox.width)
            page_height = float(original_page.mediabox.height)

            print(f"\n处理第 {page_num + 1} 页，尺寸: {page_width} x {page_height}")

            # 计算中点（从中间拆分）
            mid_point = page_width / 2

            # 创建左半部分（第一个A4页面）
            # 需要重新获取页面以避免修改原始对象
            left_page = reader.pages[page_num]
            # 裁剪左半部分：保留左边，去掉右边
            left_page.mediabox.upper_right = (mid_point, page_height)
            left_page.mediabox.lower_left = (0, 0)
            writer.add_page(left_page)
            print(f"  - 左半部分: 0 到 {mid_point}")

            # 创建右半部分（第二个A4页面）
            # 重新获取原始页面（未被修改的）
            right_page = reader.pages[page_num]
            # 裁剪右半部分：保留右边，通过调整左边界实现
            right_page.mediabox.upper_right = (page_width, page_height)
            right_page.mediabox.lower_left = (mid_point, 0)
            writer.add_page(right_page)
            print(f"  - 右半部分: {mid_point} 到 {page_width}")

        print(f"\n拆分完成！原始 {total_pages} 页 -> 生成 {len(writer.pages)} 页")

    # 写入输出文件
    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)

    print(f"文件已保存到: {output_pdf_path}")


if __name__ == "__main__":
    input_file = "/Users/hank/Downloads/格_第一次月考综合测试卷(1).pdf"
    output_file = "output_A4.pdf"

    split_pdf(input_file, output_file)

