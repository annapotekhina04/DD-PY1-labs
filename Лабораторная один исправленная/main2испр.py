# TODO Найдите количество книг, которое можно разместить на дискете
volume_ = 1.44
page_ = 100
line_ = 50
symbol_ = 25
need_bytes: int = page_ * line_ * symbol_ * 4
need_megabytes: float = need_bytes / (1024 * 1024)
all_ = volume_ // need_megabytes
all_ = int(all_)
print("Количество книг, помещающихся на дискету:", all_)
