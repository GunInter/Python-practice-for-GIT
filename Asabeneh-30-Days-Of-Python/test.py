# 5. Write check_season(month)
# Return: Autumn, Winter, Spring or Summer
def check_season(month):

    Autumn = ['September', 'October', 'November']
    Winter = ['December', 'January', 'February']
    Spring = ['March', 'April', 'May']
    Summer = ['June', 'July', 'August']

    if month in Autumn:
        return 'Autumn'

    elif month in Winter:
        return 'Winter'

    elif month in Spring:
        return 'Spring'

    elif month in Summer:
        return 'Summer'


print(check_season('September'))
