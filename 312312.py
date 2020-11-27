menu={"아메리카노" :2000, "카페라때" :2500, "그린티라떼" :3000, "모카라떼" :3500}
print("*메뉴별 가격:" , end=" ")
for coffee in menu:
    print(coffee+str(menu[coffee]) + "원" , end=" ")
    print()
    print("*모든 메뉴:" , end= " ")
for coffee in menu:
    print(coffee, end= " ")
    print() 
