from django.urls import path
from game.views import index,play # 从game/views.py 里面调用index函数

urlpatterns = [
            path("", index, name="index"),
            path("play/",play,name="play" )
]
