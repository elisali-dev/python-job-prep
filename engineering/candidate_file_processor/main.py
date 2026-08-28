import logging
from pathlib import Path

logger = logging.getLogger(__name__)

from candidate_processor.file_io import (
    load_candidate_rows,
    parse_candidate_row,
    save_report,
)
from candidate_processor.report import (
    format_candidate_report,
)
from candidate_processor.scoring import (
    evaluate_candidate,
)
from candidate_processor.validation import (
    validate_candidate,
)


BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "candidates_eng04c.csv"
OUTPUT_FILE = BASE_DIR / "candidate_report.txt"


def main() -> None:
    logger.info("Program Starts!")

    rows = load_candidate_rows(INPUT_FILE)

    reports = []
    for row in rows:
        try:
            candidate = parse_candidate_row(row)
            validate_candidate(candidate)

        except (ValueError, KeyError) as error: # error is exception object
            reports.append(
                f"Candidate: {row.get('name', 'Unknown')}\n" 
                # 因为如果 parse 失败, candidate["name"]都不存在, 所以要从 raw row 里取值
                # error handling 不要假设失败步骤已经成功产生 output。
                f"Status: Invalid\n"
                #f"Reason: {error}"
            )
            logger.warning(
                "Skipping invalid candidate: %s", error 
            )
            continue 
            # NOTE 只有当 except 块后面还有属于循环体的其他代码，而你希望发生异常时不要执行这些代码，才必须加 continue。
            # NOTE logger.exception() vs logger.error()
                # logger.exception() 它会自动记录当前 exception 信息，包括 traceback。一般放在：except:里面。
                # logger.error() 这通常只记录 message： ERROR | Failed to save report: Permission denied

        evaluation = evaluate_candidate(candidate)
                    
        report = format_candidate_report(
                                candidate,
                                evaluation,
                            )
                
        reports.append(report)

    logger.info("Loaded %d candidate rows", len(rows))

    full_report = "\n\n".join(reports)
    # NOTE The argument inside .join() must be an iterable where EVERY single element inside it is a string.
    # 这种用法是 Python 中非常经典的“列表收集 + 字符串连接”（List Append + String Join）模式。它通常用于高效地动态拼接大量文本。比 += 性能高很多

    print(full_report)

    try:
        save_report(
        full_report,
        OUTPUT_FILE,)
    except OSError:
        logger.exception("Failed to save candidate report")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format = "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt= "%Y-%m-%d %H:%M:%S",
        filename="candidate_processor.log"
        )
    main()

# if __name__ == "__main__": 的实际用途
    # 当 Python 导入一个模块时，会把里面的代码从头到尾执行一遍。如果你在模块里写了测试代码，不希望别人导入时触发，就要用到这行判断：
# if __name__ == "__main__":
    # 只有当你直接右键运行 main.py 时，下面这两行才会执行
    # # 如果别人 import my_module，下面这两行会被完全忽略
        # print("正在测试我的模块...")
        # print("Program starts")


#__name__ 和 "__main__" 怎么理解？
#每个 Python 文件在运行时，都有一个内置的隐藏属性叫做 __name__。
#这个属性的值取决于你是怎么运行这个文件的：
    #情况 A（直接运行）：如果你在终端直接点击运行 python script.py，那么在这个文件里，__name__ 的值就会被自动设为 "__main__"。
    #情况 B（被动导入）：如果你在别的文件里通过 import script 导入它，那么在这个文件里，__name__ 的值就会变成它自己的文件名（即 "script"）  。

# 一个 Package 里一定要有 main.py 吗？
    # 不需要。Python 的包（Package）绝对不强制包含 main.py。什么时候不需要：如果你的包只是一个供他人调用的工具库（比如用来做数学计算、处理文本），它只需要包含普通的模块文件供别人 import 即可，完全不需要有任何启动入口。什么时候需要：只有当你希望这个包可以作为一个独立程序直接在终端运行时，你才需要一个入口文件。
    
    # Java 程序必须有一个包含 public static void main(String[] args) 的主类作为程序的唯一入口，否则程序根本无法跑起来。但 Python 是脚本语言，它的执行逻辑非常自由：从头到尾执行：Python 解释器在执行一个 .py 文件时，没有任何特定的“入口函数限制”，它就是单纯地从第一行一直执行到最后一行。随处可当入口：任何一个写了可执行代码的 .py 文件，都可以直接作为程序的启动点。

# Python 独特的“包运行机制”：__main__.py
    # 如果你真的想让一个包（文件夹）变得像 Java 的 main 类一样可以直接被整体运行，Python 规定这个包里必须包含一个名字特殊的 __main__.py 文件（注意是双下划线，不是 main.py）。一旦你放了 __main__.py，你就可以在终端直接运行整个文件夹：   
        ## 假设你的文件夹叫 my_app
        # python -m my_app   # Python 就会自动去执行 my_app 包里面的 __main__.py 文件

# NOTE 💡 Python 导入机制铁律 
    # import: 当 Python 遇到 import 语句时，它会把被导入的模块文件最外层的代码从头到尾完整地执行一遍。只有写在 `def` 函数内部的代码不会自动执行（需要被显式调用）。    
    # # 多次 import 会执行多次吗？
        ## 不会。Python 非常聪明。在同一个程序运行期间，一个模块只会被执行一次。当第一次 import tools 时，Python 执行它并将结果缓存在内存中（具体在 sys.modules 里）。如果你在后面又写了十次 import tools，Python 只会直接从内存里拿结果，绝不会重新执行一遍文件。
    # 这就是为什么必须用 if __name__ == "__main__":正因为最外层的代码在 import 时会自动执行，所以如果你在 tools.py 里面写了一些测试代码或者启动逻辑，就会干扰到别人。为了防止这种“误伤”，你必须把只属于自己测试的代码锁起来
    

# 一个 .py 文件里只能有一个 class 吗？
# 不是。这是 Python 与 Java 的一个重大区别。
# Java 强制要求一个文件内只能有一个与文件名同名的 public class
# 在 Python 中，一个 .py 文件内可以写任意数量的 class（类）和函数。在 Python 的设计哲学中，文件（模块）是组织代码的物理单位，而不是逻辑限制。你可以把相关的多个类都放在同一个文件里。


"""
================================================================================
💡 Java 与 Python 核心概念映射速查表 (可直接作为 Python 注释保存)
================================================================================

1. 文件与类的关系 (File & Class):
   - Java  : 一个文件【强制】只能有一个 public class，且文件名必须与类名完全一致。
   - Python: 一个文件可以写【任意多个】class，文件名喜欢叫什么就叫什么。

2. 包的标识 (Package Identifier):
   - Java  : 依靠代码顶部的 `package com.example.app;` 显式声明。
   - Python: 依靠文件夹内是否存在 `__init__.py` 文件（把文件夹识别为代码包）。

3. 程序启动入口 (Program Entry):
   - Java  : 【必须】有特定的 `public static void main(String[] args)` 方法作为唯一死入口。
   - Python: 极其自由。
             - 单文件运行：任何写了可执行代码的 .py 文件都能直接跑，无需固定方法。
             - 整个包运行：如果想直接跑一整个文件夹，包内必须包含 `__main__.py` 文件。

================================================================================
"""


####============= Learning NOTE on logging ================
    # Expected problem
    # + program continues
    # → warning
    # 
    # Serious operation failure
    # → error
    # 
    # Need traceback inside except
    # → exception