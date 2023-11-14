import re
from . import actions

intent_dict = {
        r"\b([Vv][áãaàâ](?:\sao)?(?:\spara)\ (?:\ o)?[oa]|[Ll]ocomova-se\ at[ée]\ o|[Ss]e\ mova\ at[ée]\ o|[Aa]nde\ at[eé]\ o|[Vv][aá]\ ao)?\s(.+)": actions.go_to
        }

def main():
    command = input("Digite seu pedido: ")
    for key, function in intent_dict.items():
        pattern = re.compile(key)
        point = pattern.findall(command)
        if point:
            print("Ação detectada")
            print(f"{point[0][0]} {point[0][1]}")
            function(point[0][1])
            return

if __name__ == "__main__":
    main()