# TODO Найдите количество книг, которое можно разместить на дискете
st_ = 100
str_ = 50
sim_ = 25
need_b: int = st_ * str_ * sim_ * 4
need_Mb: float = need_b / (1024 * 1024)
all_ = 1.44 // need_Mb
all_ = int(all_)
print("Количество книг, помещающихся на дискету:", all_)
