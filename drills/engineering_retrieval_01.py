from pathlib import Path
import logging
import argparse

logger = logging.getLogger(__name__)

def build_output_path(filename:str) -> Path:
    return Path("output")/filename # only return Path object, does not create the folder

def validate_score(score:int)-> None:
    if score < 0 or score > 100:
        raise ValueError("Score has to be between 0 and 100") 

# level is considered a int ?? 
def configure_logging(level: int, log_path:Path) -> None:  

      log_path.parent.mkdir(parents=True, exist_ok=True)

      logging.basicConfig(
            level=level,
            # 时间 | level | logger name | message
            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S", 
            filename=log_path
        )  

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        type=Path
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("output/report.txt"),
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true" # action name 是固定字符串，大小写不能自己改
    )

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    level = logging.DEBUG if args.verbose else logging.INFO
    log_path = build_output_path("test1.log") 

    configure_logging(level, log_path) 
    
    logger.info("Program Started")

    candidate = {
    "name": "Alice",
    "score": "abc",
    }

    try:
        score = int(candidate["score"])
        validate_score(score)
        print(score)
    except ValueError:
        print("Invalid candidate score")



main()