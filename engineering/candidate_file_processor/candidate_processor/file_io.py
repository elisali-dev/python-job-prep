import csv
import logging
# Inner functions 不需要层层 try/except。Exception 默认会向上传；只有某一层要恢复、转换错误、增加 context，或决定 workflow policy 时，才在那一层 catch。
# 一但你 handle 了 exception 它就不再向上传 exception 上一层即使设计了逻辑也 handle 不到了

logger = logging.getLogger(__name__)

def load_candidate_rows(file_path:str) -> list[dict[str,str]]:
    rows= []
    with open(file_path, "r", encoding="UTF-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    logger.info("Loading candidate rows from %s", file_path)
    return rows 

# parsing 层可以因为“无法把 raw data 转成我们需要的 Python representation”而 raise；
# validation 层负责“数据已经成功转换，但业务上是否合法”。

# NOTE type hint 
# def parse_candidate_row(
#     row: dict[str, str]
# ) -> dict[str, str | float | int | list[str]]:
def parse_candidate_row(row):
    candidate = {
            "name": row["name"],
            "years_experience": float(row["years_experience"]), 
            "technical_score": int(row["technical_score"]),
            "skills": row["skills"].strip().split("|"),
            # [ 更稳妥的除去每个 skill 的 whitespace
                    #   skill.strip()
                    #   for skill in row["skills"].split("|")
                    #   if skill.strip()
                #]
     }
    
    # 因为main() 有 handle ValueError 和 KeyError , 所以这个 inner function
    # 可以不 catch exception 
    # except:
    #     raise ValueError(f"Invalid CSV row:{row}")

    # NOTE 但是如果catch 一个底层 exception → 转换成上层更有意义的 exception → 再往上传。就有意义
    # except KeyError as error:
    #     raise ValueError(
    #         f"Missing CSV field: {error}"
    #     )
    return candidate 



"""
def parse_candidate_row (row):
    try:
        name = row["name"]
        years_experience = row["years_experience"]
        technical_score = row["technical_score"]
        skills = row["skills"].strip()
    # BAD DESIGN - lower-level parser 不应该自己决定“打印一下就算了”。
    # 而且 最后 return candidate 很可能压根没有创建, 导致整个function 还是出错 UnboundLocalError
    except KeyError as error:
        print(f"Invalid Candidate. Candidate Missing Key required {error}")
    else: # 在 try...except...else 结构中，else 块的执行条件非常严格：只有当 try 块中的代码完全没有引发任何异常时，else 块才会执行。
        # 其实这些不用手动判断, 因为他们如果convert 不了自动会 raise ValueError
        # 这些具体值最好交给validation 去判断
        if not name:
            raise ValueError("This candidate has wrong value for his name")
        # BUG float(0) return 0.0 -> not 0.0 -> True 
        # 这会把 0 years experience 判断成 invalid
        if not float(years_experience):
            raise ValueError("Invalid years experience")
        # 同样没考虑0的情况
        if not int(technical_score):
            raise ValueError("Invalid Technical Score")

        candidate = {
            "name": name,
            "years_experience": float(years_experience), 
            "technical_score": int(technical_score),
            "skills": skills.split("|"),
        }

    return candidate
"""
    




#========Iteration 1 =======
"""
def load_candidates(filename):
    candidates = []

    with open(filename, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            candidate = {
                "name": row["name"].strip(),
                "years_experience": float(
                    row["years_experience"]
                ),
                "technical_score": int(
                    row["technical_score"]
                ),
                "skills": [
                    skill.strip()
                    for skill in row["skills"].split("|")
                    if skill.strip()
                ],
            }

            candidates.append(candidate)

    return candidates
"""

def save_report(report_text:str, filename:str) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report_text)