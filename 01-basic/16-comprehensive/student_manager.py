# 学生成绩管理系统

class StudentManager:
    """学生成绩管理系统"""

    def __init__(self):
        self.students = {}  # {学号: 学生信息}

    def add_student(self, student_id, name, age):
        """添加学生"""
        if student_id in self.students:
            print(f"学号{student_id}已存在")
            return False

        self.students[student_id] = {
            "id": student_id,
            "name": name,
            "age": age,
            "scores": {}
        }
        print(f"✓ 添加学生：{name}")
        return True

    def add_score(self, student_id, subject, score):
        """添加成绩"""
        if student_id not in self.students:
            print(f"学号{student_id}不存在")
            return False

        self.students[student_id]["scores"][subject] = score
        print(f"✓ 录入成绩：{subject} = {score}")
        return True

    def get_student(self, student_id):
        """查询学生信息"""
        return self.students.get(student_id)

    def get_average(self, student_id):
        """计算学生平均分"""
        student = self.get_student(student_id)
        if not student or not student["scores"]:
            return None

        scores = student["scores"].values()
        return sum(scores) / len(scores)

    def get_top_students(self, n=5):
        """获取成绩最好的N名学生"""
        # 计算每个学生的平均分
        student_avgs = []
        for sid, student in self.students.items():
            if student["scores"]:
                avg = sum(student["scores"].values()) / len(student["scores"])
                student_avgs.append((student["name"], avg))

        # 排序并返回前N名
        student_avgs.sort(key=lambda x: x[1], reverse=True)
        return student_avgs[:n]

    def get_subject_stats(self, subject):
        """统计某科目的成绩分布"""
        scores = []
        for student in self.students.values():
            if subject in student["scores"]:
                scores.append(student["scores"][subject])

        if not scores:
            return None

        return {
            "count": len(scores),
            "max": max(scores),
            "min": min(scores),
            "avg": sum(scores) / len(scores)
        }

    def find_by_score_range(self, subject, min_score, max_score):
        """查找某科目分数在指定范围内的学生"""
        result = []
        for student in self.students.values():
            if subject in student["scores"]:
                score = student["scores"][subject]
                if min_score <= score <= max_score:
                    result.append({
                        "name": student["name"],
                        "score": score
                    })
        return result

# 使用示例
if __name__ == "__main__":
    # 创建管理器
    manager = StudentManager()

    # 添加学生
    manager.add_student("2024001", "张三", 18)
    manager.add_student("2024002", "李四", 19)
    manager.add_student("2024003", "王五", 18)

    # 录入成绩
    manager.add_score("2024001", "数学", 95)
    manager.add_score("2024001", "英语", 88)
    manager.add_score("2024001", "物理", 92)

    manager.add_score("2024002", "数学", 87)
    manager.add_score("2024002", "英语", 94)
    manager.add_score("2024002", "物理", 89)

    manager.add_score("2024003", "数学", 92)
    manager.add_score("2024003", "英语", 85)
    manager.add_score("2024003", "物理", 95)

    # 查询学生
    student = manager.get_student("2024001")
    print(f"\n学生信息：{student['name']}")
    print(f"成绩：{student['scores']}")

    # 计算平均分
    avg = manager.get_average("2024001")
    print(f"平均分：{avg:.2f}")

    # 获取前3名
    print("\n前3名学生：")
    top_students = manager.get_top_students(3)
    for i, (name, avg) in enumerate(top_students, 1):
        print(f"{i}. {name}: {avg:.2f}")

    # 统计数学成绩
    print("\n数学成绩统计：")
    stats = manager.get_subject_stats("数学")
    if stats:
        print(f"人数：{stats['count']}")
        print(f"最高分：{stats['max']}")
        print(f"最低分：{stats['min']}")
        print(f"平均分：{stats['avg']:.2f}")

    # 查找数学成绩90分以上的学生
    print("\n数学90分以上：")
    excellent = manager.find_by_score_range("数学", 90, 100)
    for item in excellent:
        print(f"{item['name']}: {item['score']}")
