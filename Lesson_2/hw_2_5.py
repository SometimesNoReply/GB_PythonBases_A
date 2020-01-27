# ===================================
# Lesson 2
# Homework. Task 5
# ===================================

rating = [7, 5, 3, 3, 2]

while True:
    print()
    x = input(f'Текущий рейтинг: {rating}. Введите еще одну оценку для рейтинга: ')
    if x.isdecimal():
        # цифра - работаем
        x = int(x)
        cnt = rating.count(x)
        if cnt > 0:
            # есть в списке
            rating.insert(rating.index(x)+cnt, x)
        else:
            # нет в списке
            # ====================================================================================
            # https://docs.python.org/3/library/stdtypes.html?highlight=sort#list.sort
            # говорит:
            #         "The sort() method is guaranteed to be stable. A sort is stable if it guarantees not to change
            #         the relative order of elements that compare equal"
            # этим и воспользуемся, чтобы соблюсти условие задачи:
            # "сохранить правило: при равенстве значений элементов более новые элементы вставлять после более старых"
            # т.е. сортировкой ничего не нарушим
            # ====================================================================================
            rating.append(x)
            rating.sort(reverse=True)
    else:
        # нечисло - выходим (тут же и отрицательные числа ловятся)
        print('Пока. Запускайте ещё')
        break
