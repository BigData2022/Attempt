import numpy as np
number = np.random.randint(1, 101) # загадываем число
count = 0
predict_number = 100

while True:
    count += 1
    
    if predict_number > number:
        maximum = predict_number
        predict_number = (predict_number + 1) // 2
            
    elif predict_number < number:
        minimum = predict_number
        predict_number = (maximum + minimum + 1) // 2
        
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break # конец игры, выход из цикла