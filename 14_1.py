# 10. Составные логические выражения
# 1. Выполните код: мальчик хороший, а программа называет его неряхой. Исправьте код оператором not.

good_boy = True
if not good_boy:
    print('Этот в грязь полез')
    print('и рад,')
    print('что грязна рубаха.')
    print('Про такого говорят:')
    print('он плохой, неряха.')
else:
    print('Этот чистит валенки,')
    print('моет сам галоши.')
    print('Он хотя и маленький,')
    print('но вполне хороший.')
    
# Результат
# Этот чистит валенки,
# моет сам галоши.
# Он хотя и маленький,
# но вполне хороший.