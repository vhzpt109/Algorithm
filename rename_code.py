import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == "__main__":
    code_list = os.listdir("BOJ")

    for code in code_list:
        code = code.split('_')[0]
        code = code.split('.')[0]

        html = urlopen("https://www.acmicpc.net/problem/" + code)
        soup = BeautifulSoup(html, "html.parser")
        title = soup.select_one("#problem_title").get_text()

        try:
            os.rename("BOJ/" + code + ".py", "BOJ/" + code + "_" + title + ".py")
        except Exception as e:
            print(e)
            continue

        print(code + ".py -> " + code + "_" + title + ".py")