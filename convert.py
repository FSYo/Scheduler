# convert.py
import pandas as pd
import json

def excel_to_json(excel_file, json_file):
    # 读取 Excel 文件
    df = pd.read_excel(excel_file)

    # 将 DataFrame 转换为字典列表
    courses = df.to_dict(orient='records')

    # 将字典列表保存为 JSON 文件
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(courses, f, ensure_ascii=False, indent=4)

    print(f"转换完成！JSON 文件已保存为 {json_file}")

if __name__ == "__main__":
    # 输入 Excel 文件路径和输出的 JSON 文件路径
    excel_file = 'schedule.xlsx'  # 替换为你的 Excel 文件路径
    json_file = 'courses.json'   # 输出的 JSON 文件路径

    # 调用函数进行转换
    excel_to_json(excel_file, json_file)